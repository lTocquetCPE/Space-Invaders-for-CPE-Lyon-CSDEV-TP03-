"""
Sprite.py

class describing sprites to be used in our game. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from PIL import ImageTk, Image
from tkinter import PhotoImage
#class managing the sprites, their position and animations
class Sprite():
  def __init__(self, path, initPos, spriteSheetPos, size, scale):
    
    self.path = path
    self.pos = initPos
    self.id = 0 #Default

    #Image management
    self.imgPIL = Image.open(path) #Original image
    self.tempImg = self.imgPIL  #temporary image that can be cropped, resized and other
    self.img = None #keeps the image ref
    self.cropPos = spriteSheetPos#Default
    self.cropSize = size #Default
    self.scale = scale


    self.spriteSheetPos = spriteSheetPos
    self.size = size
    self.setSpriteScale(self.scale)
    self.setSpriteSheetPos(self.spriteSheetPos, self.size)
    




  #Chooses which part of the spritesheet should be displayed (SpriteSheet chosen to do the alien two frame animation)
  def setSpriteSheetPos(self, pos, cropSize):
    self.tempImg = self.imgPIL.crop((pos[0], pos[1], pos[0] + cropSize[0], pos[1] + cropSize[1]))
    self.cropPos = pos
    self.cropSize = cropSize
    self.setSpriteScale(self.scale)
    
  #Manages the sprite scale when displayed
  def setSpriteScale(self, scale):
    self.scale = scale
    newSize = (self.size[0]*self.scale, self.size[1]* self.scale)
    self.tempImg = self.tempImg.resize(newSize, resample = Image.NEAREST)

  #Sprite drawing
  def draw(self, gameCanvas):
      self.img = ImageTk.PhotoImage(self.tempImg)
      self.id = gameCanvas.create_image(self.pos[0],self.pos[1], image=self.img, anchor="nw")

      
