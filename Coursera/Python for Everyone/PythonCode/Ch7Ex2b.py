'''Ch7Ex2: Write a program to prompt for a file name, and then read through the file 
and look for lines of the form: X-DSPAM-Confidence:0.8475

When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart the line to extract 
the floating-point number on the line. Count these lines and then compute the total of the spam confidence values
from these lines. When you reach the end of the file, print out the average spam confidence.
'''

keyterm = 'X-DSPAM-Confidence:'
name = input("Please enter the name of the text file to be read: ")
try:
    fhand = open(name)
except:
    quit ('The file, '+name+', cannot be located. Please confirm name and location.')

name = input("Please enter the name of the text file to collect the numbers: ")
try:
    fhandwrite = open(name,'w')
except:
    quit ('The file, '+name+', cannot be located. Please confirm name and location.')

count = 0
total = 0
for line in fhand:
    if not keyterm in line: continue
    else:
        beg = line.index(keyterm)+len(keyterm)+1 
        #end = How would you be able to grab only the desired piece so that the code could be versatile for any key term?
        num = float(line[beg:])
        count = count +1
        total = total + num
        numwrite = str(num)+', '
        fhandwrite.write(numwrite)
if count!=0:
    avg = total/float(count)
else:
    print('Key term not contained within file.')
    quit()
StatA = '\r\rQuantity: '+str(count)
StatB = '\r\rAverage:'+str(avg)

fhandwrite.write(StatA)
fhandwrite.write(StatB)