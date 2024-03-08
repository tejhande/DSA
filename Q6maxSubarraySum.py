# Find the largest sum contiguous subarray
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Test the function
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
largest_sum = max_subarray_sum(arr)
print(largest_sum)