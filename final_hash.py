import rsa

# pow(a, b) % n == powerMod(a, b, n)
def powerMod(a, b, n):
    t = 1
    while b > 0:
        if b & 1 == 1:
            t = (t * a) % n
        a = (a * a) % n
        b >>= 1
    return t

if __name__ == "__main__":
    pq = 47775743999999999999
    e = 65537
    x = 26984024434151540355
    (p, q) = rsa.factorization(pq)
    d = rsa.calculate_d(p, q, e)
    h = powerMod(x, d, pq)
    print("hash:" + str(h))

