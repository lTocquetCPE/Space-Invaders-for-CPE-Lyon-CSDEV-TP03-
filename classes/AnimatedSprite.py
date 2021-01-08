"""
AnimatedSprite.py

class describing sprites to be used in our game. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from PIL import ImageTk, Image
from tkinter import PhotoImage
#class managing the sprites, their position and animations
class AnimatedSprite():
  def __init__(self, path, initPos, spriteSheetPos, size, scale):
    
    self.path = path
    self.pos = initPos

   

    #Image management
    self.imgPIL = Image.open(path) #Original image
    self.tempImg = self.imgPIL  #temporary image that can be cropped, resized and other
    self.img = None #keeps the image ref

    

    self.spriteSheetPos = spriteSheetPos
    self.size = size
    self.setSpriteSheetPos(self.spriteSheetPos, self.size)


    self.scale = scale
    self.setSpriteScale(scale)


  def setSpriteSheetPos(self, pos, cropSize):
    self.tempImg = self.imgPIL.crop((pos[0], pos[1], pos[0] + cropSize[0], pos[1] + cropSize[1]))
    
    
  def setSpriteScale(self, scale):
    self.scale = scale
    self.size = (self.size[0]*self.scale, self.size[1]* self.scale)
    self.tempImg = self.tempImg.resize(self.size, resample = Image.NEAREST)

  def draw(self, gameCanvas):
      self.img = ImageTk.PhotoImage(self.tempImg)
      gameCanvas.create_image(self.pos[0], self.pos[1], image=self.img, anchor="nw")
      
