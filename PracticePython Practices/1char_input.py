'''
1/21/24
Character Input 
input strings types int
Exercise 1 (and Solution)
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old. Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year). If you want to do this in a generic way, see exercise 39.

Extras:

Add on to the previous program by asking the user for another number and printing out that many copies of the previous message. (Hint: order of operations exists in Python)
Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''

name = input("Enter your name: ")
age = int(input("Enter your age: "))
reiteration = int(input("Give me a number! -> "))
for i in range(reiteration):
    print(f"Hi, {name}! You will turn 100 years old {100-age} years from now.")

# print("some text ", some_var, " some text part two")
# print("some text " + some_var + " some text part two")
# print(f"some text {some_var} some text part two)

# First print statement adds a space in between arguments
# Second print statement does not
# Third print statement also does not but has way better format than the previoust two