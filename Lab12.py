# Task 1: Complex number class with addition, subtraction, multiplication, division
class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    def __add__(self, other):
        return Complex(self.real + other.real, self.imag + other.imag)
    def __sub__(self, other):
        return Complex(self.real - other.real, self.imag - other.imag)
    def __mul__(self, other):
        real = self.real * other.real - self.imag * other.imag
        imag = self.real * other.imag + self.imag * other.real
        return Complex(real, imag)
    def __truediv__(self, other):
        denominator = other.real**2 + other.imag**2
        real = (self.real * other.real + self.imag * other.imag) / denominator
        imag = (self.imag * other.real - self.real * other.imag) / denominator
        return Complex(real, imag)
    def __str__(self):
        return f"{self.real} + {self.imag}i"

c1 = Complex(1, 2)
c2 = Complex(3, 4)
print("Addition:", c1 + c2)
print("Subtraction:", c1 - c2)
print("Multiplication:", c1 * c2)
print("Division:", c1 / c2)

# Task 2: Matrix class with addition, multiplication, transpose for 3x3 matrices
class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix  # 3x3 matrix as list of lists
    def __add__(self, other):
        return Matrix([[self.matrix[i][j] + other.matrix[i][j] for j in range(3)] for i in range(3)])
    def __mul__(self, other):
        result = [[sum(a * b for a, b in zip(row, col)) for col in zip(*other.matrix)] for row in self.matrix]
        return Matrix(result)
    def transpose(self):
        return Matrix([[self.matrix[j][i] for j in range(3)] for i in range(3)])
    def __str__(self):
        return "\n".join([" ".join(map(str, row)) for row in self.matrix])

m1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
m2 = Matrix([[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Matrix 1:\n", m1)
print("Matrix 2:\n", m2)
print("Addition:\n", m1 + m2)
print("Multiplication:\n", m1 * m2)
print("Transpose of Matrix 1:\n", m1.transpose())

# Task 3: Class for surface area and volume of a solid
class Solid:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    def surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)
    def volume(self):
        return self.length * self.width * self.height

s = Solid(2, 3, 4)
print("Surface Area:", s.surface_area())
print("Volume:", s.volume())

# Task 4: Class for perimeter/circumference and area of a regular shape
class Shape:
    def __init__(self, side):
        self.side = side
    def perimeter(self):
        return 4 * self.side  # Assuming square for simplicity
    def area(self):
        return self.side * self.side

s = Shape(5)
print("Perimeter:", s.perimeter())
print("Area:", s.area())

# Task 5: Time class for arithmetic operations
class Time:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes
    def __add__(self, other):
        total_minutes = self.hours * 60 + self.minutes + other.hours * 60 + other.minutes
        new_hours = total_minutes // 60
        new_minutes = total_minutes % 60
        return Time(new_hours, new_minutes)
    def __str__(self):
        return f"{self.hours} hrs {self.minutes} mins"

t1 = Time(2, 30)
t2 = Time(1, 45)
print("Time 1:", t1)
print("Time 2:", t2)
print("Sum:", t1 + t2)

# Task 6: Date class with list attributes and overloaded == operator
class Date:
    def __init__(self, day, month, year):
        self.date = [day, month, year]
    def __eq__(self, other):
        return self.date == other.date
    def __str__(self):
        return f"{self.date[0]}/{self.date[1]}/{self.date[2]}"

d1 = Date(1, 4, 2023)
d2 = Date(1, 4, 2023)
d3 = Date(2, 4, 2023)
print("Date 1:", d1)
print("Date 2:", d2)
print("Date 1 == Date 2:", d1 == d2)
print("Date 1 == Date 3:", d1 == d3)

# Task 7: Weather class with overloaded in operator
class Weather:
    def __init__(self, parameters):
        self.params = parameters
    def __contains__(self, item):
        return item in self.params
    def __str__(self):
        return str(self.params)

w = Weather(["rain", "sun", "wind"])
print("Weather parameters:", w)
print("Is 'rain' in weather?", "rain" in w)
print("Is 'snow' in weather?", "snow" in w)

# Task 8: String class with overloaded + and methods toLower, toUpper
class String:
    def __init__(self, text):
        self.text = text
    def __add__(self, other):
        return String(self.text + other.text)
    def toLower(self):
        return String(self.text.lower())
    def toUpper(self):
        return String(self.text.upper())
    def __str__(self):
        return self.text

s1 = String("Hello")
s2 = String("World")
print("String 1:", s1)
print("String 2:", s2)
print("Concatenated:", s1 + s2)
print("To Lower:", s1.toLower())
print("To Upper:", s1.toUpper())
