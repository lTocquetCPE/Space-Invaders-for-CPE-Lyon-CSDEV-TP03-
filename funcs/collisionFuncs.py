""""
collisionFuncs.py

file containing all the functions regarding collisions in our game

11/01/2021 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

 #Checks and handles for projectile/Alien colisions
def projectileCollisionsAlien(mainWindow, gameState):

  
    for proj in gameState.listProjectiles:
      idList = mainWindow.gameCanvas.find_overlapping(proj.sprite.pos[0], proj.sprite.pos[1], proj.sprite.pos[0] + 2, proj.sprite.pos[1] + 2)
      for alien in gameState.listAlien:
        if alien.sprite.id in idList:
          alien.death()
          proj.removeProjectile(gameState)

  #Checks and handles for projectile/Barrier colisions
def projectileCollisionsBarrier(mainWindow, gameState):

    for proj in gameState.listProjectiles:
      idList = mainWindow.gameCanvas.find_overlapping(proj.sprite.pos[0], proj.sprite.pos[1], proj.sprite.pos[0] + 2, proj.sprite.pos[1] + 2)
      for barrier in gameState.listBarrier:
        if barrier.sprite.id in idList:
          proj.removeProjectile(gameState)

#Checks and handles alien lazer/Barrier collisions
def lazerCollisionsBarrier(mainWindow, gameState):
  for alien in gameState.listAlien:
    if alien.lazerDisplay:
      idList = mainWindow.gameCanvas.find_overlapping(alien.lazerSprite.pos[0] + 2, alien.lazerSprite.pos[1], alien.lazerSprite.pos[0] + 4, alien.lazerSprite.pos[1] + 6)
      mainWindow.gameCanvas.create_rectangle(alien.lazerSprite.pos[0] + 2, alien.lazerSprite.pos[1], alien.lazerSprite.pos[0] + 6, alien.lazerSprite.pos[1] + 10, fill ="red")
      for barrier in gameState.listBarrier:
        if barrier.sprite.id in idList:
          alien.lazerDisplay = False
          barrier.takeDamage(gameState)

#Checks and handles lazer/Canon collisions
def lazerCollisionsCanon(mainWindow, gameState):
   for alien in gameState.listAlien:
    if alien.lazerDisplay:
      idList = mainWindow.gameCanvas.find_overlapping(alien.lazerSprite.pos[0] + 2, alien.lazerSprite.pos[1], alien.lazerSprite.pos[0] + 4, alien.lazerSprite.pos[1] + 6)
      mainWindow.gameCanvas.create_rectangle(alien.lazerSprite.pos[0] + 2, alien.lazerSprite.pos[1], alien.lazerSprite.pos[0] + 6, alien.lazerSprite.pos[1] + 10, fill ="red")
      if gameState.canon.sprite.id in idList:
         gameState.canon.getHit(gameState, alien)
