# Q2 answer =  b) 2
# Twitter:-- @DSA_Python
# Rotate an array
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
k %= n  # Handling the case when k is greater 
        # than the length of the array
arr[:] = arr[-k:] + arr[:-k]

print(arr)

# What is the output of the following code?
# a) [2, 3, 4, 5, 1]
# b) [5, 1, 2, 3, 4]
# c) [3, 4, 5, 1, 2]
# d) [4, 5, 1, 2, 3]