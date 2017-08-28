#Problem 10: Write a function unique to find all the unique elements of a list.


def unique(list):
 list_unique=set(list)
 print (list_unique)

unique([1,2,1,2,2,3,3,2,4,6])

#output:set([1, 2, 3, 4, 6])

