import sys
import math
import string

class ASCIIChar:
    def __init__(self, match, char):
        self.match = match
        self.char = char
        
l = int(input())
h = int(input())
t = input()

row = []

for i in range(h):
    row.append(input())

ASCIIChars = []

for i in range(27):
    if i != 26:
        tm = string.ascii_lowercase[i]+string.ascii_uppercase[i]
    else:
        tm = ""
        
    temp = []
    str = ""
    for j in row:
        str = j[i*l:i*l+l]
        temp.append(str)
    
    ASCIIChars.append(ASCIIChar(tm,temp))

check = False
for i in range(h):
    s = ""
    for j in t:
        check = False
        for k in ASCIIChars:
            if j in k.match:
                s += k.char[i]
                check = True
                break
        if not check:
            s += ASCIIChars[26].char[i]
    print(s)
                