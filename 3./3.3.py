#Problem 3: Write a program to list all the files in the given directory along with their length and last modification time. The output should contain one line for each file containing filename, length and modification date separated by tabs.

import os
def list(dir):
  file=os.listdir(dir)
  for item in file:
    print item,' ',len(item),' ',os.stat(os.path.abspath(os.path.join(dir,item)))[7]
list('/home/audetemi/python/python_tutorials/2.')

'''
output:
2.4.py   6   1503928270
2.18.py   7   1504010262
2.6.py   6   1503928270
2.7.py   6   1503928270
2.30.py   7   1503999478
2.8.py   6   1503928270
2.28.py   7   1503999071
2.20.py   7   1504010262
2.2.py   6   1503928270
2.10.py   7   1503928270
2.5.py   6   1503928270
2.9.py   6   1503928270
2.14.py   7   1503928270
cat.txt   7   1503991164
2.25.py   7   1503928270
2.26.py   7   1503928270
2.19.py   7   1503993912
2.31.py   7   1504010262
2.27.py   7   1504010262
foo.txt   7   1503992964
a.txt   5   1503999461
a.csv   5   1503999279
2.15.py   7   1503928270
2.29.py   7   1504010262
2.21.py   7   1503994030
2.3.py   6   1503928270
2.1.py   6   1503928270
2.24.py   7   1503928270
2.12.py   7   1503928270
2.38.py   7   1504010262
2.16.py   7   1503928270
2.37.py   7   1504010262
2.17.py   7   1504010262
2.11.py   7   1503928270
2.13.py   7   1503928270
'''
