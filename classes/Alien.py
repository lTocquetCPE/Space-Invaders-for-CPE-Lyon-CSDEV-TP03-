"""
Alien.py

class describing the Alien game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from PIL import Image
from classes.Sprite import Sprite
import random

class Alien () :
    def __init__(self, Alientype,position):
        self.Alientype = Alientype  
        self.speed = 0

        #variable for invaders move
        self.frameCounter = 0
        self.nbFrame=15
        self.moveCounter=10
        self.direction = 1
        self.deltax=8
        self.deltay=10

        #death management
        self.deathFramesNumber = 10
        self.isDead = False
        self.deathFrameCounter = 0


        #animation management
        self.animationFrameNumber = 0 #2 frames animation, can be 0 or 1
        self.lazerSpeed = 8


        #set general invader position
        #specific position is defined on GameState
        if self.Alientype == "Squid" : #Small Invader
            self.pos = [position[0]+50,position[1]+50]       #position on canvas
            self.sprite = Sprite("./ressources/SpriteSheet.png", self.pos, [0,0],[11,8],3)
        elif self.Alientype == "Crab" : #Medium Invader
            self.pos = [position[0]+50,position[1]+100]
            self.sprite = Sprite("./ressources/SpriteSheet.png", self.pos, [12,0],[13,8],3)
        else : #type=="Octopus"   Large Invader
            self.pos = [position[0]+50,position[1]+200]
            self.sprite = Sprite("./ressources/SpriteSheet.png", self.pos, [25,0],[14,8],3)
        self.countPosY=self.pos[1]

        #shooting management
        self.lazerSprite = Sprite("./ressources/SpriteSheet.png", self.pos, [random.randint(0, 11)*3,21],[3,7], 3)
        self.lazerDisplay = False
        self.shootProba = 180

        #set explosion sprite sheet
        self.explosionSprite = Sprite("./ressources/SpriteSheet.png", self.pos, [40,0],[15,8],3)

        
    #Entity drawing
    def draw (self, gameCanvas):
        self.sprite.draw(gameCanvas)
        if self.lazerDisplay :
            self.lazerSprite.draw(gameCanvas)

    #handles the alien shooting
    def shoot(self):
        if self.lazerDisplay == False:
            self.lazerDisplay = True
            self.lazerSprite.pos = (self.sprite.pos[0] + 12, self.sprite.pos[1])

    #Checks for the alien going offscreen and calls the other aliens to change direction
    def manageScreenLimits(self, gameState):
        if self.frameCounter>=self.nbFrame:
            if self.sprite.pos[0] + self.direction*self.deltax >= 760 or self.sprite.pos[0] + self.direction*self.deltax <=10:
                for al in gameState.listAlien:
                    al.changeDirection()

    #gameloop logic of the entity
    def manageEntity(self, gameState):
        if not self.isDead:

            #Alien Speed:
            if len(gameState.listAlien) <= 10 :
                self.nbFrame = 12
            if len(gameState.listAlien) <= 5 :
                self.nbFrame = 7
            if len(gameState.listAlien) <= 1 :
                self.nbFrame = 1

        if not self.isDead and gameState.state!='lose':#ODDITY THERE
            #Movement
            if self.frameCounter >= self.nbFrame:
                self.move(self.direction*self.deltax,0)
                self.frameCounter=0
            self.frameCounter+=1

            #lose game when alien touch barrier
            if self.countPosY>=375 :
                gameState.state='lose'

            if random.randint(0, self.shootProba - 1)  == 0:
                self.shoot()

            if self.lazerDisplay :
                if self.lazerSprite.pos[1] + self.lazerSpeed < 800:
                    self.lazerSprite.pos = (self.lazerSprite.pos[0] , self.lazerSprite.pos[1] + self.lazerSpeed)
                else: 
                    self.lazerDisplay = False
           

        else :
            if self.deathFrameCounter >= self.deathFramesNumber:
                gameState.listAlien.remove(self)
            self.deathFrameCounter += 1

    #Makes the alien move
    def move (self, deltax, deltay):
        
        self.sprite.pos=(self.sprite.pos[0]+deltax , self.sprite.pos[1]+deltay)

         #animation
        self.animationFrameNumber +=1
        self.animationFrameNumber = self.animationFrameNumber %2
        
        spriteSheetPosChange = 8
        if self.animationFrameNumber == 0 :
            spriteSheetPosChange = -1 * spriteSheetPosChange
        
  
        self.sprite.setSpriteSheetPos((self.sprite.cropPos[0], self.sprite.cropPos[1] + spriteSheetPosChange), (self.sprite.cropSize[0], self.sprite.cropSize[1]))
   
    #Called when an alien finds that he hit a screen side
    def changeDirection(self):
        self.direction *= -1 
        self.move(0,self.deltay)

    #Called when an alien should die (Projetile/Alien colision)
    def death (self, gameState):
        prevSpritePos = self.sprite.pos
        self.sprite = self.explosionSprite
        self.sprite.pos = prevSpritePos
        self.isDead = True
        gameState.score+=10
        
