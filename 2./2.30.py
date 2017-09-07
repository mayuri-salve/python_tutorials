#Problem 30: Write a python function parse_csv to parse csv (comma separated values) files.
def parse_csv(file):
	return [line.split()[0].split(',') for line in open(file)]

print parse_csv('a.csv')

#output:[['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
