import os
import random

# Generate random numbers as strings
random_numbers = [str(random.randint(1, 100)) for _ in range(5)]

file = open("numbers.txt", "w")
file.write("\n".join(random_numbers))
file.close()

#Read the file
file = open("numbers.txt", "r")
content = file.read()
print("File Content:\n", content)
file.close()

# Delete the file
os.remove("numbers.txt")
print("File deleted.")
