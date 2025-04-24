# Task 1: Print all alphabets in upper and lower case
print("Uppercase Alphabets:")
for i in range(65, 91):  # ASCII for A-Z
    print(chr(i), end=" ")
print("\nLowercase Alphabets:")
for i in range(97, 123):  # ASCII for a-z
    print(chr(i), end=" ")
print()

# Task 2: Print a multiplication table of a given number
num = int(input("\nEnter a number for multiplication table: "))
print(f"Multiplication table of {num}:")
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")

# Task 3: Count number of alphabets and digits in a string
string = input("\nEnter a string: ")
alphabets = 0
digits = 0
for char in string:
    if char.isalpha():
        alphabets += 1
    elif char.isdigit():
        digits += 1
print(f"Alphabets: {alphabets}, Digits: {digits}")

# Task 4: Check if a number is prime, perfect, Armstrong, palindrome, or automorphic
num = int(input("\nEnter a number to check properties: "))
# Prime
is_prime = True
if num < 2:
    is_prime = False
for i in range(2, int(num ** 0.5) + 1):
    if num % i == 0:
        is_prime = False
# Perfect
sum_of_divisors = 0
for i in range(1, num):
    if num % i == 0:
        sum_of_divisors += i
is_perfect = (sum_of_divisors == num)
# Armstrong
sum_of_powers = 0
temp = num
while temp > 0:
    digit = temp % 10
    sum_of_powers += digit ** 3  # For 3-digit numbers
    temp //= 10
is_armstrong = (sum_of_powers == num)
# Palindrome
is_palindrome = str(num) == str(num)[::-1]
# Automorphic
square = num * num
is_automorphic = str(square).endswith(str(num))
print(f"Prime: {is_prime}, Perfect: {is_perfect}, Armstrong: {is_armstrong}, Palindrome: {is_palindrome}, Automorphic: {is_automorphic}")

# Task 5: Generate Pythagorean triplets with side length <= 30
print("\nPythagorean Triplets with sides <= 30:")
for a in range(1, 31):
    for b in range(a, 31):
        for c in range(b, 31):
            if a * a + b * b == c * c:
                print(f"({a}, {b}, {c})")

# Task 6: Print 24 hours of the day with AM, PM, Noon, Midnight
print("\n24 Hours of the Day:")
for hour in range(24):
    if hour == 0:
        print("12 AM (Midnight)")
    elif hour == 12:
        print("12 PM (Noon)")
    elif hour < 12:
        print(f"{hour} AM")
    else:
        print(f"{hour - 12} PM")

# Task 7: Print nCr and nPr (combinations and permutations)
n = int(input("\nEnter n for nCr and nPr: "))
r = int(input("Enter r for nCr and nPr: "))
def factorial(x):
    result = 1
    for i in range(1, x + 1):
        result *= i
    return result
nCr = factorial(n) // (factorial(r) * factorial(n - r))
nPr = factorial(n) // factorial(n - r)
print(f"nCr = {nCr}, nPr = {nPr}")

# Task 8: Print factorial of a given number
num = int(input("\nEnter a number to find factorial: "))
fact = factorial(num)
print(f"Factorial of {num} is {fact}")

# Task 9: Print N natural numbers in reverse
N = int(input("\nEnter N to print natural numbers in reverse: "))
print(f"First {N} natural numbers in reverse:")
for i in range(N, 0, -1):
    print(i, end=" ")
print()

# Task 10: Generate N numbers of Fibonacci series
N = int(input("\nEnter N for Fibonacci series: "))
print(f"First {N} Fibonacci numbers:")
a, b = 0, 1
for i in range(N):
    print(a, end=" ")
    a, b = b, a + b
print()

# Task 11: Calculate sin(x) using the given series (x is in radians)
x = float(input("\nEnter x in degrees to calculate sin(x): "))
x_rad = x * 3.14159 / 180  # Convert degrees to radians
sin_x = x_rad  # First term: x
term = x_rad
for n in range(1, 5):  # We'll use first few terms for simplicity
    term *= -1 * x_rad * x_rad / (2 * n * (2 * n + 1))
    sin_x += term
print(f"sin({x}) = {sin_x}")
