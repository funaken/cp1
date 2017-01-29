import sympy
import fractions

def factorization(x):
    h = sympy.factorint(x)
    return map(lambda n:n, h)

def lcm(a, b):
    return a * b / fractions.gcd(a,b)

def calculate_d_sub(a, b):
    if b == 0:
        u = 1
        v = 0
    else:
        q = a / b
        r = a % b
        (u0, v0) = calculate_d_sub(b, r)
        u = v0
        v = u0 - q * v0
    return (u, v)

def calculate_d(p, q, e):
    l = lcm(p - 1, q - 1)
    d = calculate_d_sub(e,l)[0]
    if d < 0:
        d += l
    return d

if __name__ == '__main__':
    print("f=" + str(factorization(47775743999999999999)))
    print("f=" + str(factorization(65537)))
    print("gcd=" + str(fractions.gcd(24,36)))
    print("d=" + str(calculate_d(193,11,77)))

