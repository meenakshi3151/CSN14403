# Given a NumPy array, find the indices of the minimum and maximum elements, and swap those elements without affecting the rest of the array.
import numpy as np

a = input("Enter size of array: ")
arr = np.array([])
for i in range(int(a)):
    num = input("Enter the number: ")
    arr=np.append(arr, int(num))
max_index = arr.argmax()
min_index = arr.argmin()
print("Array before swapping is: ")
print(arr)
temp = arr[max_index]
arr[max_index] = arr[min_index]
arr[min_index] = temp

print("Array after swapping is: ")
print(arr)
