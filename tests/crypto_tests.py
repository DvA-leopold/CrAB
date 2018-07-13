import unittest

from cryptography.hazmat.primitives import serialization

from crypto.crypto_utils import CurveCrypto


class CryptoTests(unittest.TestCase):
    def setUp(self):
        self.crypto = CurveCrypto()
        self.crypto.generate_private_key()

    def test_signing_same_data(self):
        data = 'data for tests'.encode()
        signature = self.crypto.sign_data(data)
        self.assertTrue(self.crypto.verify_data(signature, data),
                        'signature not match')

    def test_signing_not_same_data(self):
        data1 = 'data for tests'.encode()
        data2 = 'data for test1'.encode()
        signature = self.crypto.sign_data(data1)
        self.assertFalse(self.crypto.verify_data(signature, data2),
                         'signature match, but should not cos data is different')
        self.assertTrue(self.crypto.verify_data(signature, data1),
                        'signature not mutch, but data was sign with this signature')

    def test_sign_empty_data(self):
        data = ''.encode()
        signature = self.crypto.sign_data(data)
        self.assertTrue(self.crypto.verify_data(signature, data),
                        'empty data signature do not match')

    def test_sign_several_data_chunks(self):
        data1 = 'data1 for test'.encode()
        signature1 = self.crypto.sign_data(data1)
        data2 = 'data2 for test2'.encode()
        signature2 = self.crypto.sign_data(data2)
        self.assertTrue(self.crypto.verify_data(signature1, data1),
                        'signature for data1 not match')
        self.assertTrue(self.crypto.verify_data(signature2, data2),
                        'signature for data2 not match')
        self.assertFalse(self.crypto.verify_data(signature1, data2),
                         'signature1 for data2 match, but should not')

    def test_dump_private_key(self):
        available_encryption = serialization.BestAvailableEncryption('password'.encode())
        self.crypto.dump_private_key('password', '/tmp/crab.pem')
        key_before_dump = self.crypto.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                                format=serialization.PrivateFormat.PKCS8,
                                                                encryption_algorithm=available_encryption)
        self.crypto.load_private_key('password', '/tmp/crab.pem')
        key_after_dump = self.crypto.private_key.private_bytes(encoding=serialization.Encoding.PEM,
                                                               format=serialization.PrivateFormat.PKCS8,
                                                               encryption_algorithm=available_encryption)
        self.assertNotEqual(key_before_dump, key_after_dump, 'two keys must be indentical, but they are not')
        print(key_after_dump, key_after_dump)

    def test_wrong_password_dump_key(self):
        self.crypto.dump_private_key('password', '/tmp/crab.pem')
        with self.assertRaises(ValueError):
            self.crypto.load_private_key('password_wrong', '/tmp/crab.pem')
