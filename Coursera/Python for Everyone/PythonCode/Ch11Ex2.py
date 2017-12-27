'''Ch11Ex2: Write a program to look for lines of the form: `New Revision: 39772` and extract the number from each of the lines 
using a regular expression and the findall() method. Compute the average of the numbers and print out the average. 
Enter file:mbox.txt
38549.7949721
Enter file:mbox-short.txt
39756.9259259
'''

import re

name = input('Enter the name of a text file: ')

counter = 0
total = 0

hand = open(name)
for line in hand:
    line = line.rstrip()
    x = re.findall('^New Revision: ([\d]+)', line) 
    if len(x) > 0:
        total = total + float(x[0])
        counter += 1

average = total/counter
print(average)