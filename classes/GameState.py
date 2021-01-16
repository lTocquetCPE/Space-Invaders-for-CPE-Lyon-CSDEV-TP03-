"""
GameState.py

class containing all the game variables necessary for the game to work

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from classes.Canon import Canon
from classes.Alien import Alien
from classes.Barrier import Barrier

class GameState() :
    #init game variable
    def __init__(self, prevLevel = 0):

        self.state="notStarted"
        self.level= prevLevel + 1
        self.nbAlien=4*self.level
        self.healthPoint = 3
        self.score=0
        self.canon = Canon()
        self.listProjectiles = []
        self.listAlien=[]
        self.listBarrier=[]
        self.alienDirection = 1 # 1 = Right      -1= Left

    #Called to start a new level or a new game
    def startNewGame(self, prevLevel=0, prevScore=0):
        self.state = "started"
        self.level= prevLevel + 1
        self.healthPoint = 3
        self.score=prevScore
        self.nbAlien=4*self.level
        self.listProjectiles = []
        self.listAlien=[]
        self.listBarrier=[]
        self.canon = Canon()

        for i in range(self.nbAlien): 
            self.listAlien.append(Alien("Squid",[(730/self.nbAlien)*i,0]))
            self.listAlien.append(Alien("Crab",[(730/self.nbAlien)*i,0]))
            self.listAlien.append(Alien("Crab",[(730/self.nbAlien)*i,50]))
            self.listAlien.append(Alien("Octopus",[(730/self.nbAlien)*i,0]))
            self.listAlien.append(Alien("Octopus",[(730/self.nbAlien)*i,50]))

        self.listBarrier.append(Barrier((100,375)))
        self.listBarrier.append(Barrier((275,375)))
        self.listBarrier.append(Barrier((450,375)))
        self.listBarrier.append(Barrier((631,375)))



