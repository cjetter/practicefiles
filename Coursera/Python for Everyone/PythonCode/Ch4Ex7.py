'''Ch4 . Ex 7 : Rewrite the grade program from the previous chapter using a 
function called computegrade that takes a score as its parameter and returns a grade as a string.

Score
>= 0.9 A
>= 0.8 B
>= 0.7 C
>= 0.6 D
<0.6   F

'''
def computegrade():
    score = input('Please enter a numeric score between 0.0 and 1.0\n')
    try:
        while float(score)<0 or float(score)>1:
            score = input('Please try again, entering a numberic score between 0.0 and 1.0\n')
    except:
        quit("ERROR - Please try again, entering a numberic score between 0.0 and 1.0")

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

computegrade() 