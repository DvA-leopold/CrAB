import hashlib
import leveldb

# database = leveldb.LevelDB('/home/operator/PycharmProjects/CrAB/db', create_if_missing=False)
# hash = hashlib.sha256('data'.encode())
# print('hash: ', hash.digest())
# database.Put(hashlib.sha256('data'.encode()).digest(), 'something'.encode())
# print(database.Get(hashlib.sha256('data'.encode()).digest()))

# print('is object same', string1 is string2)
# print(hash1.hexdigest(), hash2.hexdigest())
# print(hash1, hash2)
# print(hashlib.sha256(hash1.digest()).hexdigest(), hashlib.sha256(hash2.digest()).hexdigest())
from blockchain_storage.merkle_tree import MerkleTree

if __name__ == '__main__':
    pass