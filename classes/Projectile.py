
"""
Canon.py

class describing the projectile shooted by the canon. 

8/01/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
TODO collisions with entities
"""

from classes.AnimatedSprite import AnimatedSprite

class Projectile():
  def __init__(self, initXPos):
    
    self.initXPos = initXPos
    self.speed = 8
    self.sprite = AnimatedSprite("./ressources/SpriteSheet.png", (self.initXPos ,440),(20, 25), (3, 7), 2)

  def manageEntity(self, gameState):
    self.sprite.pos = (self.sprite.pos[0] , self.sprite.pos[1] - self.speed)

  def draw(self, gameCanvas):
    self.sprite.draw(gameCanvas)