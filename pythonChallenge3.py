#Python Challenge Problem 3
#http://www.pythonchallenge.com/pc/def/equality.html

#Image: shows 1 small candle surrounded by 3 large candles on either side
#Hint: One small letter, surrounded by EXACTLY three big bodyguards on each
#of its sides.

#Notes: I think we have to search through the string and pluck out
#the lower-case letters that are in between 3 upper-case letters on
#either side

import re

def findMiddle(inStr):
    '''
    String -> ListOfString

    Given an input string containing only upper- and lower-case letters
    return a list of strings that match the regex pattern:
    [A-Z]{3}[a-z][A-Z]

    >>> findMiddle('XXXoXXX')
    ['XXXoXXX']

    >>> findMiddle('XXXoYYXoxXXo')
    ['XXXoYYX']

    >>> findMiddle('XXXoYXZoABC')
    ['XXXoYXZ', 'YXZoABC']

    >>> findMiddle('XXXoYXZoABCeQTH')
    ['XXXoYXZ', 'YXZoABC', 'ABCeQTH']

    >>> findMiddle('XXXXXXXXXXXXXXXXXXo')
    []
    '''
    #uses a look-ahead assertion to match pattern as well
    #as overlapping patterns
    regex = r'(?=([A-Z]{3}[a-z][A-Z]{3}))'
    return re.findall(regex, inStr)

def stripUpper(inList):
    '''
    ListOfString -> ListofString

    Given a list of strings where each string contains 3
    uppercase letters followed by 1 lowercase letter followed by
    3 more uppercase letters, remove all uppercase letters from
    each string

    >>> stripUpper(['XXXaXXX'])
    ['a']

    >>> stripUpper(['XXXbYYX'])
    ['b']

    >>> stripUpper(['XXXeYXZ', 'YXZfABC'])
    ['e', 'f']

    >>> stripUpper(['XXXoYXZ', 'YXZoABC', 'ABCeQTH'])
    ['o', 'o', 'e']

    >>> stripUpper(['XXXYXZ', 'YXZABC', 'ABCQTH'])
    ['', '', '']
    '''
    regex = r'[A-Z]+' # match 1 or more uppercase letters
    outList = [re.sub(regex, '', str) for str in inList]
    #remove all empty strings from outList
    while '' in outList:
        del outList[outList.index('')]
    return outList

if __name__ == "__main__":
    import doctest
    doctest.testmod()

FILENAME = "/home/archjun/Documents/jun-python-challenge/pythonChallenge3.in"
resultL = []

with open(FILENAME, 'r') as garbledInput:
    for line in garbledInput:
       resultL.append(stripUpper(findMiddle(line)))

#remove all empty lists from resultL
while [] in resultL:
    del resultL[resultL.index([])]

#join all strings in sublists into one long string
finalStr = ''
for i in range(len(resultL)):
    for j in range(len(resultL[i])):
        finalStr += resultL[i][j]

print(finalStr)
