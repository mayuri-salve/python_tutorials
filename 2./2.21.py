#Problem 21: Write a program wrap.py that takes filename and width as aruguments and wraps the lines longer than width.

def wrap(files, width):
 for x in open(files).readlines():
   if len(x) < width:
	print x
   else:
	print x[:width]
	print x[width:]

wrap("foo.txt",15)

"""
output:
hi

She sells seash
ells on the seashore;

The shells that
 she sells are seashells I'm sure.

So if she sells
 seashells on the seashore,

I'm sure that t
he shells are seashore shells.

hello

I'm sure that t
he shells are seashore shells.

So if she sells
 seashells on the seashore,

The shells that
 she sells are seashells I'm sure.

She sells seash
ells on the seashore;


"""
			
