import hashlib
import leveldb

# database = leveldb.LevelDB('/home/operator/PycharmProjects/CrAB/db', create_if_missing=False)
# byte_str = (234).to_bytes(4, byteorder='big')
# database.Put('some_data'.encode(), byte_str)
# new_byte_str = database.Get('some_data'.encode())
# data = int.from_bytes(new_byte_str, byteorder='big')
# print(data, new_byte_str)
import binascii
import flatbuffers
import time

import blockchain_storage.protocol.block as protocol
from blockchain_storage import zero_hash_str

builder = flatbuffers.Builder(256)
raw_hash = hashlib.sha256('some'.encode())
print('hash: ', raw_hash.hexdigest())
merkle_root_hash = builder.CreateString(raw_hash.hexdigest())
parent_hash = builder.CreateString(zero_hash_str)

protocol.blockStart(builder)
protocol.blockAddVersion(builder, 1)
protocol.blockAddMerkleRoot(builder, merkle_root_hash)
protocol.blockAddParentBlockHash(builder, parent_hash)
protocol.blockAddTimestamp(builder, int(time.time()))
# protocol.blockAddDataBlock(builder, builder.CreateString(data))
block = protocol.blockEnd(builder)
builder.Finish(block)
buf = builder.Output()
print('buf_len: ', len(buf), 'buf: ', buf)

data = protocol.block.GetRootAsblock(buf, 0)
print('version: ', data.Version())
print('root: ', data.MerkleRoot())
print('parent: ', data.ParentBlockHash())
print('time: ', time.ctime(data.Timestamp()))