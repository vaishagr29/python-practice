# Get user input
num1 = float(input("Enter first number: "))
operator = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

# Perform operation using match-case
match operator:
    case "+":
        result = num1 + num2
        print(f"Result: {num1} + {num2} = {result}")
    case "-":
        result = num1 - num2
        print(f"Result: {num1} - {num2} = {result}")
    case "*":
        result = num1 * num2
        print(f"Result: {num1} * {num2} = {result}")
    case "/":
        if num2 != 0:
            result = num1 / num2
            print(f"Result: {num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    case _:
        print("Invalid operator entered.")
