import random

operators = ['+', '-', '*', '/']
op = random.choice(operators)

a, b = 10, 5
if op == '+': result = a + b
elif op == '-': result = a - b
elif op == '*': result = a * b
elif op == '/': result = a / b

print(f"{a} {op} {b} = {result}")
