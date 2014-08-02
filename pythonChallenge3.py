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

    Given an input string containing only upper- and lower-case letters
    return a list of strings that matches the regex pattern:
    1. [at least one non-uppercase letter] followed by
    2. [exactly three uppercase letters] followed by
    3. [exactly one lowercase letter] followed by
    4. [exactly three uppercase letters] followed by
    5. [at least one non-uppercase letter]

    [^A-Z]+[A-Z]{3}[a-z][A-Z]{3}[^A-Z]+

    >>> XXXoXXX('GdqIQNlQSLidb')
    ['IQNlQSLidb']

    >>> XXXoXXX('cZoExqHxUzeOEKiVEYjR')
    ['zeOEKiVEYj']

    >>> XXXoXXX('VJYxwaZADnMCZqT')
    ['xwaZADnMCZq']

    >>> XXXoXXX('FuCNDeHSBjgsgA')
    ['uCNDeHSBjgsg']

    >>> XXXoXXX('XXXXXXXXXXXXXXXXXXo')
    []
    '''
    regex = r'[a-z]+[A-Z]{3}[a-z][A-Z]{3}[a-z]+'
    matches = re.findall(regex, inStr)

    return matches

def pluckMiddle(inList):
    '''
    ListOfString -> ListofString

    Given a list of strings, pluck out the following pattern of
    chars:
    1. [exactly three uppercase letters] followed by
    2. [exactly one lowercase letter] followed by
    3. [exactly three uppercase letters]

    Then remove all uppercase letters from the resulting string

    >>> pluckMiddle(['IQNlQSLidb'])
    ['l']

    >>> pluckMiddle(['zeOEKiVEYj'])
    ['i']

    >>> pluckMiddle(['xwaZADnMCZq'])
    ['n']

    >>> pluckMiddle(['uCNDeHSBjgsg', 'aAAAbBBBcccc'])
    ['e', 'b']
    '''
    sixCharL = []
    ThOnTh = r'[A-Z]{3}[a-z][A-Z]{3}' #Match pattern XXXoXXX
    for string in inList:
        sixCharL.extend(re.findall(ThOnTh, string))

    regex = r'[A-Z]+' #find all uppercase letters
    singles = []

    for string in sixCharL:
        singles.append(re.sub(regex, '', string))
    return singles

if __name__ == "__main__":
    import doctest
    doctest.testmod()

FILENAME = "/home/archjun/Documents/jun-python-challenge/pythonChallenge3.in"
resultL = []

with open(FILENAME, 'r') as garbledInput:
    for line in garbledInput:
       resultL.extend(pluckMiddle(XXXoXXX(line)))

print(resultL)
