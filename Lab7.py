# Task 1: Create three dictionaries and concatenate them
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}
dict3 = {"e": 5, "f": 6}
dict4 = {**dict1, **dict2, **dict3}
print("Concatenated dictionary:", dict4)

# Task 2: Check if a dictionary is empty
my_dict = {}
print("Is dictionary empty?", not bool(my_dict))
my_dict = {"key": "value"}
print("Is dictionary empty?", not bool(my_dict))

# Task 3: Dictionary with dept no, employee roll no, salary, find min/max per dept
employees = {
    "HR": [("101", 50000), ("102", 60000)],
    "IT": [("201", 70000), ("202", 80000)]
}
dept_min_max = {}
for dept, emp_list in employees.items():
    salaries = [salary for _, salary in emp_list]
    dept_min_max[dept] = (min(salaries), max(salaries))
print("Department wise min and max salaries:", dept_min_max)

# Task 4: Create dictionary with character frequency in a string
string = input("Enter a string: ")
freq_dict = {}
for char in string:
    freq_dict[char] = freq_dict.get(char, 0) + 1
print("Character frequency:", freq_dict)

# Task 5: Two dictionaries (items, prices) and (items, quantities), compute total bill
items_prices = {"Apple": 1.5, "Banana": 0.5}
items_quantities = {"Apple": 2, "Banana": 3}
total_bill = sum(items_prices[item] * items_quantities.get(item, 0) for item in set(items_prices) & set(items_quantities))
print("Total bill:", total_bill)
