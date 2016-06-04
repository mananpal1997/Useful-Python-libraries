from passlib.hash import sha256_crypt
from passlib.apps import custom_app_context as pwd_context
from passlib.hash import md5_crypt #yet another type of hash

hash1 = sha256_crypt.encrypt("password")
#print(hash1)
#40000 iterations

if(sha256_crypt.verify(str(input("Enter password : ")), hash1) == True):
    print("correct match")
else:
    print("incorrect match")

hash2 = pwd_context.encrypt("somepass", category="admin")
#80000 iterations, stronger encryptions

