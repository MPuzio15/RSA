import secrets
import hashlib

def xgcd(a, b):
    """Extended GCD:
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
    with the sign of b if b is nonzero, and with the sign of a if b is 0.
    The numbers x,y are such that gcd = ax+by."""
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q, r = divmod(a, b)
        x, prevx = prevx - q * x, x
        y, prevy = prevy - q * y, y
        a, b = b, r
        print("a", a)
        print("prevx", prevx)
        print("prevy", prevy)
    return a, prevx, prevy


def szyfrowanie(e, n, d):
    try:
        key = secrets.randbits(128)
        if key < n:
            print(hex(key))
            c = pow(key, e, n)
            m = pow(c, d, n)
            print("WARUNEK:", key == m, "key", key, "m", m)
            input()
    except ValueError:
        print("VAL_ERROR:", ValueError.args)


def generacja_podpisu(d, n, e):
    try:
        m = hashlib.sha256()
        h = int(m.hexdigest(), 16)
        print(hex(h), '\n')
        sign = pow(h, d, n)
        print(hex(sign))
        m = pow(sign, e, n)
        print(h == m, hex(m))

    except ValueError:
        print("Cos nie tak przy obliczeniach", ValueError)


def euclid(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def check_if_correct(first_prime, second_prime):
    try:
        e = 65537
        n = first_prime * second_prime
        phi_od_n = (first_prime - 1) * (second_prime - 1)
        (gcd, r, s) = xgcd(e, phi_od_n)
        print("wzglednie pierwsze?", euclid(e, phi_od_n))
        d = r % phi_od_n
        print('\nWykładnik deszyfrujący d = {}'.format(d))
        print('\nPoprawność doboru wykładników: {}'.format(e * d % phi_od_n))  # we get 1 in all of them
        szyfrowanie(e, n, d)

    except ValueError:
        print("ValueError", ValueError)
    except TypeError:
        print("TypeError", TypeError)


def open_file(name):
    try:
        f = open(name, "r")
        t = []
        for line in f:
            t.append(int(line))
        for a in t:
            for b in t:
                if a == b:
                    break
                result = int(euclid(a, b))
                if result != 1:
                    second_prime_of_a = int(a // result)
                    second_prime_of_b = int(b // result)
                    check_if_correct(a, second_prime_of_a)
                    check_if_correct(b, second_prime_of_b)
                else:
                    check_if_correct(a, b)
        f.close()
    except ValueError:
        if ValueError:
            print("ValueError")
        else:
            print("No file")


open_file("modules.txt")




