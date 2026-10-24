a = float (input("Enter the first number: "))
op = input("Operator (+, -, *, /): ")
b = float (input("Enter the second number: "))
if op == "+":
    result = a + b
elif op == "-":
    result = a - b
elif op == "*":
    result = a * b
elif op == "/":
    result = a / b
print(f"{a} {op} {b} = {result}")