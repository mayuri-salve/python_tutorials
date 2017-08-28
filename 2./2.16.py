#Problem 16: Write a function extsort to sort a list of files based on extension.


def extsort(a):
	return sorted(a, key = lambda x: x.split('.')[1])
print extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
