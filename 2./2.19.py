#Problem 19: Implement unix commands head and tail. The head and tail commands take a file as argument and prints its first and last 10 lines of the file respectively.



def head_tail(filename):
	f = open(filename)
	list_of_lines = f.readlines()
	print 'head 1 lines.....'
	for x in list_of_lines[0:1]:
		print x
	print 'tail 10 lines.....'
	for x in list_of_lines[-10:-1]:
		print x

head_tail("foo.txt")

""""
output:
head 1 lines.....
hi

tail 10 lines.....
hi

She sells seashells on the seashore;

The shells that she sells are seashells I'm sure.

So if she sells seashells on the seashore,

I'm sure that the shells are seashore shells.

hello

I'm sure that the shells are seashore shells.

So if she sells seashells on the seashore,

The shells that she sells are seashells I'm sure.


"""
