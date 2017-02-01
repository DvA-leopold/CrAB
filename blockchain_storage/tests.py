import hashlib
import leveldb

database = leveldb.LevelDB('/home/operator/PycharmProjects/CrAB/db', create_if_missing=False)
hash = hashlib.sha256('data'.encode())
print('hash: ', hash.digest())
database.Put(hashlib.sha256('data'.encode()).digest(), 'something'.encode())
print(database.Get(hashlib.sha256('data'.encode()).digest()))
