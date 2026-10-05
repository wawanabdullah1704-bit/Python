def calculate(operator, num1, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Division by zero"
        return num1 / num2
    else: 
        return "Error: Invalid operator"

operator = input("Enter operator (+, -, *, or /): ")
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

result = calculate(operator, num1, num2)
print("Result:", result)