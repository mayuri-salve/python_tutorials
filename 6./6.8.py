
def count_change(amount,coins):
 if amount == 0:
    return 1
 elif amount < 0 or not coins:
    return 0
 else:
    return count_change(amount, coins[1:]) + count_change(amount-coins[0], coins)

if __name__ == "__main__":
    import doctest
    doctest.testmod()

print count_change(10, [1, 5])
print count_change(10, [1, 2])
print count_change(100, [1, 5, 10, 25, 50])

'''
output:
3
6
292
'''

