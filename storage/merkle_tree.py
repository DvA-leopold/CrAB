import hashlib
from typing import Tuple

from storage.utils import hash256


class MerkleTree:
    @staticmethod
    def preprocess_tree(data: Tuple[str, ...]) -> bytes:
        hash_list = [hash256(data_el) for data_el in data]
        while len(hash_list) > 1:
            if len(hash_list) % 2 != 0:
                hash_list.append(hash_list[-1])
            new_hash_list = []
            for i in range(0, len(hash_list) - 1, 2):
                concat = hash_list[i] + hash_list[i + 1]
                concat_hash = hash256(concat)
                new_hash_list.append(concat_hash)
            hash_list = new_hash_list
        return hash_list[0]

    @staticmethod
    def merkle_proof(hash: bytes):
        return True