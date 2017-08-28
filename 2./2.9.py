#Problem 9: Write a function cumulative_product to compute cumulative product of a list of numbers.

num = [1,2,3,4]

sums = []

def cumulative_product(num):
    sums.append(num[0])
    for i in range(len(num) - 1):
       if i == 0:
            sums.append(num[i] * num[i + 1])
       else:
            sums.append(num[i + 1] * sums[i])
    return sums

print cumulative_product(num)

#output:[1,2,6,24]
