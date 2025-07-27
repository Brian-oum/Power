a = int(input("Enter your first number:"))
b = int(input("Enter your second number:"))
operation = input("Enter an operation (+, -, *, /):")

if operation == "+":
    result = a+b
    print(f"{a}+{b} ={result}")

elif operation == "-":
    result = a-b
    print(f"{a}-{b} ={result}")

elif operation == "*":
    result = a*b
    print(f"{a}*{b} ={result}")

elif operation == "/":
    if b != 0:
        result = a / b
        print(f"{a} / {b} = {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter +, -, *, or /.")