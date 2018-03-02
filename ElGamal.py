import math
import gmpy2
import euclide
from random import randint
from gmpy2 import mpz, digits

g=2
p=int("FFFFFFFFFFFFFFFFC90FDAA22168C234C4C6628B80DC1CD129024E088A67CC74020BBEA63B139B22514A08798E3404DDEF9519B3CD3A431B302B0A6DF25F14374FE1356D6D51C245E485B576625E7EC6F44C42E9A637ED6B0BFF5CB6F406B7EDEE386BFB5A899FA5AE9F24117C4B1FE649286651ECE65381FFFFFFFFFFFFFFFF",16)
cpt=0

#######################################"TEST EUCLIDE"
#for i in range(1,10001):
#    a=gmpy2.mpz_rrandomb(gmpy2.random_state(randint(0,999999999999999)),1024)
#    u, v=euclide.euclide(a,p)
#    if (a*u+p*v==1):
#        cpt=cpt+1
#print (cpt)


#######################################"TEST EXPMOD"
for i in range(1,10001):
    g=gmpy2.mpz_rrandomb(gmpy2.random_state(randint(0,999999999999999)),1024)
    r=euclide.expMod(17,g,i)
    if ((g**i)%17==r):
        cpt=cpt+1
print (cpt)




























#print (hex(p))
#mpz.digits(16)
#mpz.digits=16
