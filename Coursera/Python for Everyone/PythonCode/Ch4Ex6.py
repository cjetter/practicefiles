'''Ch4 / Ex 6: Rewrite your pay computation with time-and-a-half for overtime and
create a function called computepay which takes two parameters (hours and rate).'''

## Inserting hours and validating that input is a number
def computepay():
    hours = input('Please input the number of hours worked, rounding to the nearest whole hour:\t')
    try:
        if float(hours) > 40:
            hours_standard = 40
            hours_overtime = float(hours) - 40
        else:
            hours_standard = float(hours)
            hours_overtime = 0
    except:
        print('Please run function again, entering an amount of hours rounded to the nearest hour:')

## Determining rate based on staff level and validating that input is correct
    dict_staff = {'General Manager':30, 'Department Supervisor':22.5,'Project Lead':17.5, 'Staff':15}
    for keys in dict_staff:
        print (keys)
    staff_level = input('Please enter your staff level from the preceding list:\n')

    while staff_level not in dict_staff:
        print('Please try again, being sure to match spelling and capitalization as presented in the list:')
        staff_level = input()
## Providing summary of inputs and calculated amounts
    print ('Standard Hours Worked: '+str(hours_standard))
    print ('Overtime Hours Worked: '+str(hours_overtime))
    print ('Total Hours Worked: '+str(hours))
    print ('Staff Level: '+staff_level)
    hourly_rate = float(dict_staff[staff_level])
    hourly_rate_overtime = float(dict_staff[staff_level])*1.5
    print ('Standard Hourly Rate: $'+str(hourly_rate)+'/hr')
    print ('Overtime Hourly Rate: $'+str(hourly_rate_overtime)+'/hr')
    payment_standard = int(hours_standard)*hourly_rate
    payment_overtime = int(hours_overtime)*hourly_rate_overtime
    payment_total = payment_standard + payment_overtime
    print ('Standard Payment: $'+str(payment_standard))
    print ('Overtime Payment: $'+str(payment_overtime))
    print ('Total Payment: $'+str(payment_total))

computepay()