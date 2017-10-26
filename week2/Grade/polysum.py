import math


def polysum(n, s):
	"""
	:param n: number of sides
	:type s: the length
	"""
	area = (0.25 * n * (s ** 2)) / (math.tan(math.pi / n))
	perimeter = (n * s) ** 2
	return round(area + perimeter, 4)
