'''Ch9 . Ex4: Add code to the above program (ex3) to figure out who has the most messages in the file.
TargetAnswer:
Enter a file name: mbox-short.txt
cwen@iupui.edu 5
Enter a file name: mbox.txt
zqian@umich.edu 195
'''

fhand = open('mbox.txt')
d = dict()

for line in fhand:
    if line.startswith('From ') is False: continue
    else:
        words = line.split()
        val = words[1]
        d[val]=d.get(val,0)+1
lst = d.keys()
largest = None
for key in lst:
    if largest is None or d[key]>largest:
        largest = d[key]
        winner = key
print(winner,largest)
