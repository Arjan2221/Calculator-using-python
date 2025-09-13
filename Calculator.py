print("Welcome to the Calculator!")
print("This program performs basic arithmetic operations.")
name = input("Please enter your name: ")
print("Hello, " + name + "! Let's do some calculations.")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
operator = input("Enter an operator (+, -, *, /, %, **): ")
if operator == '+':
    result = a + b
    print(f"{a} + {b} = {result}")

elif operator == '-':
    result = a - b
    print(f"{a} - {b} = {result}")

elif operator == '*':
    result = a * b
    print(f"{a} * {b} = {result}")  

elif operator == '/':
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '%':
    if b != 0:
        result = a % b
        print(f"{a} % {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
elif operator == '**':
    result = a ** b
    print(f"{a} ** {b} = {result}")
else:
    print("Error: Invalid operator.")
    
print("Thank you for using the calculator, " + name + "! Goodbye!")
# This is a simple calculator program that performs basic arithmetic operations.

