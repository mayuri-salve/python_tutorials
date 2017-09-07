#Problem 17: Write a program reverse.py to print lines of a file in reverse order


for line in reversed(open("cat.txt").readlines()):
    print line.rstrip() 

'''cat.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.
'''

'''
output:
I'm sure that the shells are seashore shells.
So if she sells seashells on the seashore,
The shells that she sells are seashells I'm sure.
She sells seashells on the seashore;

'''

