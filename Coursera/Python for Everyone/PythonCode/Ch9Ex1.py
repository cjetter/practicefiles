'''Ch9 . Ex 1: Write a program that reads the words in words.txt and stores them as keys in a dictionary. 
It doesn’t matter what the values are. Then you can use the in operator as a fast way to check whether a string is in the dictionary.

NOTE: Code is still messy. Would need to add in try/except, data input entry boxes, and determine if there is a way to simplify the 
parsing process and passage of data between text, string, list and dictionary. Also, need to identify how to capture vocab with multiple nouns
'''

masterstring = ''
keyterms = ['el','la','to','the','los','las']           # list of definite and indefinate articles to maintain with noun after splitting
keyterms2 = ['del','de']                                # list of prepositions to maintain with noun after splitting
fhand = open('TestDict.txt')
fhandw = open('Test.txt', 'w')
for line in fhand:                                      # read file line by line
    words = line.rstrip().split()                       # split lines into list of words with blank spaces trimmed
    for x in words:
        x = x.lower()                                   # split every other word (in lower-case) into lists for keys and values
        if x in keyterms:
            masterstring = masterstring + x +' '        # treatment of articles
        elif x in keyterms2:
            masterstring = masterstring +'*'+ x +' '    # treatment of prepositions
        else:
            masterstring = masterstring + x+','         # treatment of nouns
masterstring = masterstring.replace(',*',' ')           # remove comma from nouns with preposition of de or del following
masterlist = masterstring.split(',')                    # split string into list. every two values is a key:value pairing

#print(masterlist)


masterlistkeys=[]
masterlistvalues=[]
counter = 0
for x in masterlist:
    counter = counter+1-1
    if counter%2==0:
        masterlistvalues = masterlistvalues + [masterlist[counter]]
        counter = counter+1
    else:
        masterlistkeys = masterlistkeys + [masterlist[counter]]
        counter = counter+1

#print(masterlistkeys)
#print(masterlistvalues)

testdict = {}
#print(testdict)
counter = 0
for x in masterlistkeys:
    testdict[x]=masterlistvalues[counter]
    counter=counter+1
print(testdict['to buy'])

#term = input('Enter term to look up: ')
#if term in testdict:
#    print('%s is in the dictionary'%term)
#else:
#    print('%s is not in the dictionary'%term)
#stringA = str(masterlistkeys)
#stringB = str(masterlistvalues)

#fhandw.write(stringA)
#fhandw.write(stringB)
#fhandw.close()