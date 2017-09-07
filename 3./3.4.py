#Problem 4: Write a program to print directory tree. The program should take path of a directory as argument and print all the files in it recursively as a tree.

import os

def list_files(startpath):
    for root, dirs, files in os.walk(startpath):
        level = root.replace(startpath, '').count(os.sep)
        indent = ' ' * 4 * (level)
        print('{}{}/'.format(indent, os.path.basename(root)))
        subindent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(subindent, f))
list_files('/home/audetemi/python/python_tutorials')


