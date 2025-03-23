#  1. List – Sum of Elements
numbers = [10, 20, 30, 40, 50]
total = sum(numbers)
print("1. Sum of all elements:", total)

# 2. 2D List – Diagonal Elements
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("\n2. Diagonal elements:")
for i in range(3):
    print(matrix[i][i])

#  3. Tuple – Max without max()
def find_max(t):
    max_val = t[0]
    for num in t:
        if num > max_val:
            max_val = num
    return max_val

print("\n3. Maximum value in tuple:", find_max((4, 8, 1, 9, 5)))

#  4. Set – Union, Intersection, Difference
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}
print("\n4. Union:", set1 | set2)
print("4. Intersection:", set1 & set2)
print("4. Difference (set1 - set2):", set1 - set2)

#  5. Dictionary – Oldest Person
people = {"Alice": 25, "Bob": 30, "Charlie": 20, "David": 35, "Eve": 28}
oldest = ""
max_age = 0
for name, age in people.items():
    if age > max_age:
        max_age = age
        oldest = name
print("\n5. Oldest person:", oldest)

#  6. Indexing – First, Middle, Last Character
s = "Python"
first = s[0]
middle = s[len(s)//2]
last = s[-1]
print("\n6. First:", first)
print("6. Middle:", middle)
print("6. Last:", last)

#  7. Function – Factorial
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

print("\n7. Factorial of 5:", factorial(5))

#  8. Return Statement – Sum and Product
def compute(a, b):
    return a + b, a * b

s, p = compute(4, 5)
print("\n8. Sum:", s, "Product:", p)

# 9. Keyword Arguments – greet()
def greet(name, msg="Welcome!"):
    print(f"{msg} {name}")

print("\n9. Greeting examples:")
greet("Alice") 
greet(name="Bob", msg="Hello")  

#  10. Nested Function – Square
def outer(n):
    def inner(x):
        return x * x
    print("\n10. Square is:", inner(n))

outer(6)

# 11. Local Variable – Scope Demo
def my_func():
    x = 10
    print("\n11. Inside function:", x)

my_func()
# print(x)  # Uncommenting this will cause an error

#  12. Global Variable – Modify with global
count = 0
def update():
    global count
    count += 1
    print("12. Inside function, count:", count)

update()
print("12. Outside function, count:", count)

#  13. *args – Largest Number
def largest(*args):
    max_val = args[0]
    for num in args:
        if num > max_val:
            max_val = num
    return max_val

print("\n13. Largest number:", largest(4, 9, 1, 3, 7))

#  14. **kwargs – Student Details
def student_details(**kwargs):
    print("\n14. Student Details:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

student_details(name="John", age=21, grade="A", city="Mumbai")
