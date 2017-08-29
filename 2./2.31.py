#Problem 31: Generalize the above implementation of csv parser to support any delimiter and comments.

def parser_generalized(filename, delimiter, comments):
	return [line.split()[0].split(delimiter) for line in open(filename) if line[0] <> comments]

print parser_generalized('a.txt', '!', '#')

#outpur:[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]

''' a.txt
a!b!c
1!2!3
2!3!4
3!4!5
'''



