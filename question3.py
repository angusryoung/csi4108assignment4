import sympy as sym #used for isprime() and 
import hashlib 
from hashlib import sha1


#using the same implementation as before i am signing a difference message 8161474912883 using the same k value

p = 89884656743115795386465259539451236680898848983893272197932766940652724760034357226658067546237572728094337321793928379893489083007308550614928369122727068235226022278686814597283199927232279932548615112527677768438150341469143787227500327470127625334183326794991089866822951939781996227914347123564867488089
q= 730750818665451459101842416358141509827966271787

h = 3

a = (2**864) + 8
h = 420000 #randomly renerated number between 1 and  p-1
g = pow(h,a,p)
#user's Private Key
x = 11111111111111111111111111111111111
#user's Public Key
y = pow(g,x,p)
#user's pre-message secret number
k = 2222222222222222222222222222222222

#signing
r = pow(g,k,p)%q

inversek = pow(k,-1,q )
M = b"8161474912883"  #DIFFERENT MESSAGE
hashM =  int( (sha1(M).hexdigest()),base=16)

s = (inversek*(hashM+(x*r)))%q

print("signature is ("+ str(r) + " , " + str(s)+ ") ")

#verifying
w1 = pow (s,-1,q)

u1 = (int((sha1(M).hexdigest()),base=16)*w1)%q
u2 = (r*w1) % q


#find v = (((g**u1)*(y**u2))%p)%q
# using modular arithmetic properties
v = ((pow(g,u1,p)* pow(y,u2,p))%p)%q



#Attacker trying to learn K
#K =  [H(m1) - H(m2)] * modular_inverse(s1-s2, q)

#H(m2)
M2 = b"522346828557612" 
hashM2 =  int( (sha1(M2).hexdigest()),base=16)

s2 = 545272591326537567397114431234633245362001168023

attackerK = ((hashM - hashM2) * pow(s- s2 ,-1,q))%q 
print("attacker thinks K is :"+str(attackerK))

#attacker can find x now he has K
attackerX = ((attackerK*s-hashM)*pow(r,-1,q))%q

print("attacker thinks x is :"+str(attackerX))
