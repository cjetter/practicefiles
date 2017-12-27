'''Ch8Ex3: Rewrite the guardian code in the above example without two if statements. Instead, use 
a compound logical expression using the and logical operator with a single if statement.

text file = Ch8Ex2TextFile.txt
'''

fhand = open('Ch8Ex2TextFile.txt')
for line in fhand:
    words = line.split()
    if len(words) != 0 and words[0]=='From':
        try:
            print(words[2]) 
        except:
            print('Error: Date not listed within recipient line')
            continue
    else: continue