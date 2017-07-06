import unittest

from crypto.crypto_utils import CurveCrypto


class CryptoTests(unittest.TestCase):
    def test_signing_same_data(self):
        crypto = CurveCrypto()
        data = 'data for tests'.encode()
        signature = crypto.sign_data(data)
        self.assertTrue(crypto.verify_data(signature, data),
                        'signature not match')

    def test_signing_not_same_data(self):
        crypto = CurveCrypto()
        data1 = 'data for tests'.encode()
        data2 = 'data for test1'.encode()
        signature = crypto.sign_data(data1)
        self.assertFalse(crypto.verify_data(signature, data2),
                         'signature match, but should not cos data is different')
        self.assertTrue(crypto.verify_data(signature, data1),
                        'signature not mutch, but data was sign with this signature')

    def test_sign_empty_data(self):
        crypto = CurveCrypto()
        data = ''.encode()
        signature = crypto.sign_data(data)
        self.assertTrue(crypto.verify_data(signature, data),
                        'empty data signature do not match')

    def test_sign_several_data_chunks(self):
        crypto = CurveCrypto()
        data1 = 'data1 for test'.encode()
        signature1 = crypto.sign_data(data1)
        data2 = 'data2 for test2'.encode()
        signature2 = crypto.sign_data(data2)
        self.assertTrue(crypto.verify_data(signature1, data1),
                        'signature for data1 not match')
        self.assertTrue(crypto.verify_data(signature2, data2),
                        'signature for data2 not match')
        self.assertFalse(crypto.verify_data(signature1, data2),
                         'signature1 for data2 match, but should not')