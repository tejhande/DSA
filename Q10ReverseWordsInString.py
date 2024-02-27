# Q9 answer = a) 2
# Twitter:-- @DSA_Python
# Implement a function to reverse words in a string
def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Test the function
test_string = "hello world"
result = reverse_words(test_string)
print(result)
# What is the output of the following code?
# a) "world hello"
# b) "olleh dlrow"
# c) "dlrow hello"
# d) "hello world"