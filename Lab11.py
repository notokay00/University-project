# Task: Prompt for integer input, handle non-integer input with exception, loop until correct input
while True:
    try:
        user_input = int(input("Please enter an integer: "))
        print(f"Success! You entered the integer: {user_input}")
        break  # Exit loop if input is successfully converted to integer
    except ValueError:
        print("Error: That's not an integer. Please try again.")
