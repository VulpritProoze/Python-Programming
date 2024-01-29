'''
Exercise 6

Ask the user for a string and print out whether this string is a 
palindrome or not. (A palindrome is a string that reads the same 
forwards and backwards.)
'''

text = input("Give me a line of texts: ")

palindrome = []

for i in range( len(text)-1, -1, -1):    #   Iterate loops in reverse
    palindrome.append(text[i])

palindrome = "".join(palindrome)    #   Convert to string, remove all the "[]", and "," of lists

print("Text is palindrome!") if text == palindrome else print("Nah")
    
    
'''
A sample solution using string reversal


wrd=input("Please enter a word")
wrd=str(wrd)
rvs=wrd[::-1]
print(rvs)
if wrd == rvs:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
    
    
A sample solution using for loops


def reverse(word):
	x = ''
	for i in range(len(word)):
		x += word[len(word)-1-i]
	return x

word = input('give me a word:\n')
x = reverse(word)
if x == word:
	print('This is a Palindrome')
else:
	print('This is NOT a Palindrome')
'''
