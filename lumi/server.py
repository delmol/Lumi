import cherrypy
import json
from models import transaction


class Server(object):

    # SERVER MANAGER
    # CREATES A LISTENING HTTP SERVER ON THE SPECIFIED PORT (SEE CONFIG)
    # HANDLES INCOMING DATA/REQUESTS AND FORWARDS THEM TO THE CHAIN MANAGER

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
    def recblock(self):
        cl = cherrypy.request.headers['Content-Length']
        rawbody = cherrypy.request.body.read(int(cl))
        body = json.loads(rawbody)
        print("Received block:" + body["hash"])
        return body

    @cherrypy.expose
    def height(self):
        height = self.chain.height
        height = "{ height: " + str(height) + " }"
        return height

    @cherrypy.expose
    def transaction(self):
        tx = transaction.Transaction(1)
        tx = tx.serialize()
        self.chain.mempool[len(self.chain.mempool)] = tx
        return str(self.chain.mempool)
