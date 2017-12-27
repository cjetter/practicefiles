'''Exercise 2: Write a program that uses input to prompt a user for their name
and then welcomes them.'''
name = input ("Yo! What's your name?\n")
while name.isalpha() == False:
    print('Please enter your name with the letters of the alphabet only:')
    name = input ()
n = '!'
print ("It's nice to meet you, "+name+"%s" % (n))