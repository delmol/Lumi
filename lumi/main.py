from threading import Thread
import cherrypy
import server
import chainManager
import miner


chainManager = chainManager.ChainManager()  # Create instance of Chain Manager
minerD = miner.Miner(chainManager)  # Create instance of Miner Daemon


def startServer():
    cherrypy.quickstart(server.Server(chainManager))

def threadServer():
    thread = Thread(target=startServer, args=())
    thread.setDaemon(True)
    thread.start()

def startMiner():
    minerD.mining = True
    minerD.mine()

def threadMiner():
    thread = Thread(target=startMiner, args=())
    thread.setDaemon(True)
    thread.start()


threadServer()  # Start server in separate thread
threadMiner()

while(1):
    pass
