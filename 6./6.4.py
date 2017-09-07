#Problem 4: Write a function treemap to map a function over nested list.



def treemap(fun,l):
   for i in range(len(l)):
      if isinstance(l[i],list):
         treemap(fun,l[i])
      else:
	 sqr=fun(l[i])
	 l.remove(l[i])
	 l.insert(i,sqr)
   return l

print treemap(lambda x: x*x, [1, 2, [3, 4, [5]]])


#output:[1, 4, [9, 16, [25]]]

