#Problem 3: What happens when the above sum function is called with a list of strings? Can you make your sum function work for a list of strings as well.


def sums(x):
   sum = x[0]
   for i in x:
     if i == x[0]:
       continue
     else:
       sum += i
   return sum
print sums(['Hello', 'World!'])

#output:HelloWorld!


