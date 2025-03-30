import random
target = random.randint(1, 100)

while True:
    try:
        guess = int(input("Guess the number (1-100): "))
        if guess < target:
            print("Too low! Try again.")
        elif guess > target:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed it right.")
            break
    except ValueError:
        print("Invalid input. Please enter a number.")