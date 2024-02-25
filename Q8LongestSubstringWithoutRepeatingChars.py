# Q7 answer = a) 123 followed by 123
# Twitter:-- @DSA_Python
# Find the longest substring without repeating characters
def longest_substring(s):
    max_length = 0
    start = 0
    char_index_map = {}

    for i, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        else:
            max_length = max(max_length, i - start + 1)
        char_index_map[char] = i

    return max_length

# Test the function
test_string = "abcabcbb"
result = longest_substring(test_string)
print(result)
# What is the output of the following code?
# a) 3
# b) 4
# c) 5
# d) 6