#Problem 8: Cumulative sum of a list [a, b, c, ...] is defined as [a, a+b, a+b+c, ...]. Write a function cumulative_sum to compute cumulative sum of a list. Does your implementation work for a list of strings?

num = [1,2,3,4]

sums = []

def cumulative_Sum(num):
    sums.append(num[0])
    for i in range(len(num) - 1):
        if i == 0:
            sums.append(num[i] + num[i + 1])
        else:
            sums.append(num[i + 1] + sums[i])
    return sums

print cumulative_Sum(num)

#ouput:[1, 3, 6, 10]



