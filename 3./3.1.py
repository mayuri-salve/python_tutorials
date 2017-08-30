#Problem 1: Write a program to list all files in the given directory.

import os

a = open("output.txt", "w")
for path, subdirs, files in os.walk(r'/home/audetemi/python/python_tutorials/2.'):
   for filename in files:
     f = os.path.join(path, filename)
     a.write(str(f) + os.linesep) 
