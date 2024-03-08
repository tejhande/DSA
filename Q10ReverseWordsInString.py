# Implement a function to reverse words in a string
def reverse_words(s):
    words = s.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string

# Test the function
test_string = "hello world"
result = reverse_words(test_string)
print(result)