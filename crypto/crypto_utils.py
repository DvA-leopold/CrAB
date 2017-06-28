from typing import Union

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends.openssl.backend import Backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import generate_private_key, SECP256K1

'''
This code is not safe to use in real apps
'''


class CurveCrypto:
    def __init__(self):
        self.backend = Backend()
        self.curve = SECP256K1()
        self.private_key = None # FIXME should i save dat key in memory?

    def sign_data(self, data: bytes):
        if not self.private_key:
            self.private_key = generate_private_key(self.curve, self.backend)
        signature = self.private_key.sign(data, ec.ECDSA(hashes.SHA256()))
        return signature

    def verify_data(self, signature, data: bytes):
        try:
            self.private_key.public_key().verify(signature, data, ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False

    def print_curve_info(self):
        print('curve name: ', self.curve.name, '\nkey size: ', self.curve.key_size)