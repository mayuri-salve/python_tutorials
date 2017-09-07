#Problem 9: Write a function permute to compute all possible permutations of elements of a given list.


def permute(word):
  r_list=[]
  if len(word) == 1:
    r_list.append(word)
  else:
    for pos in range(len(word)):
      permutelist=permute(word[0:pos]+word[pos+1:len(word)])
      for item in permutelist:
        r_list.append(word[pos]+item)
  return list(set(r_list)) 
print permute('hello')
print permute('who')

#output:['hwo', 'owh', 'who', 'how', 'woh', 'ohw']


'''
output:
['llhoe', 'lehol', 'lleoh', 'lhelo', 'lohel', 'olehl', 'elhol', 'lolhe', 'eollh', 'olelh', 'lelho', 'ollhe', 'llheo', 'hlelo', 'oehll', 'heoll', 'elohl', 'leolh', 'leloh', 'elloh', 'ohell', 'eholl', 'lhleo', 'helol', 'elolh', 'hlole', 'hlloe', 'ehllo', 'loleh', 'hleol', 'lehlo', 'elhlo', 'olleh', 'lhoel', 'hoell', 'lloeh', 'hlleo', 'lleho', 'lheol', 'ohlle', 'oellh', 'leohl', 'holle', 'olhle', 'lohle', 'ohlel', 'ehlol', 'llohe', 'lhole', 'eolhl', 'hloel', 'loelh', 'holel', 'lhloe', 'loehl', 'olhel', 'ellho', 'hello', 'oelhl', 'eohll']
'''


