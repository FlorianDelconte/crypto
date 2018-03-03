import math
import gmpy2
import elGamal
import sys
from random import randint
from gmpy2 import mpz, digits


sys.setrecursionlimit(1500)
g=2
p=int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF",16)
p=gmpy2.mpz(p)

f=open("test.txt","w")
f.write("p : " + str(p) + "\n")
f.write("g : " + str(g) + "\n\n")


#######################################"TEST EUCLIDE"

f.write("##################################TEST EUCLIDE \n")
cpt=0
for i in range(1,10001):

    a=gmpy2.mpz_rrandomb(gmpy2.random_state(randint(0,999999999999999)),1024)
    u, v=elGamal.euclide(a,p)
    if (a*u+p*v==1):
        cpt=cpt+1
    if(i<=5):
        f.write("a :")
        f.write(str(a)+"\n")
        f.write("u :")
        f.write(str(u)+"\n")
        f.write("v :")
        f.write(str(v)+"\n")
        f.write("a*u+p*v :")
        f.write(str(a*u+p*v)+"\n\n")

print(cpt, " tests euclide réussis sur 10000")


#######################################"TEST EXPMOD"

f.write("##################################TEST EXPMOD \n")

cptexpMod=0
for i in range(0,10000):
    a=gmpy2.mpz_rrandomb(gmpy2.random_state(randint(999999999999999,999999999999999999999999999999999999999999999999999999999999)),1024)
    r=elGamal.expMod(p,g,a)
    t=gmpy2.powmod(g,a,p)
    if(r==t):
        cptexpMod=cptexpMod+1
    if (i<5):
        f.write("a : " + str(a) + "\n")
        f.write("Notre fonction expMod : " + str(r) + "\n")
        f.write("Fonction de gmpy2 : " + str(t) + "\n\n")

print(cptexpMod, " tests expmod réussis sur 10000")


########################################TEST KEYGEN/ENCRYPT/ DECRYPT

f.write("##################################TEST KEYGEN / ENCRYPT/ DECRYPT \n")

x , X=elGamal.keyGen(p,g)

cpt = 0
for i in range(0,100):
    m = gmpy2.mpz_random(gmpy2.random_state(randint(999999999999999,999999999999999999999999999999999999999999999999999999999999)), p)
    C ,B = elGamal.encrypt(p,g,X,m)
    m2 = elGamal.decrypt(p,C,B,x)

    if (m==m2):
        cpt = cpt + 1

    if (i<5):
        f.write("Message à chiffrer : " + str(m) + "\n")
        f.write("Message déchiffré : " + str(m2) + "\n\n")

print(cpt, " tests keygen encrypt decrypt réussis sur 100")

######################################### PROPRIETE HOMOMORPHIQUE

f.write("##################################TEST PROPRIETE HOMOMORPHIQUE \n")

x , X=elGamal.keyGen(p,g)

cpt = 0
for i in range(0,100):
    m1 = gmpy2.mpz_random(gmpy2.random_state(randint(999999999999999,999999999999999999999999999999999999999999999999999999999999)), p)
    C1, B1 = elGamal.encrypt(p,g,X,m1)

    m2 = gmpy2.mpz_random(gmpy2.random_state(randint(999999999999999,999999999999999999999999999999999999999999999999999999999999)), p)
    C2, B2 = elGamal.encrypt(p,g,X,m2)

    C = gmpy2.mul(C1,C2)
    B = gmpy2.mul(B1,B2)

    m = elGamal.decrypt(p,C,B,x)
    mtest=(m1*m2)%p

    if (m==mtest):
        cpt = cpt + 1

    if (i<5):
        f.write("Message 1 à chiffrer : " + str(m1) + "\n")
        f.write("Message 2 à chiffrer : " + str(m2) + "\n")
        f.write("Message déchiffré par notre fonction : " + str(m) + "\n")
        f.write("Message (m1*m2) % p : " + str(mtest) + "\n\n")

print(cpt, " tests de la propriété homomorphique réussis sur 100")

f.close()
