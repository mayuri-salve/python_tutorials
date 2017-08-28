#Problem 5: Write a function factorial to compute factorial of a number. Can you use the product function defined in the previous example to compute factorial?

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

x=factorial(4)
print(x)

#output:24
