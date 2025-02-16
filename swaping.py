# Input two numbers
a = float(input("Enter first number (a): "))
b = float(input("Enter second number (b): "))

print(f"Before swapping: a = {a}, b = {b}")

# Swapping without a third variable
if a != b:
    a = a + b
    b = a - b
    a = a - b
elif a == b:
    print("Both numbers are the same, swapping has no effect.")
else:
    print("Unexpected condition.")  # This case won't usually occur

print(f"After swapping: a = {a}, b = {b}")
