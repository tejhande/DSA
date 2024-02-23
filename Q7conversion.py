# Q6 answer = a)6
# Twitter:-- @DSA_Python
# atoi: Convert a string to an integer
def atoi(s):
    num = 0
    sign = 1
    i = 0
    if s[0] == '-':
        sign = -1
        i = 1
    while i < len(s):
        num = num * 10 + ord(s[i]) - ord('0')
        i += 1
    return sign * num

# itoa: Convert an integer to a string
def itoa(num):
    if num == 0:
        return "0"
    sign = 1
    if num < 0:
        sign = -1
        num = -num
    result = ""
    while num > 0:
        result = chr(num % 10 + ord('0')) + result
        num //= 10
    if sign == -1:
        result = '-' + result
    return result

# Test the functions
num_str = "123"
str_num = 123
result_1 = atoi(num_str)
result_2 = itoa(str_num)
print(result_1)
print(result_2)

# What is the output of the following code?
# a) 123 followed by 123
# b) 123 followed by "123"
# c) 123 followed by "321"
# d) 123 followed by -123