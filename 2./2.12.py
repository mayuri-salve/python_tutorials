#Problem 12: Write a function group(list, size) that take a list and splits into smaller lists of given size.

def group(l, size):
  return [l[i:i+size] for i in range(0, len(l), size)]

print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
print group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)

#output: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#        [[1, 2, 3, 4], [5, 6, 7, 8], [9]]


