#Problem 5: Write a function to compute the total number of lines of code in all python files in the specified directory recursively.
import sys
import os
def pyfiles(dir):
  files=os.listdir(dir)
  for f in files:
    if '.py' in f:
      print f,len(open(f).readlines())
print pyfiles('/home/audetemi/python/python_tutorials/5.')

'''
output:

5.5.py 9
5.2.py 12
5.1.py 27
5.3.py 16
5.4.py 8
None


'''
