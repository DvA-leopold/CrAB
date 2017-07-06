import binascii
import leveldb
import time
from typing import Tuple, Union

import sys

from storage import genesys_data, zero_hash_str
from storage.utils import hash256
from storage.merkle_tree import MerkleTree
from protocol import block_proto_version
from protocol.block_pb2 import Block


class Database:
    def __init__(self, database_path: str, create_if_missing=True):
        self.database_path = database_path
        self.database = leveldb.LevelDB(database_path, create_if_missing=create_if_missing)
        try:
            b_h = self.database.Get('blockchain_height'.encode())
            self.blockchain_height = int.from_bytes(b_h, sys.byteorder)
        except KeyError:
            self.database.Put('blockchain_height'.encode(), int(1).to_bytes(8, sys.byteorder))
            self.blockchain_height = 1
        _, self.last_block_hash = self.__check_genesys_and_last_blocks()

    def dispose(self):
        self.database.Put('last_block_hash'.encode(), self.last_block_hash)
        self.database.Put('blockchain_height'.encode(), self.blockchain_height.to_bytes(8, sys.byteorder))

    def put_block(self, data: Tuple[str, ...]) -> Tuple[bytes, bytes]:
        merkle_root, data_block = self.__preprocess_data(data)
        data_block.header.CopyFrom(self.__generate_header(merkle_root))  # TODO do not copy this
        serialized_data = data_block.SerializeToString()
        data_hash = hash256(serialized_data)
        self.database.Put(data_hash, serialized_data)
        self.last_block_hash = data_hash
        self.blockchain_height += 1
        return data_hash, serialized_data

    def get_block(self, hash_digest: bytes, as_raw_data: bool=False) -> Union[Block, bytes]:
        raw_data = self.database.Get(hash_digest)
        block = Block()
        block.MergeFromString(raw_data)
        return raw_data if as_raw_data else block

    def __generate_header(self, merkle_root: bytes, genesys=False):
        header = Block().Header()
        header.version = block_proto_version
        header.merkle_root = merkle_root
        header.parent_block = binascii.unhexlify(zero_hash_str) if genesys else self.last_block_hash
        header.timestamp = int(time.time())
        return header

    @staticmethod
    def __preprocess_data(data: Tuple[str, ...]) -> Tuple[bytes, Block]:
        data_block = Block()
        data_block.transactions_count = len(data)
        merkle_root = MerkleTree.preprocess_tree(data)
        for dt in data:
            data_block.merkle_leaf_data.append(dt.encode())
        return merkle_root, data_block

    def __check_genesys_and_last_blocks(self) -> Tuple[bytes, bytes]:
        merkle_root, data_block = self.__preprocess_data(genesys_data)
        data_block.header.CopyFrom(self.__generate_header(merkle_root, genesys=True))  # TODO do not copy this
        serialized_data = data_block.SerializeToString()
        genesys_block_hash = hash256(serialized_data)
        last_block_hash = genesys_block_hash
        try:
            self.database.Get(genesys_block_hash)
            last_block_hash = self.database.Get('last_block_hash'.encode())
        except KeyError:
            self.database.Put(genesys_block_hash, serialized_data)
            self.database.Put('last_block_hash'.encode(), genesys_block_hash)
        return genesys_block_hash, last_block_hash