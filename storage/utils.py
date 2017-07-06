import hashlib


def hash256(hash_data: bytes):
    return hashlib.sha256(hashlib.sha256(hash_data).digest()).digest()