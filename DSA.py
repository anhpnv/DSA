import random
from hashlib import sha1

def extended_gcd(aa, bb):
    lastremainder, remainder = abs(aa), abs(bb)
    x, lastx, y, lasty = 0, 1, 1, 0
    while remainder:
        lastremainder, (quotient, remainder) = remainder, divmod(lastremainder, remainder)
        x, lastx = lastx - quotient*x, x
        y, lasty = lasty - quotient*y, y
    return lastremainder, lastx * (-1 if aa < 0 else 1), lasty * (-1 if bb < 0 else 1)

def modinv(a, m):
	g, x, y = extended_gcd(a, m)
	if g != 1:
		raise ValueError
	return x % m

def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def main():
    p = int(input("Chon so nguyen to p: "))
    q = int(input("Chon so nguyen to q sao cho (p-1) % q = 0: "))

    if not(is_prime(p) and is_prime(q)):
        raise ValueError("p,q phai la so nguyen to")

    elif p == q:
        raise ValueError("p va q phai khac nhau")

    M = input("Nhap thong diep M: ")
    M_1 = str.encode(M,'ascii')
    H = int(sha1(M_1).hexdigest(), 16)
    print("Ban ro cua \"{0}\" sau khi ma hoa: {1}".format(M,H))

    h = random.randrange(1, p-1)
    print("Chon h sao cho 1 < h < p-1: ", h)

    g = h**((p-1)//q) % p
    print("Khoa g:",g)

    x = random.randrange(1,q)
    print("Ta co khoa bi mat x:", x)

    y = g ** x % p
    print("Ta co khoa cong khai y:",y)

    k = random.randrange(1, q)
    print("So bi mat k: ",k)

    print("===QUA TRINH KY===")
    r = ((g**k) % p) % q
    s = int((modinv(k,q) * (H + x * r)) % q)
    print("Ta co Signature(r,s) = ({0},{1})".format(r,s))

    print("===QUA TRINH KIEM CHUNG===")
    w = modinv(s,q)
    u1 = (H * w) % q
    u2 = (r * w) % q
    V = ((g**u1 * y**u2 )% p) % q
    if V == r:
        print("v=r= {0} suy ra chu ky co hieu luc".format(r))
    else:
        print("v= {0}, r= {1} suy ra chu ky khong hieu luc".format(V,r))
  


main()
