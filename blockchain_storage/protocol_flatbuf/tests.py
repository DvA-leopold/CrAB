import hashlib
import flatbuffers
import time

import blockchain_storage.protocol_flatbuf.block as protocol
from blockchain_storage import zero_hash_str

builder = flatbuffers.Builder(256)
raw_hash = hashlib.sha256('some'.encode())
print('hash: ', raw_hash.hexdigest())
merkle_root_hash = builder.CreateString(raw_hash.hexdigest())
parent_hash = builder.CreateString(zero_hash_str)
#  serialized
protocol.blockStart(builder)
protocol.blockAddVersion(builder, 1)
protocol.blockAddMerkleRoot(builder, merkle_root_hash)
protocol.blockAddParentBlockHash(builder, parent_hash)
protocol.blockAddTimestamp(builder, int(time.time()))
# protocol_flatbuf.blockAddDataBlock(builder, builder.CreateString(data))
block = protocol.blockEnd(builder)
builder.Finish(block)
buf = builder.Output()
print('buf_len: ', len(buf), 'buf: ', buf)
# deserialized
data = protocol.block.GetRootAsblock(buf, 0)
print('version: ', data.Version())
print('root: ', data.MerkleRoot())
print('parent: ', data.ParentBlockHash())
print('time: ', time.ctime(data.Timestamp()))