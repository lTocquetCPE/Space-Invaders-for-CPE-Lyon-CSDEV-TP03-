
"""
Canon.py

class describing the projectile shooted by the canon. 

8/01/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
TODO collisions with entities
"""

from classes.Sprite import Sprite

class Projectile():
  def __init__(self, initXPos):
    
    self.initXPos = initXPos
    self.speed = 8
    self.sprite = Sprite("./ressources/SpriteSheet.png", (self.initXPos ,440),(20, 25), (3, 7), 2)

  #Function called in gameLoop, makes the projectile move and deletes in when not displayed
  def manageEntity(self, gameState):
    if self.sprite.pos[1] - self.speed > 0:
      self.sprite.pos = (self.sprite.pos[0] , self.sprite.pos[1] - self.speed)
    else :
      gameState.listProjectiles.remove(self)

  def removeProjectile(self, gameState):
    gameState.listProjectiles.remove(self)

  def draw(self, gameCanvas):
    self.sprite.draw(gameCanvas)