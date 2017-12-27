'''Ch10Ex3: Write a program that reads a file and prints the letters in decreasing order of frequency. 
Your program should convert all the input to lower case and only count the letters a-z. 
Your program should not count spaces, digits, punctua- tion, or anything other than the letters a-z. 
Find text samples from several different languages and see how letter frequency varies between languages. 
Compare your results with the tables at wikipedia.org/wiki/Letter_frequencies.

Is there a way to say that if the character is not 
'''

import string

d = dict()
goodtext = string.ascii_lowercase
name = input('Name of file: ')
fhand = open(name)
for line in fhand:
    line = line.translate(line.maketrans('','',string.punctuation))
    line = line.translate(line.maketrans('','',string.digits))
    line = line.strip()
    line = line.lower()
    line = line.split()
    for word in line:
        for char in word:
            if char not in goodtext: continue
            else:
                d[char]=d.get(char,0)+1
lst = list()
for key,val in list(d.items()):
    lst.append((val,key))
lst.sort(reverse=True)
for x,y in lst:
    print(y,x)