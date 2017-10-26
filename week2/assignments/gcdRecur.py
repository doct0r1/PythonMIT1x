def gcdRecur(a, b):
	"""
	a, b: positive integers

	returns: a positive integer, the greatest common divisor of a & b.
	"""

	# TODO
	# make a base case maybe when a == 0 || b == 0
	# and recursive case when the number1 % number2 == 0
	#       return number2

	if b == 0:
		return b

	return gcdRecur(b, b % a)

