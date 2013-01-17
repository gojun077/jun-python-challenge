# Python challenge Question 1
# K -> M, O -> Q, E-> G... are all letters shifted by two places?
# coding = UTF-8
import string

cstring = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq \
ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr \
gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc\
spj."

cList = []
# convert string to list
for char in cstring:
    cList.append(char)

# shift by 2 letters to the right
for i in range(len(cList)):
    # for ASCII 121 and 122 ('y' and 'z'), y->a, z->b
    if ord(cList[i]) == 121 or ord(cList[i]) == 122:
        newchar = ord(cList[i]) - 24
        cList[i] = chr(newchar)
    # don't shift ASCII code for punctuation or whitespace
    elif string.punctuation in cList[i]:
        pass
    elif cList[i] == ' ':
        pass
    elif cList[i] == '.':
        pass
    # shift alphabet 2 chars to the right
    else:
        newchar = ord(cList[i]) + 2
        cList[i] = chr(newchar)

# convert back from list to string
result = ''.join(cList)    
print(result)
