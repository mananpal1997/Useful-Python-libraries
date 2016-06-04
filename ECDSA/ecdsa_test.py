from ecdsa import SigningKey, NIST384p, VerifyingKey, BadSignatureError
from ecdsa.util import randrange_from_seed__trytryagain, PRNG
import os


# sk = SigningKey.generate() -> uses NIST192p
sk = SigningKey.generate(curve=NIST384p)
vk = sk.get_verifying_key()
signature = sk.sign(b"MANAN PAL")
print(vk.verify(signature, b"MANAN PAL"))
print(sk.to_string())
sk_pem = sk.to_pem()
vk_pem = vk.to_pem()


'''
def make_key(seed):
    secexp = randrange_from_seed__trytryagain(seed, NIST384p.order)
    return SigningKey.from_secret_exponent(secexp, curve=NIST384p)

seed = os.urandom(NIST384p.baselen) # or other starting point
sk1a = make_key(seed)
sk1b = make_key(seed)
# note: sk1a and sk1b are the same key
sk2 = make_key(b"2-"+seed)  # different key
'''

'''
#entropy (produces a strong pseudo-random stream)
rng1 = PRNG("seed")
sk1 = SigningKey.generate(entropy=rng1)
'''

'''
#Create a NIST192p keypair and immediately save both to disk
sk = SigningKey.generate()
vk = sk.get_verifying_key()
open("private.pem","wb").write(bytes(sk.to_pem()))
open("public.pem","wb").write(bytes(vk.to_pem()))

#Load a signing key from disk, use it to sign a message, and write the signature to disk
sk = SigningKey.from_pem(open("private.pem").read())
message = b"hello"
sig = sk.sign(message)
open("signature","wb").write(bytes(sig))

#Load the verifying key, message, and signature from disk, and verify the signature
vk = VerifyingKey.from_pem(open("public.pem").read())
message = str(input("Enter to confirm signature : "))
message = message.encode(encoding = 'utf-8')
sig = open("signature","rb").read()
try:
    vk.verify(sig, message)
    print("good signature")
except BadSignatureError:
    print("BAD SIGNATURE")
'''
