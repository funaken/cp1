#!/usr/bin/env python

def lets_take_tea_break(m, e, n, c):
    if pow(m, e) % n == c: return str(m)
    return ""

if __name__ == "__main__":
    for i in range(100000):
        if lets_take_tea_break(i, 17, 3569, 915) != "":
            print("answer=" + str(i))
            break

