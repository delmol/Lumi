import block
import hashlib


class Blockchain():

    difficulty = 0
    height = 0
    chain = {}
    mempool = {}

    def __init__(self):
        self.createGenesisBlock()

    def getBlock(self, id):
        if len(self.chain) > 0:
            return self.chain[id]
        else:
            return None

    def addBlock(self, newBlock):
        if (self.validateBlock(newBlock) == True):
            self.chain[len(self.chain)] = newBlock
            self.height = len(self.chain)
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

    def validateBlock(self, testBlock):
        return True

    def validateChain(self):
        print()

    def validateTransactions(self):
        print()

    def validateTransaction(self):
        print()

    def validateForgeChain(self):
        print()
