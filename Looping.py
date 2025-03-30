num = int(input("Enter a number: "))

# Print even numbers 
print("Even numbers from 1 to", num, ":")
for i in range(1, num + 1):
    if i % 2 == 0:
        print(i, end=" ")

print()  

# Calculate sum of odd numbers
i = 1
sum_odd = 0
while i <= num:
    if i % 2 != 0:
        sum_odd += i
    i += 1

print("Sum of odd numbers from 1 to", num, "is:", sum_odd)