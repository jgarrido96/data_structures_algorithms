def simple_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


# Task 1: Identifying Key Operations
#   Analyze the provided algorithm and identify the key operations it performs.

# This operation orders an array 


# Task 2: Calculating Big O Complexity
# Apply the principles of Big O notation to express how the algorithm's runtime grows concerning the size of the input

import time

start_time = time.time()

print(simple_sort([1, 7, 6, 3, 4, 5, 2, 8, 9, 10]))

end_time = time.time()
insert_beginning_time = end_time - start_time
print("Time taken to order the array:", insert_beginning_time)

# Task 3: Efficiency Analysis:
# Propose potential improvements or alternative algorithms that might offer better performance

# One thing could be using the .sort() method

array = [1, 7, 6, 3, 4, 5, 2, 8, 9, 10]
print(f'Unorereded array: {array}')
array.sort()
print(f'Ordered array: {array}')