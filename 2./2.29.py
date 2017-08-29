#Problem 29: Write a function array to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

def array(b,c):
	return [[None for x in range(c)] for x in range(b)]
	
a = array(2, 3)
print 'None initialized array'
print a
a[0][0] = 5
print 'Modified array'

'''
output:
None initialized array
[[None, None, None], [None, None, None]]
Modified array
[[5, None, None], [None, None, None]]

'''
print a


