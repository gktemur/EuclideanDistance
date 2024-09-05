# Simple Calculator Program

# Addition function
def addition (x, y):
  return x + y

# Subtracktion function
def subtracktion(x, y):
  return x - y

# Multiplication function
def multiplication( x, y):
  return x * y

# Division function
def division(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
# User input
print("Welcome to the Calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Choose operation number (1/2/3/4): ")

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Functions for operations
def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Error! Division by zero."

# Show the result based on user's choice
if choice == '1':
    print(f"{num1} + {num2} = {addition(num1, num2)}")

elif choice == '2':
    print(f"{num1} - {num2} = {subtraction(num1, num2)}")

elif choice == '3':
    print(f"{num1} * {num2} = {multiplication(num1, num2)}")

elif choice == '4':
    print(f"{num1} / {num2} = {division(num1, num2)}")

else:
    print("Invalid choice!")