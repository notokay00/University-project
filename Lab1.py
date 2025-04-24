# --------------------------------------------
# Program 1: Add two numbers
# --------------------------------------------
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum:", a + b)

# --------------------------------------------
# Program 2: Subtract two numbers
# --------------------------------------------
print("Difference:", a - b)

# --------------------------------------------
# Program 3: Multiply two numbers
# --------------------------------------------
print("Product:", a * b)

# --------------------------------------------
# Program 4: Divide two numbers
# --------------------------------------------
print("Quotient:", a / b)

# --------------------------------------------
# Program 5: Add, Subtract, Multiply, Divide
# --------------------------------------------
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)

# --------------------------------------------
# Program 6: Convert hours into minutes
# --------------------------------------------
hours = int(input("Enter hours: "))
print("Minutes:", hours * 60)

# --------------------------------------------
# Program 7: Convert minutes into hours
# --------------------------------------------
minutes = int(input("Enter minutes: "))
print("Hours:", minutes / 60)

# --------------------------------------------
# Program 8: Convert dollars into Rs. (1$ = 48Rs)
# --------------------------------------------
dollars = float(input("Enter dollars: "))
print("Rupees:", dollars * 48)

# --------------------------------------------
# Program 9: Convert Rs. into dollars (1$ = 48Rs)
# --------------------------------------------
rs = float(input("Enter rupees: "))
print("Dollars:", rs / 48)

# --------------------------------------------
# Program 10: Convert dollars into pounds
# 1$ = 48 Rs, 1 pound = 70 Rs
# --------------------------------------------
dollars = float(input("Enter dollars: "))
rs = dollars * 48
pounds = rs / 70
print("Pounds:", pounds)

# --------------------------------------------
# Program 11: Convert grams into kg
# --------------------------------------------
grams = float(input("Enter grams: "))
print("Kilograms:", grams / 1000)

# --------------------------------------------
# Program 12: Convert kg into grams
# --------------------------------------------
kg = float(input("Enter kilograms: "))
print("Grams:", kg * 1000)

# --------------------------------------------
# Program 13: Convert bytes into KB, MB, GB
# --------------------------------------------
bytes_ = int(input("Enter bytes: "))
print("KB:", bytes_ / 1024)
print("MB:", bytes_ / (1024**2))
print("GB:", bytes_ / (1024**3))

# --------------------------------------------
# Program 14: Celsius to Fahrenheit
# --------------------------------------------
c = float(input("Enter Celsius: "))
f = (9/5 * c) + 32
print("Fahrenheit:", f)

# --------------------------------------------
# Program 15: Fahrenheit to Celsius
# --------------------------------------------
f = float(input("Enter Fahrenheit: "))
c = 5/9 * (f - 32)
print("Celsius:", c)

# --------------------------------------------
# Program 16: Calculate simple interest (I = P * R * N / 100)
# --------------------------------------------
p = float(input("Enter Principal: "))
r = float(input("Enter Rate: "))
n = float(input("Enter Time (years): "))
i = (p * r * n) / 100
print("Interest:", i)

# --------------------------------------------
# Program 17: Area & Perimeter of Square
# --------------------------------------------
l = float(input("Enter side length of square: "))
print("Area:", l ** 2)
print("Perimeter:", 4 * l)

# --------------------------------------------
# Program 18: Area & Perimeter of Rectangle
# --------------------------------------------
l = float(input("Enter length: "))
b = float(input("Enter breadth: "))
print("Area:", l * b)
print("Perimeter:", 2 * (l + b))

# --------------------------------------------
# Program 19: Area of a Circle (A = 22/7 * R * R)
# --------------------------------------------
r = float(input("Enter radius: "))
print("Area of circle:", (22/7) * r * r)

# --------------------------------------------
# Program 20: Area of a Triangle (A = 0.5 * H * B)
# --------------------------------------------
h = float(input("Enter height: "))
b = float(input("Enter base: "))
print("Area of triangle:", 0.5 * h * b)

# --------------------------------------------
# Program 21: Calculate Net Salary
# Allowance = 10% of gross, Deduction = 3% of gross
# --------------------------------------------
gross = float(input("Enter gross salary: "))
allowance = 0.10 * gross
deduction = 0.03 * gross
net_salary = gross + allowance - deduction
print("Net Salary:", net_salary)

# --------------------------------------------
# Program 22: Calculate Net Sales (Net = Gross - 10% discount)
# --------------------------------------------
gross_sales = float(input("Enter gross sales: "))
discount = 0.10 * gross_sales
net_sales = gross_sales - discount
print("Net Sales:", net_sales)

# --------------------------------------------
# Program 23: Average of Three Subjects
# --------------------------------------------
s1 = float(input("Enter marks of subject 1: "))
s2 = float(input("Enter marks of subject 2: "))
s3 = float(input("Enter marks of subject 3: "))
total = s1 + s2 + s3
average = total / 3
print("Total:", total)
print("Average:", average)

# --------------------------------------------
# Program 24: Swap Two Values
# --------------------------------------------
a = input("Enter value of A: ")
b = input("Enter value of B: ")
a, b = b, a
print("After swapping - A:", a, "B:", b)
