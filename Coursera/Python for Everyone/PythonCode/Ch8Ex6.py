'''Ch8 . Ex 6: Rewrite the program that prompts the user for a list of numbers and prints 
out the maximum and minimum of the numbers at the end when the user enters “done”. 
Write the program to store the numbers the user enters in a list and use the max() and min() functions 
to compute the maximum and minimum numbers after the loop completes.
'''

masterlist = list()
while True:
    entry = input('Enter a number: ')
    try:
        if entry == 'done':
            break
        else:
            entry1 = float(entry)
            masterlist = masterlist + [entry1]
            print ("Number Entered: ",str(entry1))
    except:
        print('Invalid entry')
        continue
MaxEntry = str(max(masterlist))
MinEntry = str(min(masterlist))
print("Max: ",MaxEntry)
print("Min: ",MinEntry)