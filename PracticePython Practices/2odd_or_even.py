'''
Ask the user for a number. Depending on whether the number is even or 
odd, print out an appropriate message to the user. Hint: how does an 
even / odd number react differently when divided by 2?

Extras:

1. If the number is a multiple of 4, print out a different message.
2. Ask the user for two numbers: one number to check (call it num) and
one number to divide by (check). If check divides evenly into num,
tell that to the user. If not, print a different appropriate message.
'''

number = int(input("Give me a number: "))
if number%2 == 0:
    print("The number is even!")
elif number%4 == 0:
    print("The number is even and is also a multiple of four. Great!")
else:
    print("The number is odd...")
    
x, y = [int(x) for x in input("Now, give me two numbers... ").split()]
if x/y == number:
    print(f"Wow, when I divided the numbers you gave me, it resulted into the number you first gave me, which was {number}!")
else:
    print("Oof! Looks like these numbers are an \"odd\" pair.")
    