#Python Challenge Question 1
#http://www.pythonchallenge.com/pc/def/map.html
#Image:  K -> M, O -> Q, E-> G... are all letters shifted by two places?
#Hint: everybody thinks twice before solving this.

import doctest

cstring = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq \
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr \
gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc \
spj."

cList = cstring.split()

def shiftChars(los):
    '''
    ListofString -> ListofString

    Given los, for each element in los shift the ASCII code of every
    lowercase alphabetic character by +2 and return a new los. For
    the letters y (ASCII 121) and z (ASCII 122) wrap around to
    a (ASCII 97) and b (ASCII 98), respectively.

    >>> shiftChars(['abc', 'def'])
    ['cde', 'fgh']

    >>> shiftChars(['yow', 'sos'])
    ['aqy', 'uqu']
    '''
    shiftedList = []
    for word in los:
        shiftWord = ''
        for char in word:
            if char.isalpha():
                if ord(char) > 120:
                    shiftASCII = ord(char) - 24
                    shiftWord += chr(shiftASCII)
                else:
                    shiftASCII = ord(char) + 2
                    shiftWord += chr(shiftASCII)
            #non-alpha chars like punctuation
            else:
                shiftWord += char
        shiftedList.append(shiftWord)

    return shiftedList

doctest.testmod()

print(' '.join(shiftChars(cList)))
print(shiftChars(['http://www.pythonchallenge.com/pc/def/map.html']))
