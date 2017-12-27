'''Ch6. Ex 5: Take the following Python code that stores a string:‘
str = ’X-DSPAM-Confidence:0.8475’
Use find and string slicing to extract the portion of the string after the colon character 
and then use the float function to convert the extracted string into a floating point number.
'''

text = 'X-DSPAM-Confidence:0.8475'
start = text.find(':')+1
new_text = float(text[start:])
print (new_text)

text = 'X-DSPAM-Confidence:    0.8475'
start = text.find(':')+1
new_text = text[start:]
print (new_text)
new_text = text[:]
print (new_text)