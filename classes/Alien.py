"""
Alien.py

class describing the Alien game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from PIL import Image
from classes.AnimatedSprite import AnimatedSprite

class Alien () :
    def __init__(self, Alientype):
        self.Alientype = Alientype
        self.speed = 0

        #TO DO set all attribut
        if self.Alientype == "Squid" : #Small Invader
            #TO DO reset next attribut
            self.pos = [50,50]                #position on canvas
            self.SpriteSheet = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [0,0],[11,8],5)
        elif self.Alientype == "Crab" : #Medium Invader
            self.pos = [50,100]
            self.SpriteSheet = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [12,0],[13,8],5)
        else : #type=="Octopus"   Large Invader
            self.pos = [50,200]
            self.SpriteSheet = AnimatedSprite("./ressources/SpriteSheet.png", self.pos, [25,0],[14,8],5)


    def setSprite (self):
        #createSprite=AnimatedSprite()
        #createSprite.setSpriteSheetPos(spriteSheetPos, cropSize)
        #createSprite.setSpriteSize(size, [10,10])
        #self.sprite = createSprite.tempImg
        return 0 #juste parce que tout est commentççà

    def draw (self, gameCanvas):
        self.SpriteSheet.draw(gameCanvas)
