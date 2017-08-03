from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.backends.openssl.backend import Backend
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives.asymmetric.ec import generate_private_key, SECP256K1
from cryptography.hazmat.primitives.serialization import load_pem_private_key, load_pem_public_key

'''
This code must be carefully checked for crypto issues
'''


class CurveCrypto:
    def __init__(self):
        self.backend = Backend()
        self.curve = SECP256K1()
        self.private_key = None
        self.public_key = None

    def generate_private_key(self):
        self.private_key = generate_private_key(self.curve, self.backend)
        self.public_key = self.private_key.public_key()

    def sign_data(self, data: bytes) -> bytes:
        signature = self.private_key.sign(data, ec.ECDSA(hashes.SHA256()))  # bitcoin use double sha
        return signature

    def verify_data(self, signature: bytes, data: bytes) -> bool:
        try:
            self.public_key.verify(signature, data, ec.ECDSA(hashes.SHA256()))
            return True
        except InvalidSignature:
            return False

    def dump_private_key(self, password: str, path_to_key: str):
        with open(path_to_key, 'wb') as pem_file:
            available_encryption = serialization.BestAvailableEncryption(password.encode())
            private_key_bytes = self.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                               format=serialization.PrivateFormat.PKCS8,
                                                               encryption_algorithm=available_encryption)
            pem_file.write(private_key_bytes)

    def load_private_key(self, password: str, path_to_key: str):
        with open(path_to_key, 'rb') as pem_file:
            bin_private_key = pem_file.read()
            self.private_key = load_pem_private_key(bin_private_key, password.encode(), self.backend)

    def dump_public_key(self, path_to_key: str):
        with open(path_to_key, 'wb') as pem_file:
            public_key_bytes = self.public_key.public_bytes(encoding=serialization.Encoding.PEM,
                                                            format=serialization.PublicFormat.SubjectPublicKeyInfo)
            pem_file.write(public_key_bytes)

    def load_public_key(self, path_to_key: str):
        with open(path_to_key, 'rb') as pem_file:
            bin_public_key = pem_file.read()
            self.public_key = load_pem_public_key(bin_public_key, self.backend)
