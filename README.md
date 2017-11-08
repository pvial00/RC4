# RC4
Python class implementation of the RC4 cipher (slighlty modeled after Apple's C implementation)  
Supports both Python2 and Python3  

from RC4 import RC4  

rc4 = RC4("key")  
cipher_text = rc4.crypt("data")  
