from blockchain_storage.database import Database

if __name__ == '__main__':
    blockchain_database = Database('/home/operator/PycharmProjects/CrAB/db')

    hash, header, data = blockchain_database.put_block(('val1', 'val2', 'val3', 'vqwe'))
    print(hash)
    print(blockchain_database.get_block(hash, True))
