# 1. Find largest and smallest of two numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Largest:", a)
    print("Smallest:", b)
else:
    print("Largest:", b)
    print("Smallest:", a)


# 2. Find largest and smallest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
largest = max(a, b, c)
smallest = min(a, b, c)
print("Largest:", largest)
print("Smallest:", smallest)


# 3. Check if a number is odd or even
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# 4. Check if number is divisible by 10
num = int(input("Enter a number: "))
if num % 10 == 0:
    print("Divisible by 10")
else:
    print("Not divisible by 10")


# 5. Classify person as Minor or Major
age = int(input("Enter your age: "))
if age < 18:
    print("Minor")
else:
    print("Major")


# 6. Print number of digits in a number
num = int(input("Enter a number: "))
print("Number of digits:", len(str(abs(num))))


# 7. Check if year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")


# 8. Check if triangle is valid based on angles
a = int(input("Enter first angle: "))
b = int(input("Enter second angle: "))
c = int(input("Enter third angle: "))
if a + b + c == 180:
    print("Valid triangle")
else:
    print("Invalid triangle")


# 9. Print absolute value of a number
num = int(input("Enter a number: "))
print("Absolute value:", abs(num))


# 10. Compare area and perimeter of rectangle
length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))
area = length * breadth
perimeter = 2 * (length + breadth)
if area > perimeter:
    print("Area is greater than perimeter")
else:
    print("Perimeter is greater than or equal to area")


# 11. Check if three points are collinear
x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())
x3, y3 = map(int, input("Enter x3 y3: ").split())
# Check using slope comparison
if (y2 - y1)*(x3 - x2) == (y3 - y2)*(x2 - x1):
    print("Points are collinear")
else:
    print("Points are not collinear")


# 12. Check if point lies inside, on or outside a circle
import math
x, y = map(float, input("Enter point (x y): ").split())
cx, cy = map(float, input("Enter circle center (cx cy): ").split())
r = float(input("Enter radius: "))
distance = math.sqrt((x - cx)**2 + (y - cy)**2)
if distance < r:
    print("Inside the circle")
elif distance == r:
    print("On the circle")
else:
    print("Outside the circle")


# 13. Convert number 0 to 19 to words
num = int(input("Enter number (0-19): "))
words = ["Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine",
         "Ten", "Eleven", "Twelve", "Thirteen", "Fourteen", "Fifteen", "Sixteen",
         "Seventeen", "Eighteen", "Nineteen"]
if 0 <= num <= 19:
    print("Word:", words[num])
else:
    print("Number out of range")


# 14. Check student pass/fail and assign grade
marks = []
for i in range(3):
    m = input(f"Enter marks for subject {i+1} (or type 'Absent'): ")
    if m.lower() == 'absent':
        marks.append(-1)
    else:
        marks.append(int(m))

grades = []
passed = True
for m in marks:
    if m == -1:
        grades.append("NA")
        passed = False
    elif m <= 39:
        grades.append("F")
        passed = False
    elif m <= 44:
        grades.append("P")
    elif m <= 49:
        grades.append("C")
    elif m <= 54:
        grades.append("B")
    elif m <= 59:
        grades.append("B+")
    elif m <= 69:
        grades.append("A")
    elif m <= 79:
        grades.append("A+")
    else:
        grades.append("O")

total = sum([m for m in marks if m != -1])
average = total / len([m for m in marks if m != -1])
print("Grades:", grades)
print("Total:", total)
print("Average:", average)
print("Result:", "Pass" if passed else "Fail")
