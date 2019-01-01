import threading
from threading import Thread
import cherrypy
import server
import blockchain
import miner
import database

screen_lock = threading.Semaphore()

db = database.Database()
chain = blockchain.Blockchain(db)
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

def startCLI():
    print()

def threadCLI():
    print()


loadConfig()
threadServer()
threadMiner()

a = ""

while(sflag == False):
    screen_lock.acquire()
    a = input("> ")
    screen_lock.release()
    if(a == "c"):
        sflag == True
        minerD.mining = False
        print("stop")
