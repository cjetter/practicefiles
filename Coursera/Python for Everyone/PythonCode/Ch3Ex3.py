'''Exercise 3: Write a program to prompt for a score between 0.0 and 1.0.
If the score is out of range, print an error message. If the score is between 0.0 and 1.0,
print a grade using the following table:

Score
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
<0.6   F

'''
import sys

score = input('Please record your score based on the scale 0.0 to 1.0\n')

try:
    while float(score)<0 or float(score)>1:
        score = input('Please try again, entering a numberic score between 0.0 and 1.0\n')
except:
    sys.exit("ERROR - Please try again, entering a numberic score between 0.0 and 1.0")

score1 = float(score)

if score1 >=0.9:
    grade = 'A'
elif score1 >=0.8:
    grade = 'B'
elif score1 >=0.7:
    grade = 'C'
elif score1 >=0.6:
    grade = 'D'
else:
    grade = 'F'

print (('Based on the entered scrore of %s, you have received a letter grade of: '+grade) % str(score))