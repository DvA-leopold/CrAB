import shutil

from blockchain_storage.database import Database

if __name__ == '__main__':
    blockchain_database = Database('/home/leo/PycharmProjects/CrAB/db')

    hash, header, data = blockchain_database.put_block(('vasl1', 'val2', 'val3', 'vqwe'))
    print('hello workd')
    print(hash)
    print(blockchain_database.get_block(hash, True))

    # shutil.rmtree('/home/leo/PycharmProjects/CrAB/db')