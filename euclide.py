import gmpy2
from gmpy2 import mpz, digits

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
    x = random.randint(2, p-2)
    X = expMod(p, g, x)
    return (x, X)


def encrypt(p, g, X, m):
    r = random.randint(2, p-2)
    print("R = ",r)
    y = expMod(p, X, r)
    print("Y = ",y)
    C = (m * y) % p
    B = expMod(p, g, r)
    return (C, B)

def decrypt(p, C, B, x):
    D = expMod(p, B, x)
    print("D = ",D)
    u, v = euclide(D, p)
    inverseD = u
    print("inverse = ",inverseD)
    m = (C * inverseD) % p
    return m



'''u, v = euclide(325, 145)
print("u =", u, "v =", v)

print(expMod(17, 9, 1))'''

'''p = 17
x, X = keyGen(p, 2)
print("x = ",x)
print("X = ",X)
C, B = encrypt(p, 2, X, 16)
print("C = ",C)
print("B = ",B)
m = decrypt(p, C, B, x)
print(m)'''


'''void expMod(mpz_t res,mpz_t p,mpz_t g,mpz_t a) {
//         On applique le modulo après chaque calcul
    mpz_t mod2,gg,aa,un,deux;
//     initialisation des variables
    mpz_init(gg);
    mpz_init(aa);
    mpz_init(deux);
    mpz_init(un);
    mpz_init(mod2);
    mpz_set_d(mod2,2);
    mpz_set_d(deux,2);
    mpz_set_d(un,1);
//     Si a = 1 le résultat est g
    if (mpz_cmp_d(a,1)==0) {
        mpz_mod(gg,g,p);
        mpz_set(res,gg);
    }
    else {
//     Si a est pair le résultat est expMod(res,p,g²,a/2)
        mpz_mod(mod2,a,mod2);
        if (mpz_cmp_d(mod2,0)==0) {
//            g²
            mpz_mul(gg,g,g);
//         a/2
            mpz_fdiv_q(aa,a,deux);
//         Appel récursif
            expMod(res,p,gg,aa);
            mpz_mod(res,res,p);
        }
//     Si a > 2 est impair le résultat est g*expMod(res,p,g²,(a-1)/2)
        else {
            if (mpz_cmp_d(a,2)>0) {
//         g²
                mpz_mul(gg,g,g);
//         a-1
                mpz_sub(aa,a,un);
//         (a-1)/2
                mpz_fdiv_q(aa,aa,deux);
//         Appel récursif
                expMod(res,p,gg,aa);
                mpz_mod(res,res,p);
//         g*expMod(...)
                mpz_mul(res,g,res);
                mpz_mod(res,res,p);
            }
        }

    }
//     Libère la mémoire
    mpz_clear(mod2);
    mpz_clear(gg);
    mpz_clear(aa);
    mpz_clear(deux);
    mpz_clear(un);
}


u, v = euclide(325, 145)
print("u =", u, "v =", v)

print(expMod(17, 9, 1))'''
