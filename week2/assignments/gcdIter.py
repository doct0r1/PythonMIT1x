def gcdIter(a, b):
	"""
	a, b: positive integers

	returns: a positive integer, the greatest common divisor of a & b.
	"""
	# TODO
	# while from the greatest number in the smaller one decrement from there!
	#   and every -1 check the % for both
	#       if found: that's mean I got the greatest number
	#           return theNumber

	if a < b:
		z = a
	else:
		z = b
	while z > 0:
		if a % z == 0 and b % z == 0:
			return z
		else:
			z -= 1


# Test Cases
#print(gcdIter(12, 2))