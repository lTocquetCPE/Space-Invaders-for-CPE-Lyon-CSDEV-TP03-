"""
Alien.py

class describing the Alien game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from PIL import Image
from classes.AnimatedSprite import AnimatedSprite

class Alien () :
    def __init__(self, Alientype,position):
        self.Alientype = Alientype  
        self.speed = 0

        #variable for invaders move
        self.frameCounter = 0
        self.nbFrame=15
        self.moveCounter=10
        self.deltax=8
        self.deltay=10

        #set general invader position
        #specific position is define on GameState
        if self.Alientype == "Squid" : #Small Invader
            self.pos = [position[0]+50,position[1]+50]                #position on canvas
            self.SpriteSheet = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [0,0],[11,8],3)
        elif self.Alientype == "Crab" : #Medium Invader
            self.pos = [position[0]+50,position[1]+100]
            self.SpriteSheet = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [12,0],[13,8],3)
        else : #type=="Octopus"   Large Invader
            self.pos = [position[0]+50,position[1]+200]
            self.SpriteSheet = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [25,0],[14,8],3)

        #set explosion sprite sheet
        self.explosionSprite = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [40,0],[15,8],3)

    def draw (self, gameCanvas):
        self.SpriteSheet.draw(gameCanvas)

    def manageEntity(self):
        if self.frameCounter==self.nbFrame and self.moveCounter!=0:
            self.move(self.deltax,0)
            self.frameCounter=0
            self.moveCounter-=1
        elif self.frameCounter==self.nbFrame and self.moveCounter==0:
            self.moveCounter=10
            self.deltax=-1*self.deltax
            self.move(0,self.deltay)
            self.frameCounter=0
        self.frameCounter+=1

    def move (self, deltax, deltay):
        self.SpriteSheet.pos=(self.SpriteSheet.pos[0]+deltax , self.SpriteSheet.pos[1])
        self.SpriteSheet.pos=(self.SpriteSheet.pos[0], self.SpriteSheet.pos[1]+deltay)

    def death (self):
        self.SpriteSheet = self.explosionSprite
        


