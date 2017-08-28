#Problem 6: What will be the output of the following program.

a, b = 2, 3
c, b = a, c + 1
print a, b, c

'''error:Traceback (most recent call last):
  File "1.6.py", line 4, in <module>
    c, b = a, c + 1
NameError: name 'c' is not defined'''

