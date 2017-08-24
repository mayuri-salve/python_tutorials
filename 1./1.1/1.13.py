#Problem 13: Write a function istrcmp to compare two strings, ignoring the case.

def istrcmp(a,b):
 if a.upper()==b.upper():
  return True
 else:
  return False

print istrcmp('python','Python')
print istrcmp('LaTeX', 'Latex')
print istrcmp('a', 'b')

'''output:True
          True
          False
'''