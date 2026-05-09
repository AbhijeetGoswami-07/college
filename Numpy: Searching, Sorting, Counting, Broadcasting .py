import numpy as np

# Input array from the user
array1 = np.array(list(map(int, input().split())))

# Searching
search_value = int(input("Value to search: "))
count_value = int(input("Value to count: "))
broadcast_value = int(input("Value to add: "))

# Searching → indices where value matches
indices = np.where(array1 == search_value)[0]
print(indices)

# Counting → number of occurrences
count = np.count_nonzero(array1 == count_value)
print(count)

# Broadcasting → add value to each element
broadcasted_array = array1 + broadcast_value
print(broadcasted_array)

# Sorting → sort array in ascending order
sorted_array = np.sort(array1)
print(sorted_array)
