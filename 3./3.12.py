#problem 12:Write a program mydoc.py to implement the functionality of pydoc. 

import sys
__import__(sys.argv[1])
print 'Help on module ',sys.argv[1],':'
print '\n\nDESCRIPTION\n\n'
print sys.argv[1].__doc__
print '\n\nFUNCTIONS\n\n'
for i in dir(sys.argv[1]):
  print i,'()'


'''
output:
Help on module  os :


DESCRIPTION


str(object='') -> string

Return a nice string representation of the object.
If the argument is a string, the return value is the same object.


FUNCTIONS


__add__ ()
__class__ ()
__contains__ ()
__delattr__ ()
__doc__ ()
__eq__ ()
__format__ ()
__ge__ ()
__getattribute__ ()
__getitem__ ()
__getnewargs__ ()
__getslice__ ()
__gt__ ()
__hash__ ()
__init__ ()
__le__ ()
__len__ ()
__lt__ ()
__mod__ ()
__mul__ ()
__ne__ ()
__new__ ()
__reduce__ ()
__reduce_ex__ ()
__repr__ ()
__rmod__ ()
__rmul__ ()
__setattr__ ()
__sizeof__ ()
__str__ ()
__subclasshook__ ()
_formatter_field_name_split ()
_formatter_parser ()
capitalize ()
center ()
count ()
decode ()
encode ()
endswith ()
expandtabs ()
find ()
format ()
index ()
isalnum ()
isalpha ()
isdigit ()
islower ()
isspace ()
istitle ()
isupper ()
join ()
ljust ()
lower ()
lstrip ()
partition ()
replace ()
rfind ()
rindex ()
rjust ()
rpartition ()
rsplit ()
rstrip ()
split ()
splitlines ()
startswith ()
strip ()
swapcase ()
title ()
translate ()
upper ()
zfill ()
'''

