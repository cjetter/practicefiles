'''Ch6 . Ex 1: Write a while loop that starts at the last character in the string
and works its way backwards to the first character in the string, printing each letter
on a separate line, except backwards.
'''

fruit = "christopher"
index = -1
while index >= -len(fruit):
    letter = fruit[index]
    print(letter)
    index = index - 1
print ('done')