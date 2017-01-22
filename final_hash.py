
# pow(a, b) % n == powerMod(a, b, n)
def powerMod(a, b, n):
    t = 1
    while b > 0:
        if b & 1 == 1:
            t = (t * a) % n
        a = (a * a) % n
        b >>= 1
    return t

def lets_take_tea_break(m, e, n, c):
    return powerMod(m, e, n) == c

if __name__ == "__main__":
    max_x = 1000000000
    step = max_x / 100
    count = 0
    for x in range(max_x):
        if (x % step) == 0:
            print("step:" + str(count * step))
            count += 1
        if lets_take_tea_break(x, 65537, 47775743999999999999, 26984024434151540355):
            print("answer=" + str(x))
            break

