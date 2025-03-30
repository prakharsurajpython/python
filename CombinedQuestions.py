import random
import string

#1
try:
    number = random.randint(1, 10)
    guess = int(input("Guess the number (1–10): "))
    if guess == number:
        print("Congratulations! You guessed it!".format())
    else:
        print("Wrong! The number was {}".format(number))
except ValueError:
    print("Please enter a valid number.")

#2
try:
    length=int(input("Password Length:"))
    chars = string.ascii_letters + string.digits
    password = ''.join(random.choice(chars) for _ in range(length))
    print("Generated password: {}".format(password))
except ValueError:
    print("Invalid input.")
