import hashlib
import time
import binascii
from blockchain_storage.protocol.block_pb2 import Block

data_block = Block()
data_block.version = 1
hash, hash2 = hashlib.sha256('some'.encode()), hashlib.sha256('data'.encode())
print('merkle: ', hash.hexdigest())
print('parent: ', hash2.hexdigest())
data_block.merkle_root = hash.digest()
data_block.parent_block = hash2.digest()
data_block.timestamp = int(time.time())
data_block.data_block = 'byte_data'.encode()

serialized_data = data_block.SerializeToString()
print('data type: ', type(serialized_data))
print('serialized: ', serialized_data)
print('data size: ', len(serialized_data))

data_block.Clear()

new_block = Block()
new_block.ParseFromString(serialized_data)

print('restored version: ', new_block.version)
print('restored root: ', binascii.hexlify(new_block.merkle_root))
print('restored block: ', binascii.hexlify(new_block.parent_block))
print('restored timestamp: ', time.ctime(new_block.timestamp))
