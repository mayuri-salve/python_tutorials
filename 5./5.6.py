#Problem 6: Write a function to compute the total number of lines of code, ignoring empty and comment lines, in all python files in the specified directory recursively.



import sys
import os
def pyfile(files):
  for file in files:
    if '.py' in file:
      yield file

def countlines(pyfiles):
  for file in pyfiles:
    count=0
    for line in open(file).readlines():
      if line[0]!='#' and line!='\n':
        count=count+1
    print file,count	

def main(dir):		
  files=os.listdir(dir)
  pyfiles=pyfile(files)
  countlines(pyfiles)

main('/home/audetemi/python/python_tutorials/5.')

'''
output:
5.5.py 17
5.2.py 11
5.1.py 22
5.3.py 16
5.4.py 8
5.6.py 18
'''
