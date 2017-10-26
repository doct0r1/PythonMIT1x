"""
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh
"""

# s = "azcbobobegghakl" # uncomment out this line to work on your PC
count = 0
word = 0
longWord = 0

# TODO (pseudoCode)
# iterate over the chars in the word:
#   if the char <= char[+ in the index]:
#      count++
#       if count > longword:
#           longWord = count
#           word = char + 1
#   else:
#       count = 0
# startPosition = word - longWord

## print Longest substring in the alphabetical order

for char in range(len(s) - 1):
	if s[char] <= s[char + 1]:
		count += 1
		if count > longWord:
			longWord = count
			word = char + 1
	else:
		count = 0

startOfWord = word - longWord
print(s[startOfWord:word + 1])
