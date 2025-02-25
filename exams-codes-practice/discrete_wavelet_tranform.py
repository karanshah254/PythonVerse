import numpy as np
import matplotlib.pyplot as plt
from skimage import data, color, io # type: ignore
from skimage.transform import resize # type: ignore
import pywt # type: ignore
import pywt.data # type: ignore

# Load a grayscale image (MRI scan example)
image = data.brain()  # Skimage has a built-in brain MRI image for demonstration
image = color.rgb2gray(image)  # Convert to grayscale if necessary
image = resize(image, (256, 256))  # Resize for consistency in processing

# Plot the original image
plt.figure(figsize=(8, 8))
plt.subplot(1, 2, 1)
plt.title("Original Image")
plt.imshow(image, cmap="gray")
plt.axis("off")

# Perform Discrete Wavelet Transform (DWT) using 'haar' wavelet (simple choice for illustration)
coeffs2 = pywt.dwt2(image, "haar")
LL, (LH, HL, HH) = coeffs2  # LL is the approximation, LH, HL, HH are the details

# Zeroing out the details (LH, HL, HH) for compression
threshold = 0.1
LH = np.where(np.abs(LH) < threshold, 0, LH)
HL = np.where(np.abs(HL) < threshold, 0, HL)
HH = np.where(np.abs(HH) < threshold, 0, HH)

# Inverse DWT to reconstruct the compressed image
coeffs2_compressed = LL, (LH, HL, HH)
compressed_image = pywt.idwt2(coeffs2_compressed, "haar")

# Plot the compressed image
plt.subplot(1, 2, 2)
plt.title("Compressed Image")
plt.imshow(compressed_image, cmap="gray")
plt.axis("off")
plt.show()

# Displaying compression results
original_size = image.nbytes
compressed_size = coeffs2[0].nbytes + LH.nbytes + HL.nbytes + HH.nbytes
compression_ratio = original_size / compressed_size

print(f"Original Image Size: {original_size} bytes")
print(f"Compressed Image Size: {compressed_size} bytes")
print(f"Compression Ratio: {compression_ratio:.2f}")

# Observations:
# The original image is decomposed into approximation and detail coefficients.
# By reducing the detail coefficients, we achieve compression.
# The image quality may degrade as more detail coefficients are removed.
