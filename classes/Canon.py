"""
Canon.py

class describing the Canon game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
TODO shoots the right sprite
"""
from classes.Sprite import Sprite
from classes.Projectile import Projectile

class KeyboardInfoCanon():
  def __init__(self):
    self.isRightPressed = False
    self.isLeftPressed = False
    self.isSpacePressed = False

class Canon ():
    def __init__(self):
      self.sprite = Sprite("./ressources/SpriteSheet.png", (215 , 450),(56, 0), (16, 10), 2)
      self.speed = 25
      self.keyboardInfoCanon = KeyboardInfoCanon()
      self.shootFrameCounter = 15
      self.shootEveryNFrames = 15

    #Function called in the game Loop. Contains all the things needed to be done each frame
    def manageEntity(self, gameState):
      if self.keyboardInfoCanon.isRightPressed:
          self.move("RIGHT")
      if self.keyboardInfoCanon.isLeftPressed:
          self.move("LEFT")
      if self.keyboardInfoCanon.isSpacePressed:
          if self.shootFrameCounter == self.shootEveryNFrames:
            self.shoot(gameState)
            self.shootFrameCounter = 0
          self.shootFrameCounter += 1    

    #Function called by keyboard events. Updates the keyboardInfoCanon
    def handleKeyboardEvent(self, keycode, eventType):
      newValue = False
      if eventType == "KEY_PRESS":
        newValue = True
      if keycode == 114:
        self.keyboardInfoCanon.isRightPressed = newValue
      elif keycode == 113:
        self.keyboardInfoCanon.isLeftPressed = newValue
      elif keycode == 65:
        self.keyboardInfoCanon.isSpacePressed = newValue
      
   

    #Updates canon position
    def move (self, direction):

      if direction == "RIGHT": 
            if self.sprite.pos[0] + self.speed < 780:
              self.sprite.pos = (self.sprite.pos[0] + self.speed, self.sprite.pos[1])
      elif direction =="LEFT":
          if self.sprite.pos[0] - self.speed >= 0:
            self.sprite.pos = (self.sprite.pos[0] - self.speed, self.sprite.pos[1])
        
    #Handles projectile display
    def shoot(self, gameState):
      projectile = Projectile(self.sprite.pos[0] + 9)
      gameState.listProjectiles.append(projectile)

      

    def draw(self, gameCanvas):
      self.sprite.setSpriteScale(2)#Weird workaround, the sprite scale is reset to 1 and I can't find where
      self.sprite.draw(gameCanvas)

