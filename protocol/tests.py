import binascii
import hashlib
import time

from protocol import Block


def serialisation_test():
    data_block = Block()
    data_block.header.version = 1
    hash, hash2 = hashlib.sha256('some'.encode()), hashlib.sha256('data'.encode())
    print('merkle: ', hash.hexdigest())
    print('parent: ', hash2.hexdigest())
    data_block.header.merkle_root = hash.digest()
    data_block.header.parent_block = hash2.digest()
    data_block.header.timestamp = int(time.time())

    tree_branch = data_block.branch_data.add()
    tree_branch.parent_hash = hashlib.sha256('data2'.encode()).digest()
    tree_branch.data = 'data2'.encode()

    tree_branch2 = data_block.branch_data.add()
    tree_branch2.parent_hash = hashlib.sha256('data33'.encode()).digest()
    tree_branch2.data = 'data33'.encode()

    serialized_data = data_block.SerializeToString()
    print('data type: ', type(serialized_data))
    print('serialized: ', serialized_data)
    print('data size: ', len(serialized_data))

    new_block = Block()
    new_block.ParseFromString(serialized_data)

    print('restored version: ', new_block.header.version)
    print('restored root: ', binascii.hexlify(new_block.header.merkle_root))
    print('restored block: ', binascii.hexlify(new_block.header.parent_block))
    print('restored timestamp: ', time.ctime(new_block.header.timestamp))
    for leaf in new_block.branch_data:
        print('leaf: ', binascii.hexlify(leaf.parent_hash))
        print('data: ', leaf.data)

if __name__ == '__main__':
    # serialisation_test()
    header = Block.Header()
    header.version = 2
