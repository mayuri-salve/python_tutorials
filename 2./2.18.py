#Problem 18: Write a program to print each line of a file in reverse order.

def line_reverse(filename):
	f = open(filename)
	lines = f.readlines()
	for x in lines:
		print x[::-1]

line_reverse("cat.txt")



''' cat.txt
She sells seashells on the seashore;
The shells that she sells are seashells I'm sure.
So if she sells seashells on the seashore,
I'm sure that the shells are seashore shells.'''

'''output:

;erohsaes eht no sllehsaes slles ehS

.erus m'I sllehsaes era slles ehs taht sllehs ehT

,erohsaes eht no sllehsaes slles ehs fi oS

.sllehs erohsaes era sllehs eht taht erus m'I'''

