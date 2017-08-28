#Problem 24: Provide an implementation for zip function using list comprehensions.


def my_zip(x,y):
	return [(x[i], y[i]) for i in range(min(len(x),len(y)))]
print my_zip([1, 2, 3], ['a', 'b', 'c'])

#output:[(1, 'a'), (2, 'b'), (3, 'c')]

