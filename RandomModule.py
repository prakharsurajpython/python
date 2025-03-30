import random

#1
print(random.randint(1,100))

#2
colors=['Red','yellow','green','pink']
print(random.choice(colors))

#3
otp=random.randint(1000,9999)
print("otp",otp)

#4
names=['alice','mika','bob']
random.shuffle(names)
print(names)

