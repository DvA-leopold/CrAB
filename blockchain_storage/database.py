import binascii
import hashlib
import leveldb
import time
from typing import Tuple, Union

from blockchain_storage import genesys_data, zero_hash_str
from blockchain_storage.merkle_tree import MerkleTree
from protocol import block_proto_version
from protocol.block_pb2 import Block


class Database:
    def __init__(self, database_path: str, create_if_missing=True):
        self.database_path = database_path
        self.database = leveldb.LevelDB(database_path, create_if_missing=create_if_missing)
        try:
            self.blockchain_height = self.database.Get('blockchain_height'.encode())
            self.blockchain_height = int.from_bytes(self.blockchain_height, byteorder='big')
        except KeyError:
            self.database.Put('blockchain_height'.encode(), int(1).to_bytes(32, byteorder='big'))
            self.blockchain_height = 1
        _, self.last_block_hash = self.check_genesys_and_last_blocks()

    def put_block(self, data: Tuple[str, ...]) -> Tuple[bytes, bytes, bytes]:
        merkle_root, data_block = self.preprocess_data(data)
        header_block = self.generate_header(merkle_root)
        serialized_header_block = header_block.SerializeToString()
        serialized_data_block = data_block.SerializeToString()
        block_header_hash = hashlib.sha256(hashlib.sha256(serialized_header_block).digest()).digest()
        self.database.Put(block_header_hash, serialized_data_block)
        self.last_block_hash = block_header_hash
        self.blockchain_height += 1  # TODO write height to database
        self.database.Put('last_block_hash'.encode(), block_header_hash)
        return block_header_hash, serialized_header_block, serialized_data_block

    def get_block(self, hash_digest: bytes, as_raw_data=False) -> Union[Block, bytes]:
        raw_data = self.database.Get(hash_digest)
        return raw_data if as_raw_data else Block().ParseFromString(raw_data)

    def generate_header(self, merkle_root: bytes, genesys=False) -> Block.Header:
        header = Block.Header()
        header.version = block_proto_version
        header.merkle_root = merkle_root
        header.parent_block = binascii.unhexlify(zero_hash_str) if genesys else self.last_block_hash
        header.timestamp = int(time.time())
        return header

    @staticmethod
    def preprocess_data(data: Tuple[str, ...]) -> Tuple[bytes, Block]:
        data_block = Block()
        data_block.transactions_count = len(data)
        merkle_root = MerkleTree.preprocess_tree(data)
        for dt in data:
            data_block.merkle_leaf_data.append(dt.encode())
        return merkle_root, data_block

    def check_genesys_and_last_blocks(self) -> Tuple[bytes, bytes]:
        merkle_root, data_block = self.preprocess_data(genesys_data)
        header_block = self.generate_header(merkle_root, genesys=True)
        genesys_block_hash = hashlib.sha256(hashlib.sha256(header_block.SerializeToString()).digest()).digest()
        last_block_hash = genesys_block_hash
        try:
            self.database.Get(genesys_block_hash)
            last_block_hash = self.database.Get('last_block_hash'.encode())
        except KeyError:
            data_block.header.MergeFrom(header_block)
            self.database.Put(genesys_block_hash, data_block.SerializeToString())
            self.database.Put('last_block_hash'.encode(), genesys_block_hash)
        return genesys_block_hash, last_block_hash
