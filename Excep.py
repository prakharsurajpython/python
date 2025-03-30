#1
try:
    num=int(input('Enter a number'))
    print("you entered",num)
except ValueError:
    print("Invalid input")

#2
try:
    a=int(input('Enter a number'))
    b=int(input('Enter second number'))
    res=a/b
    print(res)

except ZeroDivisionError:
    print("Cannot divide by zero")

#3
try:
    f=input("Enter filenmae")
    file=open(f)
    print(file.read())

except FileNotFoundError:
    print('file not found')