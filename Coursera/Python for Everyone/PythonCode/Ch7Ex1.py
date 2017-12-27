'''Ch7Ex1: Write a program to read through a file and print the contents of the
file (line by line) all in upper case. Executing the program will look as follows:
'''

fhand = open('mbox-short.txt')
for line in fhand:
    print(line.upper())
fhand.close()