import threading
screen_lock = threading.Semaphore()

class Miner():

    mining = False

    def __init__(self, chain):
        self.chain = chain

    def mine(self):
        print("MINING")
        print(self.mining)
        b = self.chain.createBlock(str(self.chain.mempool))
        self.chain.mempool.clear()
        print("MINING")
        while (self.mining == True):
            if(b.hash.startswith("00000") == True):
                b = b.serialize()
                self.chain.addBlock(b)
                b = self.chain.createBlock(str(self.chain.mempool))
                self.chain.mempool.clear()
            else:
                b.nonce = b.nonce + 1
                b.calculateHash()

