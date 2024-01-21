# Create a 5x5 NumPy array filled with the square of the numbers from 1 to 25 using broadcasting.
import numpy as np
arr=np.arange(1,26)
arr=arr.reshape(5,5)**2
print(arr)

