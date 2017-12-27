'''Ch11Ex1: Write a simple program to simulate the operation of the grep com- mand on Unix. 
Ask the user to enter a regular expression and count the number of lines that matched the regular expression:

Enter a regular expression: ^Author
mbox.txt had 1798 lines that matched ^Author

Enter a regular expression: ^X-
mbox.txt had 14368 lines that matched ^X-

Enter a regular expression: java$
mbox.txt had 4218 lines that matched java$
'''

import re

name = input('Enter the name of a text file: ')
inp = input('Enter a regular expression: ')

counter = 0

hand = open(name)
for line in hand:
    line = line.rstrip()
    if re.search(inp, line):
        counter += 1

print('%s had %d lines that matched %s'%(name,counter,inp))
