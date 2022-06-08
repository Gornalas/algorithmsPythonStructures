def gcd(a,b):
    if a % b == 0:
        return b
    r = a % b
    return gcd(b,r)
