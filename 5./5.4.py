#Problem 4: Write a function to compute the number of python files (.py extension) in a specified directory recursively.

import sys
import os
def pyfiles(dir):
  files=os.listdir(dir)
  for f in files:
    if '.py' in f:
      print f,

print pyfiles('/home/audetemi/python/python_tutorials/5.')

#output:5.5.py 5.2.py 5.1.py 5.3.py 5.4.py None

