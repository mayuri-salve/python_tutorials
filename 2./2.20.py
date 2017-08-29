#Problem 20: Implement unix command grep. The grep command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

def grep(filename,word):
   for f in open(filename):
      if word in f:
        print f

grep("foo.txt","So if")


'''
output:
So if she sells seashells on the seashore,

So if she sells seashells on the seashore,

'''
