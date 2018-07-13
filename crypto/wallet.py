import hashlib

from cryptography.hazmat.backends.openssl.backend import Backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric.ec import SECP256K1, generate_private_key


class Wallet:
    def __init__(self):
        pass

    def generate_wif(self):
        pass

    def generate_address(self, public_key: bytes):
        hash = hashlib.sha224(public_key)
        return hash
        # print(hash.hexdigest())

wallet = Wallet()
key, backend = SECP256K1(), Backend()

private_key = generate_private_key(key, backend)
public_key = private_key.public_key()
serialized_public = public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                            format=serialization.PublicFormat.SubjectPublicKeyInfo)
serialized_private = private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                               format=serialization.PrivateFormat.PKCS8,
                                               encryption_algorithm=serialization.BestAvailableEncryption('pass'.encode()))
print(serialized_private)
# print('key : ', serialized_public.splitlines())
# address = wallet.generate_address(public_key)
# print('address: ', address.hexdigest())