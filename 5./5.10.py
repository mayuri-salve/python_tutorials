#Problem 10: Implement a function izip that works like itertools.izip.
def izip(list1,list2):
   i=0
   while i<len(list1):
      yield list1[i],list2[i]	
      i=i+1
for i,j in izip(['a','b','c','d'],[1,2,3,4]):
   print i,j

'''
output:
a 1
b 2
c 3
d 4
'''

