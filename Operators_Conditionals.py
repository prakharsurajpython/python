try:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("Addition: {:.2f}".format(num1 + num2))
    print("Subtraction: {:.2f}".format(num1 - num2))
    print("Multiplication: {:.2f}".format(num1 * num2))
    print("Division: {:.2f}".format(num1 / num2))
    print("Modulus: {:.2f}".format(num1 % num2))
    print("Floor Division: {:.2f}".format(num1 // num2))
    print("Exponentiation: {:.2f}".format(num1 ** num2))
except ZeroDivisionError:
    print("Division by zero is not allowed.")
