#Problem 2: Write a program extcount.py to count number of files for each extension in the given directory. The program should take a directory name as argument and print count and extension for each available file extension.

import os 
import glob
import collections

dirpath = r"/home/audetemi/python/python_tutorials/2."
os.chdir(dirpath)
cnt = collections.Counter()
for filename in glob.glob("*"):
    name, ext = os.path.splitext(filename)
    cnt[ext] += 1
print(cnt)

#output:Counter({'.py': 31, '.txt': 3, '.csv': 1})

