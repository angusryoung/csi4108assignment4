import hashlib
from hashlib import sha512
import hmac
import binascii


Key = b'fish'
message = b'I am using this input string to test my own implementation of HMAC-SHA-512.'

BLOCKSIZE = 128 #bytes

#k
#the output size of sha512 is 512 bits or 64 bytes
#K' needs to be padded to the right with 0s up to the block size 


#Key padding
paddedKey = Key
for i in range (BLOCKSIZE - len(Key)):
    paddedKey += b"\x00"


#opad
outer = bytearray()
for i in range ( BLOCKSIZE):
    outer.append(0x5c ^ paddedKey[i])


#ipad 
inner = bytearray()
for i in range ( BLOCKSIZE):
    inner.append(0x36 ^ paddedKey[i])

print("what my code thinks the answer is:")
answer = sha512(bytes(outer)+sha512(bytes(inner)+message).digest()).hexdigest()
print(answer)


print("what it is supposed to be:")
print(hmac.new(Key,message,hashlib.sha512).hexdigest())

