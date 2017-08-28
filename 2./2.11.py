#Problem 11: Write a function dups to find all duplicates in the list.


a = [10,20,30,20,10,50,60,40,80,50,40]
dupes = [x for n, x in enumerate(a) if x in a[:n]]
print dupes

#output:[20, 10, 50, 40]



