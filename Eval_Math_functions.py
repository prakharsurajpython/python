import math
expression = input("Enter a mathematical expression: ")
try:
    result = eval(expression)
    print("Result:", result)
    print("Square Root:", math.sqrt(result))
except Exception as e:
    print("Invalid expression:", e)