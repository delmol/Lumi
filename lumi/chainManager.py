from models import block
import hashlib
import threading
from lib import database
import json


class ChainManager():

    difficulty = 0  # current blockchain difficulty
    height = 0  # current blockchain height
    chain = {}
    mempool = {}

    def __init__(self):
        self.db = database.Database()
        self.initChain()

    def initChain(self):
        blocks = self.db.getNumBlocks()
        self.height = blocks
        if(blocks > 0):
            '''load chain'''
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
            self.chain[len(self.chain)] = newBlock
            self.height = len(self.chain)
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
