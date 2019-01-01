import cherrypy
import json
import transaction


class Server(object):

    def __init__(self, chain):
        self.chain = chain

    @cherrypy.expose
    def index(self):
        return json.dumps(self.chain.chain)

    @cherrypy.expose
    def ping(self):
        '''if is not peer - ping back'''
        '''if success, add to peers'''
        return "has of block hash"

    @cherrypy.expose
    def block(self, id):
        block = json.dumps(self.chain.chain[int(id)])
        return block

    @cherrypy.expose
    def transaction(self):
        tx = transaction.Transaction(1)
        tx = tx.serialize()
        self.chain.mempool[len(self.chain.mempool)] = tx
        return str(self.chain.mempool)
