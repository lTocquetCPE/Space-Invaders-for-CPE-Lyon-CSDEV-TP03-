"""
Alien.py

class describing the Alien game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from PIL import Image
from AnimatedSprite import AnimatedSprite
class Alien () :
    def __init__(self, Alientype):
        self.type = Alientype
        self.speed = 0

    def manageType (self, type):
        #TO DO set all attribut
        if type == "Squid" : #Small Invader
            #TO DO reset next attribut
            self.pos = [0,0]                #position on canvas
            self.spriteSheetPos = [0,0]     # alien image on sprite sheet
            self.spriteSize =[50,50]        #size of image we want
        elif type == "Crab" : #Medium Invader
            self.pos = [0,0]
            self.spriteSheetPos = [0,0]
            self.spriteSize = [50,50] 
        else : #type=="Octopus"   Large Invader
            self.pos = [0,0]
            self.spriteSheetPos = [0,0]
            self.spriteSize = [50,50] 

    def setSprite (self):
        createSprite=AnimatedSprite()
        createSprite=AnimatedSprite()
        createSprite.setSpriteSheetPos(spriteSheetPos, cropSize)
        createSprite.setSpriteSize(size, [10,10])
        self.sprite = createSprite.tempImg

