# Implement strstr (substring search)
def strstr(haystack, needle):
    if not needle:
        return 0
    for i in range(len(haystack) - len(needle) + 1):
        if haystack[i:i+len(needle)] == needle:
            return i
    return -1

# Test the function
haystack = "hello"
needle = "ll"
result = strstr(haystack, needle)
print(result)