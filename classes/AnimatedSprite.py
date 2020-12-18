"""
AnimatedSprite.py

class describing sprites to be used in our game. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from PIL import ImageTk, Image
from tkinter import PhotoImage
#class managing the sprites, their position and animations
class AnimatedSprite():
  def __init__(self, path, initPos, spriteSheetPos, size, scale=1):
    
    self.path = path
    self.pos = initPos

   

    #Image management
    self.imgPIL = Image.open(path) #Original image
    self.tempImg = self.imgPIL  #temporary image that can be cropped, resized and other
    self.img = ImageTk.PhotoImage(self.imgPIL) #image used in create_image

    

    self.spriteSheetPos = (0, 0)
    self.size = size
    self.setSpriteSheetPos(self.spriteSheetPos, self.size)


    self.scale = scale
    self.setSpriteSize(scale)


  def setSpriteSheetPos(self, pos, cropSize):
    self.tempImg = self.imgPIL.crop((pos[0], pos[1],cropSize[0], cropSize[1]))
    
    
  def setSpriteSize(self, size,cropSize, sizeMultiplier=10):
    self.size = (cropSize[0]*sizeMultiplier, cropSize[1]* sizeMultiplier)
    self.tempImg = self.tempImg.resize(self.size, resample = Image.NEAREST)

  def draw(self, gameCanvas):
    if self.sprite == None:
      self.sprite = None gameCanvas.create_image(self.pos[0], self.pos[1], image=self.img, anchor="nw")
    else:
      self.img = ImageTk.PhotoImage(self.tempImg)
      gameCanvas.itemconfig(self.sprite, image= self.img)
