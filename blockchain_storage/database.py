import leveldb
import hashlib

import binascii
import time

from blockchain_storage import genesys_data, zero_hash_str
from blockchain_storage.merkle_tree import MerkleTree
from blockchain_storage.protocol import block_proto_version
from blockchain_storage.protocol.block_pb2 import Block


class Database:
    def __init__(self, database_path: str, create_if_missing=True):
        self.database_path = database_path
        self.database = leveldb.LevelDB(database_path, create_if_missing=create_if_missing)
        _, self.last_block_hash = self.check_genesys_and_last_blocks()
        try:
            self.blockchain_height = self.database.Get('blockchain_height'.encode())
            self.blockchain_height = int.from_bytes(self.blockchain_height, byteorder='big')
        except KeyError:
            self.database.Put('blockchain_height'.encode(), int(1).to_bytes(32, byteorder='big'))
            self.blockchain_height = 1

    def put_block(self, data: str):
        data_hash = hashlib.sha256(hashlib.sha256(data))
        serialized_data = self.serialize(data)
        self.database.Put(data_hash.hexdigest(), serialized_data)
        self.last_block_hash = data_hash  # TODO write new last block hash to db
        self.blockchain_height += 1

    def get_block(self, key: str, as_raw_data=False) -> Block:
        raw_data = self.database.Get(key.encode())
        data_block = Block()
        return raw_data if as_raw_data else data_block.ParseFromString(raw_data)

    def serialize(self, data: str) -> bytes:
        data_block = Block()
        data_block.version = block_proto_version
        data_block.merkle_root = MerkleTree.calculate_merkle_root(data)
        data_block.parent_block = binascii.unhexlify(zero_hash_str) if self.blockchain_height == 1 else self.last_block_hash
        data_block.timestamp = int(time.time())
        data_block.data_block = data.encode()
        return data_block.SerializeToString()

    def check_genesys_and_last_blocks(self):
        serialized_data = self.serialize(genesys_data)
        genesys_block_hash = hashlib.sha256(hashlib.sha256(serialized_data)).digest()
        last_block_hash = genesys_block_hash
        try:
            self.database.Get(genesys_block_hash)
            last_block_hash = self.database.Get('last_block_hash'.encode())
        except KeyError:
            self.database.Put(genesys_block_hash, serialized_data)
            self.database.Put('last_block_hash'.encode(), genesys_block_hash)
        return genesys_block_hash, last_block_hash
