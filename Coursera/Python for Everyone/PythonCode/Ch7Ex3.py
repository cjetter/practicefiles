'''Ch7Ex3: Sometimes when programmers get bored or want to have a bit of fun, 
they add a harmless Easter Egg to their program Modify the program that prompts the user for the file name
so that it prints a funny message when the user types in the exact file name “na na boo boo”. 
The program should behave normally for all other files which exist and don’t exist.
'''

name = input("Please enter the name of the text file \nwith '.txt' attached to the end: ")
try:
    fhand = open(name)
except:
    name = name.lower()
    if name == 'na na boo boo': 
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit ()
    else:
        quit ('The file, '+name+', cannot be located. Please confirm name and location.')
keyterm = 'subject:'
count = 0
for line in fhand:
    if not keyterm in line.lower(): continue
    else:
        count = count +1
print ('Quantity: ',count)