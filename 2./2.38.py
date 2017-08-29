#Problem 38: Write a function invertdict to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

def invertdict(dictionary):
	a = {}
	for x in dictionary:
		a.update({dictionary[x]:x})
	print a

invertdict({'x':1, 'y':2, 'z':3})

#output:{1: 'x', 2: 'y', 3: 'z'}

