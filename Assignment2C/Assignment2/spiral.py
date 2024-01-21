# Create a 5x5 NumPy array with values ranging from 1 to 25 in a spiral pattern.
import numpy as np
arr=np.array([[1,2,3,4,5],[10,9,8,7,6],[11,12,13,14,15],[20,19,18,17,16],[21,22,23,24,25]])
print("Spiral array is: ")
# print(arr)
for i in range(5):
    for j in range(5):
        print(arr[i][j],end=" ")
    print()
    