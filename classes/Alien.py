"""
Alien.py

class describing the Alien game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from PIL import Image
from classes.Sprite import Sprite

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

        #death management
        self.deathFramesNumber = 10
        self.isDead = False
        self.deathFrameCounter = 0

        #animaton management
        self.animationFrameNumber = 0 #2 frames animation, can be 0 or 1

        #set general invader position
        #specific position is define on GameState
        if self.Alientype == "Squid" : #Small Invader
            self.pos = [position[0]+50,position[1]+50]                #position on canvas
            self.sprite = Sprite("./ressources/SpriteSheet.png", self.pos, [0,0],[11,8],3)
        elif self.Alientype == "Crab" : #Medium Invader
            self.pos = [position[0]+50,position[1]+100]
            self.sprite = Sprite("./ressources/SpriteSheet.png", self.pos, [12,0],[13,8],3)
        else : #type=="Octopus"   Large Invader
            self.pos = [position[0]+50,position[1]+200]
            self.sprite = Sprite("./ressources/SpriteSheet.png", self.pos, [25,0],[14,8],3)

        #set explosion sprite sheet
        self.explosionSprite = Sprite("./ressources/SpriteSheet.png", self.pos, [40,0],[15,8],3)

    def draw (self, gameCanvas):
        self.sprite.draw(gameCanvas)


    def manageEntity(self, gameState):
        if not self.isDead:
            #Movement
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
            
           

        else :
            if self.deathFrameCounter >= self.deathFramesNumber:
                gameState.listAlien.remove(self)
            self.deathFrameCounter += 1


    def move (self, deltax, deltay):
        
        self.sprite.pos=(self.sprite.pos[0]+deltax , self.sprite.pos[1])
        self.sprite.pos=(self.sprite.pos[0], self.sprite.pos[1]+deltay)

         #animation
        self.animationFrameNumber +=1
        self.animationFrameNumber = self.animationFrameNumber %2
        
        spriteSheetPosChange = 8
        if self.animationFrameNumber == 0 :
            spriteSheetPosChange = -1 * spriteSheetPosChange
        
  
        self.sprite.setSpriteSheetPos((self.sprite.cropPos[0], self.sprite.cropPos[1] + spriteSheetPosChange), (self.sprite.cropSize[0], self.sprite.cropSize[1]))
   
    def death (self):
        prevSpritePos = self.sprite.pos
        self.sprite = self.explosionSprite
        self.sprite.pos = prevSpritePos
        self.isDead = True
        


