#Problem 25: Python provides a built-in function map that applies a function to each element of a list. Provide an implementation for map using list comprehensions

def square(x):
	return x * x

def map(function, lists):
	return [function(i) for i in lists]

print map(square, range(5))


#output:[0, 1, 4, 9, 16]

