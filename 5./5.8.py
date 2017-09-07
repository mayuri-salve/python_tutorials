# problem 8:Program to implement a function peep, that takes an iterator as argument and returns the first element and an equivalant iterator.

def peep(it):
   t=list(it)
   p=t[0]
   return p,t
it = iter(range(5))
x,t=peep(it)
print x,list(t)

#output:0 [0, 1, 2, 3, 4]



