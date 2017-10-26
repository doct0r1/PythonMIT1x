def isIn(char, aStr):
	"""
	char: a single character
	aStr: an alphabetized string

	returns: True if char is in aStr; False otherwise
	"""

	# TODO
	# check if string is empty or not
	# check if string is 1 char && char == string
	# get to the mid of string:
	#     if char == middle of the aString:
	#           return True
	#     elif char < middleChar:
	#           recursively search the right half of aString
	#     else:
	#           recursively search the left half of aString

	if aStr == '':
		return False

	if len(aStr) == 1:
		return aStr == char

	midIndex = len(aStr)//2
	midChar = aStr[midIndex]
	if char == midChar:
		return True
	elif char < midChar:
		return isIn(char, aStr[:midIndex])
	else:
		return isIn(char, aStr[midIndex + 1:])

print(isIn('b', 'abbgkmoppqrttuyy'))
