import random

while True:
    number = int(input("choose the amount of characters that you want for your password: "))
    if 0 < number <= 25:
        break
    else:
        print("The amount of characters needs to be less than 25 and greater than 0")

password = ''
for i in range(number):
    password += random.choice('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')

print("Your password:", password)