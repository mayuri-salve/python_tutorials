#Problem 5: Write a function tree_reverse to reverse elements of a nested-list recursively.


def tree_reverse(l):
   l.reverse()
   for i in l:
      if isinstance(i,list):
         tree_reverse(i)			
   return l
print tree_reverse([[1, 2], [3, [4, 5]], 6])

#output:[6, [[5, 4], 3], [2, 1]]

