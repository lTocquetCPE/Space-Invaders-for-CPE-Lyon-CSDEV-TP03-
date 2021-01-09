"""
gameLoop.py

Function managing the game and drawing loop

18/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

framesPerSecond = 30

  #Checks for projectile/Alien colisions
def projectileCollisions(mainWindow, gameState):
    for proj in gameState.listProjectiles:
      idList = mainWindow.gameCanvas.find_overlapping(proj.sprite.pos[0], proj.sprite.pos[1], proj.sprite.pos[0] + 2, proj.sprite.pos[1] + 2)
      for alien in gameState.listAlien:
        if alien.sprite.id in idList:
          alien.death()
          proj.removeProjectile(gameState)

def gameLoop(mainWindow, gameState):

  #GAME LOGIC
  gameState.canon.manageEntity(gameState)

  for alien in gameState.listAlien :
    alien.manageEntity(gameState)

  for proj in gameState.listProjectiles:
    proj.manageEntity(gameState)

  projectileCollisions(mainWindow, gameState)


  #DISPLAYING STUFF

  mainWindow.gameCanvas.updateCanvas(gameState)

  #TODO condition to stop the gameLoop
  mainWindow.after(int(1000/framesPerSecond), lambda: gameLoop (mainWindow, gameState))
  
