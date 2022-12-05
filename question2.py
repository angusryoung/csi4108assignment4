import sympy as sym #used for isprime() and 
import hashlib 
from hashlib import sha1





# searchPrime =list( sym.primerange((2**159) +1,(2**159) +700) )
# print(searchPrime)

# currentQ =730750818665451459101842416358141509827966271787
# #look for p

# potentialP = currentQ * (2**864)

# for i in range(1000):

#     if (sym.isprime(potentialP+1) and  potentialP % (currentQ **2)!=0):
#             print("found p:")
#             print(potentialP+1)
#             print("i is :")
#             print(i)
#             break

#     if (potentialP>= 2**1024):
#         print("counld not find p is too big")
#         break

#     potentialP += currentQ

#     print(potentialP)

#using the commented code above I was able to find p =89884656743115795386465259539451236680898848983893272197932766940652724760034357226658067546237572728094337321793928379893489083007308550614928369122727068235226022278686814597283199927232279932548615112527677768438150341469143787227500327470127625334183326794991089866822951939781996227914347123564867488089

# 1024-bit prime p
#found using sym.randprime(2**1023, 2**1024 -1)
p = 89884656743115795386465259539451236680898848983893272197932766940652724760034357226658067546237572728094337321793928379893489083007308550614928369122727068235226022278686814597283199927232279932548615112527677768438150341469143787227500327470127625334183326794991089866822951939781996227914347123564867488089
print("test to see if p is prime: "+ str(sym.isprime(p)))
print("test to see if p is a 1024 bit number: "+ str((2**1023)<p<(2**1024)))

#160-bit prime qu
#need to meet condition q|(p-1) and q^2 deos not divide p-1
q= 730750818665451459101842416358141509827966271787
print("test to see if q is prime: "+ str(sym.isprime(q)))
print("test to see if q is a 160 bit number: "+ str((2**159)<q<(2**160)))
print("test to see if q|(p-1) holds true: "+str((p-1)%q == 0))
print("test to see if q^2 deos not divide p-1 holds true: "+str((p-1)%(q**2)!= 0))


#choose h where 1<h<(p-1) and h^((p-1)/q) mod p > 1
h = 3


#generator of the q-order subgroup Zp*
#g= h^((p-1)/q) mod p
#find (p-1)/q
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
M = b"522346828557612" 
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

print("the value of v is :"+ str(v))
print("the value of r is :"+ str(r))



