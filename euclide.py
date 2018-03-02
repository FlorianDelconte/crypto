def euclide(r0, r1):

    u0 = 1
    u1 = 0
    v0 = 0
    v1 = 1

    while r1 != 0:

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
    print("u = %d, v = %d" %(u, v))
    return (u, v)

#u, v = euclide(325, 145)
#print("u = %d, v = %d" %(u, v))
