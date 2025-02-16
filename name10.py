# Taking input from the user
text = input("Enter a string: ")

# Initializing counters
letter_count = 0
digit_count = 0

# Using for loop to check each character
for char in text:
    if char.isalpha():  # Check if the character is a letter
        letter_count += 1
    elif char.isdigit():  # Check if the character is a digit
        digit_count += 1

# Printing the results
print(f"Number of letters: {letter_count}")
print(f"Number of digits: {digit_count}")
