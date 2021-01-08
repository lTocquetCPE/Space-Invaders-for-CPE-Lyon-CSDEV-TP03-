"""
GameState.py

class containing all the game variables necessary for the game to work

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from classes.Canon import Canon
from classes.Alien import Alien

class GameState() :
    #init game variable
    def __init__(self):

        self.gameState="off"
        self.nbLives=3
        self.score=0
        self.canon = Canon()
        self.listAlien=[]
        for i in range(12):   #generalisation with n variable for switch between level (level 1 => 5, level 2 => 9, level 3 => 12)
            self.listAlien.append(Alien("Squid",[52*i,0]))
            self.listAlien.append(Alien("Crab",[52*i,0]))
            self.listAlien.append(Alien("Crab",[52*i,50]))
            self.listAlien.append(Alien("Octopus",[52*i,0]))
            self.listAlien.append(Alien("Octopus",[52*i,50]))

