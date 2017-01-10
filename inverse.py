#/usr/bin/env python

from second_code import Bars
from third_code import decode_morse

str1 = "ITT TI I T TIii"
str2 = "T i  I Iii  TTT"
s = str2
for i in range(1000):
    bs = Bars(s)
    if bs.next() == str1:
        print("answer: " + decode_morse(s))
        break
    s = str(bs)
