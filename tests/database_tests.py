import unittest
import shutil

from storage.database import Database


class DatabaseTest(unittest.TestCase):
    def setUp(self):
        self.database = Database('/tmp/testdb', True)
        self.data_to_store = ('vasl1', 'val2', 'val3', 'vqwe')
        self.hash, self.data = self.database.put_block(self.data_to_store)
        self.database.dispose()

    def tearDown(self):
        shutil.rmtree(self.database.database_path)

    def test_db_get_put_binary(self):
        data_from_db = self.database.get_block(self.hash, True)
        self.assertEqual(self.data, data_from_db,
                         'binary data is not equal, something wrong with put_block or get_block')

    def test_db_get_put(self):
        block = self.database.get_block(self.hash)
        for leaf in block.merkle_leaf_data:
            self.assertNotIn(leaf, self.data_to_store, leaf.decode() + ' is not in self.datastore')

    @unittest.skip("chaining data")
    def test_db_put_chain(self):
        pass

    @unittest.skip('not finished test for now')
    def test_db_get_header(self):
        block = self.database.get_block(self.hash)
        header = block.header


'''
block = Block()
block.ParseFromString(blockchain_data)
self.assertEqual(data, data_from_db)
for leaf in data_from_db.merkle_leaf_data:
    print('leaf: ', leaf)
header = data_from_db.header
print('version: ', header.version)
print('merkel root: ', header.merkle_root)
print('timestamp: ', header.timestamp)
shutil.rmtree(database.database_path)
header.parent_block = binascii.unhexlify(zero_hash_str) if genesys else self.last_block_hash

for data in blockchain_data:
print('\ndata: ', blockchain_data) 
'''
