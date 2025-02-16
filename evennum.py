# Taking input from the user
n = int(input("Enter how many even numbers to display: "))

# Initializing variables
i = 1  # Counter for counting even numbers
num = 2  # First even number

# Using while loop to print even numbers
if n > 0:
    while i <= n:
        print(num, end=", " if i < n else "\n")  # Print in horizontal format
        num += 2  # Increment by 2 to get the next even number
        i += 1
elif n == 0:
    print("No even numbers to display.")
else:
    print("Please enter a positive number.")
