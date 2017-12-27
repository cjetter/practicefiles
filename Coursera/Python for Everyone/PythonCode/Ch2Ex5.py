'''
Exercise 5: Write a program which prompts the user for a Celsius temperature,
convert the temperature to Fahrenheit, and print out the converted temperature.
'''

Temp_Measure = input('A cual escala deseas convertir la temperatura? C o F?: ')
TestRange = ["C","F"]
while Temp_Measure not in TestRange:
    Temp_Measure = input('Por favor, intentar nuevamente: A cual escala deseas convertir la temperatura? C o F?: ')
Temp = input('Temperatura: ')
while Temp.isdigit == False:
    Temp = input('Por favor, intentar nuevamente. Temperatura: ')
if Temp_Measure == "F":
    Temp_Conv = float(Temp) * 1.8 + 32
    print ('Temperatura en grados de Farenheit: '+str(Temp_Conv)+' '+Temp_Measure)
else:
    Temp_Conv = (float(Temp) - 32) / 1.8
    print ('Temperatura en grados de Celsius: '+str(Temp_Conv)+' '+Temp_Measure)