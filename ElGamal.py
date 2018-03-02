import math
import gmpy2
import euclide
import sys
from random import randint
from gmpy2 import mpz, digits

g=2
p=int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF",16)
p=gmpy2.mpz(p)
'''
cpt=0

#######################################"TEST EUCLIDE"
for i in range(1,10001):
    a=gmpy2.mpz_rrandomb(gmpy2.random_state(randint(0,999999999999999)),1024)
    u, v=euclide.euclide(a,p)
    if (a*u+p*v==1):
        cpt=cpt+1
print (cpt)
'''


#######################################"TEST EXPMOD"
'''
sys.setrecursionlimit(1500)
cptexpMod=0
for i in range(0,10000):
    a=gmpy2.mpz_rrandomb(gmpy2.random_state(randint(999999999999999,999999999999999999999999999999999999999999999999999999999999)),1024)
    r=euclide.expMod(p,g,a)
    if(r==gmpy2.powmod(g,a,p)):
        #print("CA MARCHE FDPx")
        cptexpMod=cptexpMod+1
print (cptexpMod)'''


########################################TEST KEYGEN/ENCRYPT/ DECRYPT
'''sys.setrecursionlimit(1500)
x , X=euclide.keyGen(p,g)
print("Bob génère clef privée : ",x)
print("Bob génère clef publique : ",X)


m=1562766473638209786454637777777777766666666666555555555
print("Alice chiffre le message :",m)
C ,B =euclide.encrypt(p,g,X,m)
print("Alice envoie :",C)
print("Alice envoie :",B)

print("Bob recoit le message chiffré, il le déchiffre")
m2=euclide.decrypt(p,C,B,x)
print("message déchiffré :",m2)'''


######################################### PROPRIETE HOMOMORPHIQUE
sys.setrecursionlimit(1500)
x , X=euclide.keyGen(p,g)
m1 = 150
C1, B1 = euclide.encrypt(p,g,X,m1)

m2 = 10
C2, B2 = euclide.encrypt(p,g,X,m2)

C = gmpy2.mul(C1,C2)
B = gmpy2.mul(B1,B2)

m = euclide.decrypt(p,C,B,x)
mtest=(m1*m2)%p
if(m==mtest):
    print("CA MARCHE FDP")
print(m)
print(mtest)



















#print (hex(p))
#mpz.digits(16)
#mpz.digits=16
