'''Ch6. Ex 3: Encapsulate this code in a function named count, 
and generalize it so that it accepts the string and the letter as arguments.
'''

def fruitycode():
    fruit = raw_input("Please select the fruit to be analyzed: ")
    letter = raw_input("Please select the letter to be counted: ")
    count = 0
    for target in fruit:
        if target == letter: count = count + 1
    print count

fruitycode()
