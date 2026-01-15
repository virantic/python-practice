num1 = int(input("What is the first number? "))
operator = input("Enter operator (+, -, *, /): ")
num2 = int(input("What is the second number? "))

if operator == "+":
    print(num1 + num2)
elif operator == "-":
    print(num1 - num2)
elif operator == "*":
    print(num1 * num2)
elif operator == "/":
    print(num1 / num2)
else:
    print("Invalid operator")