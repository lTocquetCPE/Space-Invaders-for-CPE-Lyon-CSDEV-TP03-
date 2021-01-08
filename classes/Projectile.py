

class Projectile():
  def __init__(self, initXPos):
    
    self.initXPos = initXPos
    self.speed = 1
    self.sprite = AnimatedSprite("./ressources/SpriteSheet.png", (330 ,900),(56, 0), (16, 10), 5)

  def handleEntity(self):
    

  def draw(self):
    self.sprite.draw()