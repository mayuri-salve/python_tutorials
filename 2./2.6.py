#Problem 6: Write a function reverse to reverse a list. Can you do this without using list slicing?

#using in-built-function
x=[1,2,3,4,5,6,7]
x.reverse()
print x

x.reverse()
print x

#output: [7, 6, 5, 4, 3, 2, 1]
#        [1, 2, 3, 4, 5, 6, 7]

#using function
list=[1,2,3,4,5]
def reverse(l):
   l.reverse()
   return l
print reverse(list)
print reverse(reverse(list))

#output:[5, 4, 3, 2, 1]
#       [5, 4, 3, 2, 1]

