"""
GameState.py

class containing all the game variables necessary for the game to work

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from classes.Canon import Canon

class GameState() :
    #init game variable
    def __init__(self):

        self.gameState="off"
        self.nbLives=3
        self.score=0
        self.listAlien=[]
        self.canon = Canon()
