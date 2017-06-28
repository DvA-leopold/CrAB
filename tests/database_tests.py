import leveldb

import sys
import unittest


class DatabaseTest(unittest.TestCase):
    def test_data(self):
        self.assertTrue('FOO'.isupper(), 'no')

# if __name__ == '__main__':
#     unittest.main()

# database = leveldb.LevelDB('/home/leo/PycharmProjects/CrAB/db', create_if_missing=True)
# database.Put('data'.encode(), int(1241241241241224124).to_bytes(8, sys.byteorder, signed=False))
#
# bytes_data = database.Get('data'.encode())
# int_data = int.from_bytes(bytes_data, sys.byteorder, signed=False)
#
# print(int_data)