# 1. Count how many vowels are there in a string. Accept the string from the user.

def count_vowels(s):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

# Example
# print(count_vowels("Hello World"))

# 2. Convert string to lower/upper/toggle case without using built-in functions

def to_lower_case(s):
    result = ''
    for char in s:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

def to_upper_case(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    return result

def toggle_case(s):
    result = ''
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        elif 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char
    return result

# Example
# print(to_lower_case("HeLLo"))
# print(to_upper_case("HeLLo"))
# print(toggle_case("HeLLo"))

# 3. Accept two strings. Check whether one string is there in another string.

def is_substring(main_str, sub_str):
    return sub_str in main_str

# Example
# print(is_substring("abcdef", "cd"))

# 4. Write a function that removes one string from another string, if present.

def remove_substring(main_str, remove_str):
    result = ''
    i = 0
    while i < len(main_str):
        found = False
        if main_str[i:i+len(remove_str)] == remove_str:
            found = True
            i += len(remove_str)
        if not found:
            result += main_str[i]
            i += 1
    return result

# Example
# print(remove_substring("abcdef", "cd"))
