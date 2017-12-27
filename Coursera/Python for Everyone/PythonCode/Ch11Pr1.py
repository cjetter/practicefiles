'''Ch11Pr1: In this assignment you will read through and parse a file with text and numbers. 
You will extract all the numbers in the file and compute the sum of the numbers.

Python version = 2
'''

import re

total = 0   

fhand = open('Ch11Pr1SampleText2.txt')
for line in fhand:
    line = line.rstrip()
    x = re.findall('[0-9]+', line)
    if len(x) > 0:
        for i in x:
            total = total + int(i)
       
print total