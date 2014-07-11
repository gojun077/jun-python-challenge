# Python Challenge Question 2
#http://www.pythonchallenge.com/pc/def/ocr.html
#Image: An open book between two orange pillows
#Hint: Recognize the characters. Maybe they are in the book,
#but MAYBE they are in the page source.

#Message in page source: find rare characters in the mess below.

#The obfuscated text to be parsed is in pythonChallenge2.in

FILENAME = "/home/archjun/Documents/jun-python-challenge/pythonChallenge2.in"
with open(FILENAME, 'r') as garbledInput:
    garbledInput = list(garbledInput)

clean = []
for i in garbledInput:
    for char in i:
        if char.isalpha():
            clean.append(char)

print(clean)
