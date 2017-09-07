#Problem 27: Write a function triplets that takes a number n as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that (a, b, c) and (b, a, c) represent same triplet.


def triplets(number):
	return [(a, b, c) for a in range(1, number) for b in range(1, number) for c in range(1, number) if a + b == c]
print triplets(5)

#output:[(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 1, 3), (2, 2, 4), (3, 1, 4)]

