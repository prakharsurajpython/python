def calculate(*args, **kwargs):
    operation = kwargs.get("operation")
    result = 0 if operation == "sum" else 1
    if operation == "sum":
        for num in args:
            result += num
    elif operation == "product":
        for num in args:
            result *= num
    else:
        return "Invalid operation"
    return result

print("Sum:", calculate(1, 2, 3, 4, operation="sum"))
print("Product:", calculate(2, 3, 4, operation="product"))