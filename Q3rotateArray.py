# Rotate an array
arr = [1, 2, 3, 4, 5]
k = 2
n = len(arr)
k %= n  # Handling the case when k is greater 
        # than the length of the array
arr[:] = arr[-k:] + arr[:-k]

print(arr)
