'''Exercise 3: Write a program to prompt the user
for hours and rate per hour to compute gross pay.'''
hours = input('Please enter the number of hours worked, rounded to \nthe nearest hour: ')
while hours.isdigit() == False:
    print('Please try again, rounding to the nearest 15 minute interval:')
    hours = input()
dict_staff = {'General Manager':30, 'Department Supervisor':22.5,'Project Lead':17.5, 'Staff':15}
for keys in dict_staff:
    print (keys)
#keys = dict_staff.viewkeys()
#list(keys)
staff_level = input('Please enter your staff level from the preceding list:\n')

while staff_level not in dict_staff:
    print('Please try again, being sure to match spelling and capitalization as presented in the list:')
    staff_level = input()
print ('Hours Worked: '+str(hours))
print ('Staff Level: '+staff_level)
hourly_rate = int(dict_staff[staff_level])
print ('Hourly Rate: $'+str(hourly_rate)+'/hr')
payment = int(hours)*int(hourly_rate)
print ('Payment: $'+str(payment))

    