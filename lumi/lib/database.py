import os
import sqlite3


class Database():

    # DATABASE MANAGER
    # DEALS WITH READING AND WRITING DATA TO THE (LOCAL) SQLITE DATABASE

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
        cursor.execute('''
                            CREATE TABLE peers(id INTEGER PRIMARY KEY, port INT,
                                               address TEXT)
                        ''')
        self.db.commit()

    def getNumBlocks(self):
        self.db = sqlite3.connect('data/db')
        cursor = self.db.cursor()
        cursor.execute(
            '''SELECT count( * ) FROM blocks'''
        )
        numBlocks = cursor.fetchone()
        numBlocks = int(numBlocks[0])
        return numBlocks

    def getBlock(self, id):
        self.db = sqlite3.connect('data/db')
        cursor = self.db.cursor()
        cursor.execute(
            '''SELECT * FROM blocks WHERE id=?''', (id,)
        )
        block = cursor.fetchone()
        return block

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
