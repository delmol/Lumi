import time
import hashlib


class Transaction():

    hash = ""
    timestamp = 0
    type = 1
    inputs = {}
    outputs = {}

    def __init__(self, type):
        self.timestamp = int(time.time())
        self.type = type
        self.hash = self.calculateHash()

    def calculateHash(self):
        content = str(self.timestamp) + str(self.type) + str(self.inputs) + str(self.outputs)
        hash = hashlib.sha256(str(content).encode('utf-8')).hexdigest()
        self.hash = hash
        return hash

    def serialize(self):
        dump = {
            "timestamp": self.timestamp,
            "type": self.type,
            "hash": self.hash,
            "inputs": self.inputs,
            "outputs": self.outputs
        }
        return dump
