'''Ch5 . Ex 1: Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, 
print out the total, count, and average of the numbers. If the user enters anything other than a number, detect their mistake
using try and except and print an error message and skip to the next number.

Enter a number: 4
Enter a number: 5
Enter a number: bad data
Invalid input
Enter a number: 7
Enter a number: done
16 3 5.333333333333333

ATTENTION: MUST RUN IN PYTHON 3 !!!!

'''

total = 0
count = 0
while True:
    entry = input('Enter a number: ')
    try:
        if entry == 'done':
            break
        else:
            entry1 = float(entry)
            total = total + entry1
            count = count + 1
            print ("Number Entered: ",str(entry1))
    except:
        print('Invalid entry')
        continue
print("Total: ",str(total))
print("Quantity: ",str(count))
avg = total/count
print("Average: ",str(avg))