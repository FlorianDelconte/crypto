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
     #print("u = %d, v = %d" %(u, v))
    return (u, v)


def expMod(p, g, a):
    if (a==1):
        return g % p
    elif (a%2==0):
        return expMod(p, (g**2) % p, (a/2) % p) % p
    elif ((a%2==1) and (a > 2)):
        return (g * expMod(p, (g**2) % p, ((a-1)/2) % p)) % p


#def keyGen(p, g):




u, v = euclide(325, 145)
print("u =", u, "v =", v)

print(expMod(17, 9, 1))
