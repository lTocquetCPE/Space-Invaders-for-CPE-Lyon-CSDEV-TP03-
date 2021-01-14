"""
Barrier.py

class describing the barrier game entity

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from classes.Sprite import Sprite

class Barrier():
  def __init__(self, pos):
    self.sprite = Sprite("./ressources/SpriteSheet.png", pos,(0, 30), (23, 16), 3)


  def draw(self, gameCanvas):
    self.sprite.draw(gameCanvas)