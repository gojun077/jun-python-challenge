#Python Challenge Problem 3
#http://www.pythonchallenge.com/pc/def/equality.html

#Image: shows 1 small candle surrounded by 3 large candles on either side
#Hint: One small letter, surrounded by EXACTLY three big bodyguards on each
#of its sides.

#Note 1: I think we have to search through the string and pluck out
#the lower-case letters that are in between 3 upper-case letters on
#either side

#Note 2: If the lowercase letter is surrounded by more than 3 uppercase
#letters on each side, it should not match
# ex: XXXXoXXX, AAAAAAbAAAA

import re

def XXXoXXX(inStr):
    '''
    String -> ListOfString

    Given an input string containing only upper-and-lowercase letters,
    match the following regex pattern:

    1. [one non-uppercase letter] followed by
    2. [exactly three uppercase letters] followed by
    3. [exactly one lowercase letter] followed by
    4. [exactly three uppercase letters] followed by
    5. [one non-uppercase letter]

    and then from within the pattern, return #3 above -- the lowercase
    letter in between 'lUUU' and 'UUUl' where 'l' = lowercase ltr
    and 'U' = UPPERCASE ltr

    >>> XXXoXXX('GdqIQNlQSLidb')
    ['l']

    >>> XXXoXXX('cZoExqHxUzeOEKiVEYjR')
    ['i']

    >>> XXXoXXX('VJYxwaZADnMCZqT')
    ['n']

    >>> XXXoXXX('FuCNDeHSBjgsgA')
    ['e']

    >>> XXXoXXX('XXXXXXXXXXXXXXXXXXo')
    []
    '''
    regex = r'[a-z][A-Z]{3}([a-z])[A-Z]{3}[a-z]'
    matches = re.findall(regex, inStr)

    return matches

if __name__ == "__main__":
    import doctest
    doctest.testmod()

FILENAME = "/home/archjun/Documents/jun-python-challenge/pythonChallenge3.in"
resultL = []

with open(FILENAME, 'r') as garbledInput:
    for line in garbledInput:
       resultL.extend(XXXoXXX(line))

print(resultL)
