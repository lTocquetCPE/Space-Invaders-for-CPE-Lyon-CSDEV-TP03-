"""
AnimatedSprite.py

class describing sprites to be used in our game. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from tkinter import PhotoImage
#class managing the sprites, their position and animations
class AnimatedSprite():
  def __init__(self, gameCanvas, path, initPos, scale=1):
    self.path = path

    self.img = PhotoImage(file=path)
    self.sprite = gameCanvas.create_image(initPos[0], initPos[1], image=self.img)