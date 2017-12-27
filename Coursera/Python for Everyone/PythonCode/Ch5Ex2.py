'''Ch5 . Ex 1: Write another program that prompts for a list of numbers as above and
at the end prints out both the maximum and minimum of the numbers instead of the average.
'''

smallest = None
largest = None
while True:
    entry = input('Enter a number: ')
    try:
        if entry == 'done':
            break
        else:
            entry1 = float(entry)
            if smallest == None or entry1 < smallest:
                smallest = entry1
            if largest == None or entry1 > largest:
                largest = entry1
            print ("Number Entered: ",str(entry1))
    except:
        print('Invalid entry')
        continue
print("Max: ",str(largest))
print("Min: ",str(smallest))