import os
from cryptography.fernet import Fernet
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography import x509
from cryptography.x509.oid import NameOID
from cryptography.hazmat.primitives import hashes

key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"A really secret message.")
print('encrypted : ',str(token))
print('decrypted : ',str(f.decrypt(token)))

'''
key = rsa.generate_private_key(public_exponent=65537,key_size=2048,backend=default_backend())
with open("key.pem", "wb") as f:
    f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
        ))
'''

'''
# If you’ve already generated a key you can load it with load_pem_private_key()
key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048,
    backend=default_backend()
    )
# Write our key to disk for safe keeping
with open("key.pem", "wb") as f:
        f.write(key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.TraditionalOpenSSL,
        encryption_algorithm=serialization.BestAvailableEncryption(b"passphrase"),
        ))

# Generate a CSR (certificate signing request)
csr = x509.CertificateSigningRequestBuilder().subject_name(x509.Name([
    # Provide various details about who you are.
    x509.NameAttribute(NameOID.COUNTRY_NAME, u"US"),
    x509.NameAttribute(NameOID.STATE_OR_PROVINCE_NAME, u"CA"),
    x509.NameAttribute(NameOID.LOCALITY_NAME, u"San Francisco"),
    x509.NameAttribute(NameOID.ORGANIZATION_NAME, u"My Company"),
    x509.NameAttribute(NameOID.COMMON_NAME, u"mysite.com"),
    ])).add_extension(
	x509.SubjectAlternativeName([
		# Describe what sites we want this certificate for.
		x509.DNSName(u"mysite.com"),
		x509.DNSName(u"www.mysite.com"),
		x509.DNSName(u"subdomain.mysite.com"),
		]),
	critical=False,
	# Sign the CSR with our private key.
).sign(key, hashes.SHA256(), default_backend())
# Write our CSR out to disk.
with open("csr.pem", "wb") as f:
    f.write(csr.public_bytes(serialization.Encoding.PEM))

def decrypt_file(file_name, key):
    with open(file_name, 'rb') as fo:
        ciphertext = fo.read()
    dec = decrypt(ciphertext, key)
    with open(file_name[:-4], 'wb') as fo:
        fo.write(dec)
'''

'''
#random key generation
iv = os.urandom(16)
#iv = b'JT\xd3eY\x8d\xda\xdc\xda\x04\x9f\x1b\x11y\xa5\xcf'
serial = int.from_bytes(os.urandom(20), byteorder="big")
#serial = 1306509249204385676128142508742140326393358959058
'''
