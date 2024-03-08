# Find the duplicate number in an array
def find_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)

# Test the function
arr = [1, 3, 4, 2, 2]
duplicate_num = find_duplicate(arr)
print(duplicate_num)
