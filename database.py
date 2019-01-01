import os
import sqlite3


class Database():

    def __init__(self):
        '''try connect to local db'''
        '''if not exist, create'''
        if os.path.isfile('data/db'):
            self.db = sqlite3.connect('data/db')
        else:
            self.db = sqlite3.connect('data/db')
            self.initDB()

    def initDB(self):
        cursor = self.db.cursor()
        cursor.execute('''
            CREATE TABLE blocks(id INTEGER PRIMARY KEY, hash TEXT,
                               prevHash TEXT, timestamp TIMESTAMP, nonce INT)
        ''')
        self.db.commit()
        cursor.execute('''
                    CREATE TABLE outputs(id INTEGER PRIMARY KEY, amount INT,
                                       address TEXT)
                ''')
        self.db.commit()

    def addBlock(self, hash, prevHash, timestamp, nonce):
        self.db = sqlite3.connect('data/db')
        cursor = self.db.cursor()
        cursor.execute('''
                    INSERT INTO blocks(hash, prevHash, timestamp, nonce) VALUES(?,?,?,?)
                ''', (hash, prevHash, timestamp, nonce))
        self.db.commit()

    def addUTXO(self):
        print()

    def dropUTXO(self):
        print()