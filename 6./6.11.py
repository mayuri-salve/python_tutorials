#Problem 11: Write a function vectorize which takes a function f and return a new function, which takes a list as argument and calls f for every element and returns the result as a list.



def square(x):
   return x * x

def vectorize(square):
   def g(l):
      a=[]
      for i in l:
         v=square(i)
         a.append(v)
      return a
   return g

s=vectorize(len)
print s([[1,2],[3,4,5]])


#output:[2,3]

