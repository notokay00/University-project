import random

# Task 1: Create list of 5 odd integers and 4 even integers, replace third odd with even list, flatten, sort
odd_list = [random.randrange(1, 100, 2) for _ in range(5)]
even_list = [random.randrange(0, 100, 2) for _ in range(4)]
print("Odd list:", odd_list)
print("Even list:", even_list)
odd_list[2] = even_list  # Replace third element
flattened = []
for item in odd_list:
    if isinstance(item, list):
        flattened.extend(item)
    else:
        flattened.append(item)
flattened.sort()
print("Flattened and sorted list:", flattened)

# Task 2: Generate 20 random integers, find positions of user input number
numbers = [random.randint(1, 50) for _ in range(20)]
print("Random list:", numbers)
num_to_find = int(input("Enter a number to find its positions: "))
positions = [i for i in range(len(numbers)) if numbers[i] == num_to_find]
print(f"Positions of {num_to_find}: {positions}")

# Task 3: Generate 30 random numbers, create two lists (positive and negative)
all_numbers = [random.randint(-50, 50) for _ in range(30)]
positive = [x for x in all_numbers if x > 0]
negative = [x for x in all_numbers if x < 0]
print("All numbers:", all_numbers)
print("Positive numbers:", positive)
print("Negative numbers:", negative)

# Task 4: List of 5 strings, convert to uppercase
strings = ["apple", "banana", "cherry", "date", "elderberry"]
upper_strings = [s.upper() for s in strings]
print("Original strings:", strings)
print("Uppercase strings:", upper_strings)

# Task 5: Convert Fahrenheit to Celsius
fahrenheit = [32, 50, 68, 86, 104]
celsius = [(f - 32) * 5/9 for f in fahrenheit]
print("Fahrenheit:", fahrenheit)
print("Celsius:", celsius)

# Task 6: Stack implementation with menu
stack = []
while True:
    print("\nStack Menu: 1.Push 2.Pop 3.Display 4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        item = input("Enter item to push: ")
        stack.append(item)
    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break

# Task 7: Queue implementation with menu
queue = []
while True:
    print("\nQueue Menu: 1.Enqueue 2.Dequeue 3.Display 4.Exit")
    choice = int(input("Enter choice: "))
    if choice == 1:
        item = input("Enter item to enqueue: ")
        queue.append(item)
    elif choice == 2:
        if queue:
            print("Dequeued:", queue.pop(0))
        else:
            print("Queue is empty")
    elif choice == 3:
        print("Queue:", queue)
    elif choice == 4:
        break

# Task 8: Take two lists, create third with numbers from first not in second
list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8]
list3 = [x for x in list1 if x not in list2]
print("List 1:", list1)
print("List 2:", list2)
print("List 3:", list3)
