"""
Canon.py

class describing the Canon game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from classes.AnimatedSprite import AnimatedSprite

class KeyboardInfoCanon():
  def __init__(self):
    self.isRightPressed = False
    self.isLeftPressed = False
    self.isSpacePressed = False

class Canon ():
    def __init__(self):
      self.sprite = AnimatedSprite("./ressources/SpriteSheet.png", (215 , 450),(56, 0), (16, 10), 2)
      self.speed = 25
      self.keyboardInfoCanon = KeyboardInfoCanon()
      self.shootFrameCounter = 0
      self.shootEveryNFrames = 15

    #Function called in the game Loop. Contains all the things needed to be done each frame
    def manageEntity(self):
      if self.keyboardInfoCanon.isRightPressed:
          self.move("RIGHT")
      if self.keyboardInfoCanon.isLeftPressed:
          self.move("LEFT")
      if self.keyboardInfoCanon.isSpacePressed:
          if self.shootFrameCounter == self.shootEveryNFrames:
            self.shoot()
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
            #TODO add condition if x=max, don't change position
            self.sprite.pos = (self.sprite.pos[0] + self.speed, self.sprite.pos[1])
      elif direction =="LEFT":
            self.sprite.pos = (self.sprite.pos[0] - self.speed, self.sprite.pos[1])
        

    def shoot(self):
      print("shoot")

    def draw(self, gameCanvas):
      self.sprite.draw(gameCanvas)
