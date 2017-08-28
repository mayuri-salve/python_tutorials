#Problem 10: What will be the output of the following program?

x = 1
def f():
        y = x
        x = 2
        return x + y
print x
print f()
print x

'''error:1
Traceback (most recent call last):
  File "1.10.py", line 9, in <module>
    print f()
  File "1.10.py", line 5, in f
    y = x
UnboundLocalError: local variable 'x' referenced before assignment
'''
