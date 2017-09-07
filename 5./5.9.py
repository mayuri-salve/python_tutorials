import itertools
def my_enum(list):
  return (itertools.izip(range(len(list)),list))
print list(my_enum(['a','b','c','d']))
for x,y in my_enum(['a','b','c','d']):
   print x,y

'''
output:
[(0, 'a'), (1, 'b'), (2, 'c'), (3, 'd')]
0 a
1 b
2 c
3 d
'''

