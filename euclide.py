import gmpy2
from gmpy2 import mpz, digits
from random import randint

def euclide(r0, r1):
    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    while r1 > 1:
        q = r0 // r1

        r = r0 % r1

        u = u0 - q * u1
        v = v0 - q * v1

        r0 = r1
        r1 = r
        u0 = u1
        u1 = u
        v0 = v1
        v1 = v

    return (u, v)

#g=2
#p=grand nombre premier
#a= puissance de g
def expMod(p, g, a):
    a=gmpy2.mpz(a)
    p=gmpy2.mpz(p)
    g=gmpy2.mpz(g)

    if (a==1):
        return gmpy2.f_mod(g , p)
    elif (gmpy2.f_mod(a,2)==0):
        #print("pair")
        na=gmpy2.f_mod(gmpy2.div(a,2),p)
        ng=gmpy2.f_mod(gmpy2.mul(g,g), p)
        #return gmpy2.c_mod((expMod(p, ng, na) , p)
        return gmpy2.f_mod(expMod(p, ng, na),p)
    elif ((gmpy2.f_mod(a,2)==1) and (a>2)):
        #and (a > 2)
        #print("impair")
        na=gmpy2.f_mod(gmpy2.div((a-1),2),p)
        ng=gmpy2.f_mod(gmpy2.mul(g,g), p)
        return  gmpy2.f_mod(gmpy2.mul(expMod(p, ng, na),g),p)
        #return (g * expMod(p, (g**2) % p, ((a-1)/2) % p)) % p




def keyGen(p, g):
    #petit chiffres
    #x = random.randint(2, p-2)
    #X = expMod(p, g, x)
    #gros chiffres
    x= gmpy2.mpz_random(gmpy2.random_state(randint(0,45)),p-3)+2
    X = expMod(p, g, x)
    return (x, X)





def encrypt(p, g, X, m):
    #petit chiffre
    #r = random.randint(2, p-2)
    #grand chiffre
    r=gmpy2.mpz_random(gmpy2.random_state(randint(0,45)),p-3)+2
    print("R = ",r)
    y = expMod(p, X, r)
    print("Y = ",y)
    #petit chiffre
    #C = (m * y) % p
    #grand chiffre
    C=gmpy2.f_mod(gmpy2.mul(m,y),p)
    B = expMod(p, g, r)
    return (C, B)

def decrypt(p, C, B, x):
    D = expMod(p, B, x)
    print("D = ",D)
    u, v = euclide(D, p)
    inverseD = u
    print("inverse = ",inverseD)
    #petit chiffre
    #m = (C * inverseD) % p
    #grand chiffres
    m= gmpy2.f_mod(gmpy2.mul(C,inverseD),p)
    return m
