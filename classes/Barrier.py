"""
Barrier.py

class describing the barrier game entity

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from classes.Sprite import Sprite
from PIL import Image
class Barrier():
  def __init__(self, pos):
    self.sprite = Sprite("./ressources/SpriteSheet.png", pos,(0, 30), (23, 16), 3)
    
    self.HP = 10
    self.HPMax = 10

  def draw(self, gameCanvas):
    self.sprite.draw(gameCanvas)

  #becomes redder and redder each damage till destruction
  def takeDamage(self, gameState):
    self.HP -= 1
    if self.HP == 0:
      gameState.listBarrier.remove(self)

    #Color management
    rgbaIMG = self.sprite.tempImg.convert("RGB")

    r, g, b = rgbaIMG.split()

    g = g.point(lambda i: i - ((1/self.HPMax)*255))
    b = b.point(lambda i: i - ((1/self.HPMax)*255))

    self.sprite.tempImg = Image.merge('RGB', (r, g, b))


