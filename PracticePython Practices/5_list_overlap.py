
'''
Exercise 5

Take two lists, say for example these two:
  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
and write a program that returns a list that contains only the elements 
that are common between the lists (without duplicates). Make sure your 
program works on two lists of different sizes.

Extras:

1.  Randomly generate two lists to test this
2.  Write this in one line of Python (don’t worry if you can’t figure this 
out at this point - we’ll get to it soon)
'''
import random as rand

range_of_rand = 23  # could be anything really
list_a = [rand.randint(0, range_of_rand) for x in range(10)] # generate 10 random numbers from 0 to 22
list_b = [rand.randint(0, range_of_rand) for x in range(10)]

print(*list_a)
print(*list_b)

compared_list = []

for i in range( len(list_a)):
  for j in range( len(list_b)):
    if list_a[i] == list_b[j]:
      compared_list.append( list_a[i])

compared_list = list( set( compared_list))  # converts list into a set to remove duplicates

print(*compared_list)