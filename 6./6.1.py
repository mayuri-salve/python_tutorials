#Problem 1: Implement a function product to multiply 2 numbers recursively using + and - operators only.


def mult(a, b):
   if a == 0:
      return 0
   elif a == 1:
      return b
   else:
      return b + mult(a-1, b)
print mult(2,6)

