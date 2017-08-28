#Problem 13: Write a function lensort to sort a list of strings based on length.

def lensort(list):
 
  list.sort(key=lambda x:len(x))
  print(list)

lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])

#output:['c', 'perl', 'java', 'ruby', 'python', 'haskell']

