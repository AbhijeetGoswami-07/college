import numpy as np


r, c = map(int, input().split())


elements = []
for _ in range(r):
    row = list(map(int, input().split()))
    elements.extend(row)
arr = np.array(elements).reshape(r, c)


print(arr)          
print(arr.ndim)     
print(arr.shape)    
print(arr.size)     


#Write a Python program to create a NumPy array based on user input and display the following:
# The created NumPy array.
# The number of dimensions of the array using ndim
# The shape of the array using shape
# The total number of elements in the array using size
# Assume all input elements are valid integers.
