# Task 1: Count boys and girls in a list (boys as tuples)
mixed_list = [("John", 20), "Alice", ("Bob", 21), "Eve", ("Charlie", 22)]
boys = len([x for x in mixed_list if isinstance(x, tuple)])
girls = len(mixed_list) - boys
print("Number of boys:", boys)
print("Number of girls:", girls)

# Task 2: Create three lists from tuples (roll no, name, age)
students = [("101", "John", 20), ("102", "Alice", 21), ("103", "Bob", 22)]
roll_no = [t[0] for t in students]
names = [t[1] for t in students]
ages = [t[2] for t in students]
print("Roll No:", roll_no)
print("Names:", names)
print("Ages:", ages)

# Task 3: Find days between two date tuples
from datetime import datetime
date1 = (2023, 4, 1)  # (year, month, day)
date2 = (2023, 4, 10)
d1 = datetime(date1[0], date1[1], date1[2])
d2 = datetime(date2[0], date2[1], date2[2])
days_diff = (d2 - d1).days
print("Days between dates:", days_diff)

# Task 4: Create list of tuples (food, price), sort by price descending
food_prices = [("Apple", 1.5), ("Banana", 0.5), ("Orange", 2.0)]
food_prices.sort(key=lambda x: x[1], reverse=True)
print("Sorted food prices:", food_prices)

# Task 5: Remove empty tuples from list
tuple_list = [(1, 2), (), (3, 4), (), (5,)]
cleaned_list = [t for t in tuple_list if t]
print("Original list:", tuple_list)
print("Cleaned list:", cleaned_list)

# Task 6: Modify an element of a tuple (convert to list, modify, back to tuple)
t = (1, 2, 3)
t_list = list(t)
t_list[1] = 5
t = tuple(t_list)
print("Modified tuple:", t)

# Task 7: Delete an element of a tuple (convert to list, remove, back to tuple)
t = (1, 2, 3, 4)
t_list = list(t)
t_list.remove(2)
t = tuple(t_list)
print("Tuple after deletion:", t)
