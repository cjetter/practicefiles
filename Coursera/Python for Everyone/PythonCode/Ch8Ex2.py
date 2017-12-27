'''Ch8Ex2: Figure out which line of the below program is still not properly guarded. 
See if you can construct a text file which causes the program to fail and then modify the program 
so that the line is properly guarded and test it to make sure it handles your new text file.

text file = Ch8Ex2TextFile.txt
'''

fhand = open('Ch8Ex2TextFile.txt')
count = 0
#print(fhand)
for line in fhand:
    words = line.split()
    # print 'Debug:', words
    if len(words) == 0 : continue
    if len(words)<3: continue
    if words[0] != 'From': continue
    print(words[2])