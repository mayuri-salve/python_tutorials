#Problem 15: Reimplement the unique function implemented in the earlier examples using sets.

def unique(x):
	return list(set(x))

print unique([1, 2, 3, 4 , 4 , 4 , 3, 2, 8, 9])

#output:[1, 2, 3, 4, 8, 9]

