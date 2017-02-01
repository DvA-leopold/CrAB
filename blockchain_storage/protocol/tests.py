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

tree_branch = data_block.tree_data_block.add()
tree_branch.parent_hash = hashlib.sha256('data2'.encode()).digest()
tree_branch.data = 'data2'.encode()

tree_branch2 = data_block.tree_data_block.add()
tree_branch2.parent_hash = hashlib.sha256('data33'.encode()).digest()
tree_branch2.data = 'data33'.encode()

serialized_data = data_block.SerializeToString()
print('data type: ', type(serialized_data))
print('serialized: ', serialized_data)
print('data size: ', len(serialized_data))

# data_block.Clear()

new_block = Block()
new_block.ParseFromString(serialized_data)

print('restored version: ', new_block.version)
print('restored root: ', binascii.hexlify(new_block.merkle_root))
print('restored block: ', binascii.hexlify(new_block.parent_block))
print('restored timestamp: ', time.ctime(new_block.timestamp))
for leaf in new_block.tree_data_block:
    print('leaf: ', binascii.hexlify(leaf.parent_hash))
    print('data: ', leaf.data)
