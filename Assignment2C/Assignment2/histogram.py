# Generate 1000 random samples from a standard normal distribution and plot their histogram using Matplotlib.
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)
random_samples = np.random.randn(1000)

plt.hist(random_samples, bins=30, edgecolor='blue', color='skyblue')
plt.title('Histogram of 1000 Random Samples from Standard Normal Distribution')
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
