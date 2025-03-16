# Assignment-1

# 1. Checking if a number is even or odd
def check_even_odd(n):
    if n % 2 == 0:
        print(f"{n} is Even")
    else:
        print(f"{n} is Odd")

# 2. Finding the largest of three numbers
def largest_of_three(a, b, c):
    return max(a, b, c)

# 3. Checking for prime numbers
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

# 4. Displaying a multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# 5. Counting vowels in a string
def count_vowels(s):
    vowels = "aeiouAEIOU"
    return sum(1 for char in s if char in vowels)

# 6. Sum of digits of a number
def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# 7. Calculating factorial of a number
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i  
    return fact

# 8. Fibonacci Sequence (Optimized)
def fibonacci(n):
    a, b = 0, 1
    fib_sequence = []
    for _ in range(n):
        fib_sequence.append(a)
        a, b = b, a + b
    return fib_sequence

# 9. Palindrome Check
def is_palindrome(s):
    return s == s[::-1]

# 10. Checking for Armstrong Numbers
def is_armstrong(n):
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d**power for d in digits) == n

# Menu for user input
while True:
    print("\nChoose a program to run:")
    print("1. Check Even or Odd")
    print("2. Find Largest of Three Numbers")
    print("3. Check Prime Number")
    print("4. Display Multiplication Table")
    print("5. Count Vowels in a String")
    print("6. Sum of Digits of a Number")
    print("7. Calculate Factorial")
    print("8. Fibonacci Sequence")
    print("9. Palindrome Check")
    print("10. Check Armstrong Number")
    print("0. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 0:
        print("Exiting the program.")
        break
    elif choice == 1:
        num = int(input("Enter a number: "))
        check_even_odd(num)
    elif choice == 2:
        a, b, c = map(int, input("Enter three numbers: ").split())
        print(f"Largest number: {largest_of_three(a, b, c)}")
    elif choice == 3:
        num = int(input("Enter a number: "))
        print(f"{num} is Prime" if is_prime(num) else f"{num} is Not Prime")
    elif choice == 4:
        num = int(input("Enter a number: "))
        multiplication_table(num)
    elif choice == 5:
        s = input("Enter a string: ")
        print(f"Number of vowels: {count_vowels(s)}")
    elif choice == 6:
        num = int(input("Enter a number: "))
        print(f"Sum of digits: {sum_of_digits(num)}")
    elif choice == 7:
        num = int(input("Enter a number: "))
        print(f"Factorial: {factorial(num)}")
    elif choice == 8:
        num = int(input("Enter number of terms: "))
        print("Fibonacci Sequence:", fibonacci(num))  # Optimized: Prints only one sequence
    elif choice == 9:
        s = input("Enter a string: ")
        print(f"{s} is a Palindrome" if is_palindrome(s) else f"{s} is Not a Palindrome")
    elif choice == 10:
        num = int(input("Enter a number: "))
        print(f"{num} is an Armstrong number" if is_armstrong(num) else f"{num} is Not an Armstrong number")
    else:
        print("Invalid choice! Please select a valid option.")
