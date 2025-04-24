# Task 1: Convert words in list to uppercase and store in set
words = ["apple", "banana", "cherry", "date"]
upper_set = set(word.upper() for word in words)
print("Uppercase set:", upper_set)

# Task 2: Create set of 10 random numbers (15-45), count < 30, delete > 35
numbers = set(random.randint(15, 45) for _ in range(10))
print("Original set:", numbers)
count_less_30 = len([x for x in numbers if x < 30])
print("Numbers less than 30:", count_less_30)
numbers = {x for x in numbers if x <= 35}
print("Set after deleting > 35:", numbers)

# Task 3: Create empty set, add 5 names, modify one, delete two
name_set = set()
name_set.update(["Alice", "Bob", "Charlie", "David", "Eve"])
print("Initial set:", name_set)
name_set.remove("Charlie")
name_set.add("Charles")  # Modify
name_set.remove("David")
name_set.remove("Eve")
print("Modified set:", name_set)

# Task 4: Separate names starting with A and B
names = {"Alice", "Bob", "Anna", "Ben", "Charlie"}
set_a = {name for name in names if name.startswith("A")}
set_b = {name for name in names if name.startswith("B")}
print("Names starting with A:", set_a)
print("Names starting with B:", set_b)
