# Task 1: Define three functions and call them in a loop
def fun1():
    print("Function 1 called")
def disp1():
    print("Display 1 called")
def msg1():
    print("Message 1 called")
functions = [fun1, disp1, msg1]
for func in functions:
    func()

# Task 2: Add corresponding elements of two lists using map and lambda
list1 = [1, 2, 3, 4, 5, 6]
list2 = [6, 5, 4, 3, 2, 1]
sum_list = list(map(lambda x, y: x + y, list1, list2))
print("Sum list:", sum_list)

# Task 3: Generate 10 random numbers (-15 to 15), create square list
numbers = [random.randint(-15, 15) for _ in range(10)]
squares = [x * x for x in numbers]
print("Original numbers:", numbers)
print("Squares:", squares)

# Task 4: Print palindromes from list
lst = ["madam", "python", "malayalam", "12321"]
palindromes = [s for s in lst if s == s[::-1]]
print("Palindromes:", palindromes)

# Task 5: Filter names longer than 8 characters
faculty = ["Christopher", "Alice", "RobertJohnson", "Bob"]
long_names = [name for name in faculty if len(name) > 8]
print("Names longer than 8 characters:", long_names)
