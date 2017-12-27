'''Ch8Ex4: Write a program to open the file romeo.txt and read it line by line. 
For each line, split the line into a list of words using the split function.
For each word, check to see if the word is already in a list. If the word is not in
the list, add it to the list. When the program completes, sort and print the resulting 
words in alphabetical order.
'''
masterlist = list()
fhand = open('romeo.txt')
for line in fhand:              # read file line by line
    words = line.split()        # split lines into list of words
    for x in words:
        x = x.lower()
        if x in masterlist: continue
        else: masterlist = masterlist + [x]
print(masterlist)
        