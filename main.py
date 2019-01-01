from threading import Thread
import cherrypy
import server
import blockchain
import miner
import database


chain = blockchain.Blockchain()
minerD = miner.Miner(chain)

sflag = False

def loadConfig():
    print()

def startServer():
    cherrypy.quickstart(server.Server(chain))

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


loadConfig()
threadServer()
threadMiner()

db = database.Database()

a = ""

while(sflag == False):
    a = input("> ")
    if(a == "c"):
        sflag == True
        minerD.mining = False
        print("stop")
