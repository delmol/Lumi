import time
import hashlib


class Block():

    timestamp = 0
    hash = ""
    data = {}
    prevHash = ""
    chainHash = ""
    merkle = ""
    nonce = 0

    def __init__(self, data, prevHash, chainHash):
        self.timestamp = int(time.time())
        self.data = data
        self.prevHash = prevHash
        self.chainHash = chainHash
        self.merkle = ""
        self.nonce = 0
        self.hash = self.calculateHash()

    def calculateHash(self):
        content = str(self.timestamp) + str(self.data) + str(self.nonce) + str(self.prevHash)
        hash = hashlib.sha256(str(content).encode('utf-8')).hexdigest()
        self.hash = hash
        return hash

    def serialize(self):
        dump = {
            "timestamp": self.timestamp,
            "hash": self.hash,
            "data": self.data,
            "prevHash": self.prevHash,
            "chainHash": self.chainHash,
            "merkle": self.merkle,
            "nonce": self.nonce
        }
        return dump
