# Using a labeled dataset perform dimensionality reduction using
# both PCA and LDA.
# Perform the following tasks:
# 1 Visualize the results of PCA and LDA side-by-side in a 2D plot.
# 2 Discuss the differences in the data representation by PCA and LDA.
# 3 Analyze which method works better for this specific dataset and justify why.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import metrics

# Load the iris dataset
data = load_iris()
X = data.data[:100]  # First 100 records
y = data.target[:100]  # Corresponding labels (only first 100)

# Standardize the data (important for PCA)
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Split dataset into training and testing set (for LDA purposes)
X_train, X_test, y_train, y_test = train_test_split(
    X_scaled, y, test_size=0.3, random_state=42
)

# 1. PCA (Principal Component Analysis)
pca = PCA(n_components=2)  # Reduce to 2D
X_pca = pca.fit_transform(X_scaled)

# 2. LDA (Linear Discriminant Analysis)
lda = LDA(n_components=2)  # LDA also reduces to 2D
X_lda = lda.fit_transform(X_train, y_train)

# 3. Visualize PCA and LDA results side by side

fig, axs = plt.subplots(1, 2, figsize=(14, 6))

# Plot PCA
axs[0].scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap="viridis", edgecolor="k")
axs[0].set_title("PCA: First 2 Principal Components")
axs[0].set_xlabel("Principal Component 1")
axs[0].set_ylabel("Principal Component 2")

# Plot LDA
axs[1].scatter(X_lda[:, 0], X_lda[:, 1], c=y_train, cmap="viridis", edgecolor="k")
axs[1].set_title("LDA: First 2 Discriminant Components")
axs[1].set_xlabel("LD 1")
axs[1].set_ylabel("LD 2")

plt.tight_layout()
plt.show()

# 4. Evaluate and compare models (optional, only for LDA)
lda_pred = lda.predict(X_test)
accuracy = metrics.accuracy_score(y_test, lda_pred)
print(f"LDA Classification Accuracy: {accuracy:.2f}")

# Output Results for PCA and LDA
print("\nPCA Explained Variance Ratio:", pca.explained_variance_ratio_)
print(
    "LDA Explained Variance Ratio:",
    np.var(X_lda, axis=0) / np.var(X_train, axis=0).sum(),
)

# Conclusion:
# - PCA: Does not consider class labels and seeks to maximize variance, leading to a more general representation of data.
# - LDA: Seeks to maximize the separation between the classes, so it is more suited for classification tasks, resulting in a better data representation for class separation.
