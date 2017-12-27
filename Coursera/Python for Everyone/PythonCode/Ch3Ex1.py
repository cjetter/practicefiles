'''Ch3 / Exercise 1: Rewrite your pay computation to give the employee 1.5 times
the hourly rate for hours worked above 40 hours.'''

## Inserting hours and validating that input is a number
hours = input('Please enter the number of hours worked, rounded to \nthe nearest hour: ')
while hours.isdigit() == False:
    print('Please try again, rounding to the nearest hour:')
    hours = input()
if int(hours) > 40:
    hours_standard = 40
    hours_overtime = int(hours) - 40
else:
    hours_standard = int(hours)

dict_staff = {'General Manager':30, 'Department Supervisor':22.5,'Project Lead':17.5, 'Staff':15}
for keys in dict_staff:
    print (keys)
staff_level = input('Please enter your staff level from the preceding list:\n')

while staff_level not in dict_staff:
    print('Please try again, being sure to match spelling and capitalization as presented in the list:')
    staff_level = input()
print ('Standard Hours Worked: '+str(hours_standard))
print ('Overtime Hours Worked: '+str(hours_overtime))
print ('Total Hours Worked: '+str(hours))
print ('Staff Level: '+staff_level)
hourly_rate = float(dict_staff[staff_level])
hourly_rate_overtime = float(dict_staff[staff_level])*1.5
print ('Standard Hourly Rate: $'+str(hourly_rate)+'/hr')
print ('Overtime Hourly Rate: $'+str(hourly_rate_overtime)+'/hr')
payment = int(hours_standard)*hourly_rate+int(hours_overtime)*hourly_rate_overtime
print ('Payment: $'+str(payment))

    