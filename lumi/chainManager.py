from models import block
import hashlib
import threading
from lib import database
import json
import urllib
import requests

data = {
        'ids': [12, 3, 4, 5, 6]
}


class ChainManager():

    difficulty = 0  # current blockchain difficulty
    height = 0  # current blockchain height
    chain = {}
    mempool = {}

    def __init__(self):
        self.db = database.Database()
        self.initChain()
        self.verifyGenesis()

    def initChain(self):
        blocks = self.db.getNumBlocks()
        self.height = blocks
        if(blocks > 0):
            '''load chain state & verify'''
            print("Chain exists")
        else:
            self.createGenesisBlock()
        print("Blockchain initialised.")
        print("Block height: " + str(self.height))

    def getBlock(self, id):
        if len(self.chain) > 0:
            return self.chain[id]
        else:
            return None

    def addBlock(self, newBlock):
        if (1 == 1):
            self.height = self.height + 1
            self.db.addBlock(newBlock["hash"], newBlock["prevHash"], newBlock["timestamp"], newBlock["nonce"])
            '''Run Forge Lottery'''
            '''If we won, begin mining'''
            print("Added block: " + newBlock["hash"])
        else:
            print("Block Rejected")

    def createBlock(self, data):
        if len(self.chain) == 0:
            prevHash = "09F663DE96BE771F50CAB5DED00256FFE63773E2EAA9A604092951CC3D7C6621"
        else:
            prevHash = self.chain[len(self.chain) - 1]["hash"]

        newBlock = block.Block(data, prevHash, self.calculateChainHash())
        return newBlock

    def createGenesisBlock(self):
        data = "{0: {'timestamp': 1545674867, 'hash': 'e6e032148741aa49d79c6c6995fd347d0257b5490171bfc4f7971f218d9d14d3', 'inputs': {0: {'address': '', 'amount': 1000000}}, 'outputs': {0: {'address': '1C9SLGeHVLysXobhj737FGp7RsnVXRso12', 'amount': 1000000}}}}"
        genBlock = self.createBlock(data)
        genBlock = genBlock.serialize()
        self.addBlock(genBlock)
        print("Initialised Genesis Block: " + genBlock["hash"])

    def calculateChainHash(self):
        hash = hashlib.sha256(str(self.chain).encode('utf-8')).hexdigest()
        return hash


    def receiveBlock(self, block):
        # check block is valid
        self.addBlock(block)

    def broadcastBlock(self, block):
        r = requests.post('http://127.0.0.1:8555/recblock', json=block)
        print(r.status_code)
        '''req = urllib.request.urlopen('http://127.0.0.1:8555/recblock')
        req.add_header('Content-Type', 'application/json')
        response = urllib.urlopen(req, json.dumps(data))
        response = str(response)
        print(response)'''



    def verifyGenesis(self):
        genesis = self.db.getBlock(1)
        if(genesis[1] == "hash"):
            print()

        if(genesis[2] == "prevHash"):
            print()

        if(genesis[3] == "timestamp"):
            print()

        if(genesis[4] == "nonce"):
            print()

        print(genesis)
        return True