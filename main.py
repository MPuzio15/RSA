import secrets
import hashlib
""" 2. faktoryzacja  bez  faktoryzacji.
    Należy  dokonać  próby  faktoryzacji  modułów  załączonych  w  pliku modules.txt.
    • [max. 3 punkty] Wykonanie faktoryzacji z wykorzystaniem języka Python
      i pokazanie poprawności odnalezionego wykładnika deszyfrującego
      (tj. jego komplementarności matematycznej z wykładnikiem szyfrującym). """


def xgcd(a, b):
    """Extended GCD:
    Returns (gcd, x, y) where gcd is the greatest common divisor of a and b
    with the sign of b if b is nonzero, and with the sign of a if b is 0.
    The numbers x,y are such that gcd = ax+by."""
    prevx, x = 1, 0
    prevy, y = 0, 1
    while b:
        q, r = divmod(a, b)
        print("q", q, "r", r)
        x, prevx = prevx - q*x, x
        y, prevy = prevy - q*y, y
        a, b = b, r
        print("a", a)
        print("prevx", prevx)
        print("prevy", prevy)
    return a, prevx, prevy


def szyfrowanie(e, n, d):
    print("e ", e)
    print("n ", n)
    print("d ", d)
    # klucz publiczny (e, n)
    # n = 143
    # d = 103
    # e = 7
    try:
        key = secrets.randbits(128)
        if key < n:
            print(hex(key))
            # c = pow(key, e, n)
            c = (key ** e) % n
            print("c", c)
            # m = pow(c, d, n)
            m = (c ** d) % n
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

        if r < 0:
            print("r mniejsze od zera", r)
        d = r % phi_od_n
        print("odwrotnosc modulo phi? ", d * e % phi_od_n == 1)
        if d < 0:
            print("d mniejsze od zera", r)
        print('\nWykładnik deszyfrujący d = {}'.format(d))
        print('\nPoprawność doboru wykładników: {}'.format(e * d % phi_od_n))  # we get 1 in all of them
        szyfrowanie(e, n, d)

    except ValueError:
        print("ValueError", ValueError)
    except TypeError:
        print("TypeError", TypeError)



def odwr_mod(a, n):
    p0 = 0
    p1 = 1
    a0 = a
    n0 = n
    q = n0 / a0
    r = n0 % a0
    while r > 0:
        t = p0 - q * p1
        if t >= 0:
            t = t % n
        else:
            t = n - ((-t) % n)
        p0 = p1
        p1 = t
        n0 = a0
        a0 = r
        q = n0 / a0
        r = n0 % a0
    return p1


def open_file(name):
    try:
        f = open(name, "r")
        t = []
        for line in f:
            t.append(int(line))
        #print(t)
        for a in t:
            for b in t:
                if a == b:
                    break  # nie chcemy takich samych
                result = int(euclid(a, b))
                # result = euclid(a, b)
                if result != 1:
                    second_prime_of_a = int(a // result)
                    second_prime_of_b = int(b // result)
                    # second_prime_of_a = (a // result)
                    # second_prime_of_b = (b // result)
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




