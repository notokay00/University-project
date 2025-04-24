# Task 1: Define count_lower_upper() to count uppercase and lowercase, return as dictionary
def count_lower_upper(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    return {"uppercase": upper, "lowercase": lower}

test_string = "HeLLo WoRLd"
result = count_lower_upper(test_string)
print("Count of uppercase and lowercase:", result)

# Task 2: Define compute() to calculate n + nn + nnn + nnnn, test for digits 4 to 7
def compute(n):
    n_str = str(n)
    return n + int(n_str + n_str) + int(n_str + n_str + n_str) + int(n_str + n_str + n_str + n_str)

for digit in range(4, 8):
    print(f"compute({digit}) = {compute(digit)}")

# Task 3: Define create_array() to create and return 3D array with given dimensions and value
def create_array(dim1, dim2, dim3, value):
    return [[[value for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]

array = create_array(3, 4, 5, 0)
print("3D Array (first element of each dimension):", array[0][0][0])

# Task 4: Define sum_avg() to accept marks of five subjects, return total and average
def sum_avg(sub1, sub2, sub3, sub4, sub5):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    average = total / 5
    return total, average

marks = (85, 90, 88, 92, 87)
total, avg = sum_avg(*marks)
print(f"Total: {total}, Average: {avg}")

# Task 5: Define ispangram() to check if string is pangram
def ispangram(string):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet.issubset(set(string.lower()))

test1 = "The quick brown fox jumps over the lazy dog"
test2 = "Crazy Fredrick bought many very exquisite opal jewels"
print(f"Is '{test1}' a pangram?", ispangram(test1))
print(f"Is '{test2}' a pangram?", ispangram(test2))

# Task 6: Define function to create list of tuples (x, x^2) for x from 1 to end
def create_tuples(end):
    return [(x, x**2) for x in range(1, end + 1)]

result = create_tuples(5)
print("Tuples (x, x^2):", result)

# Task 7: Define ispalindrome() to check palindrome, ignore spaces and case
def ispalindrome(string):
    cleaned = ''.join(char.lower() for char in string if char.isalnum())
    return cleaned == cleaned[::-1]

test1 = "A man a plan a canal Panama"
test2 = "race a car"
print(f"Is '{test1}' a palindrome?", ispalindrome(test1))
print(f"Is '{test2}' a palindrome?", ispalindrome(test2))
