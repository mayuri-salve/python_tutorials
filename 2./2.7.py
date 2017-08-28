#Problem 7: Python has built-in functions min and max to compute minimum and maximum of a given list. Provide an implementation for these functions. What happens when you call your min and max functions with a list of strings?



x=raw_input('enter 1st list : ')
y=raw_input('enter 2nd list : ')

print 'min string:'+','+min(x,y)
print 'max string;'+','+max(x,y)

'''output:enter 1st list : 1,2,3,4
          enter 2nd list : 5,6,7,8
          min string:,1,2,3,4
          max string;,5,6,7,8'''

