'''
1/28/24
Exercise 3

Take a list, say for example this one:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
and write a program that prints out all the elements of the list that 
are less than 5.
   
Extras:

1. Instead of printing the elements one by one, make a new list that has 
all the elements less than 5 from this list in it and print out this 
new list.
2. Write this in one line of Python.
3. Ask the user for a number and return a list that contains only elements 
from the original list a that are smaller than that number given by the 
user.
'''
# list_1 = [0,1,2,3,4]
# print(*list_1)

# list_2 = [x for x in range(5)]
# print(*list_2)

list_one_line = [x for x in range(5) if print(f"{x} ", end="") or True]

inp = int(input("\nGive me a number: "))

for numbers in list_one_line:
    if inp > numbers:
        print(f"{numbers} ")
    else:
        print("Sorry, that number is lesser than the numbers in the list")
        break

