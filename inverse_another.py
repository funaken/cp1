#/usr/bin/env python

from second_code import Bars
from third_code import decode_morse

def take_away_tea(s):
    return s.replace('T','')

str1 = "ITT TI I T TIii"
str2 = "T i  I Iii  TTT"
s = str2
for i in range(1000):
    bs = Bars(s)
    if bs.next() == str1:
        print("answer: " + ''.join([take_away_tea(decode_morse(take_away_tea(x))) for x in [s, str1, str2]]))
        break
    s = str(bs)
