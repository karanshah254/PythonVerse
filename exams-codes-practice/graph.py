import matplotlib.pyplot as plt
import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a plot
fig, ax = plt.subplots()
ax.plot(x, y, label="Sine Wave")

# Add a label
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_title("Example Plot with Labels, Annotations, and Legend")

# Add an annotation
ax.annotate(
    "Max Point",
    xy=(np.pi / 2, 1),
    xytext=(np.pi / 2 + 1, 1.5),
    arrowprops=dict(facecolor="black", shrink=0.05),
)

# Add a legend
ax.legend()

# Show the plot
plt.show()
