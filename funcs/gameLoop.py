"""
gameLoop.py

Function managing the game and drawing loop

18/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from funcs.collisionFuncs import projectileCollisionsBarrier, projectileCollisionsAlien, lazerCollisionsBarrier, lazerCollisionsCanon

framesPerSecond = 30

 

def gameLoop(mainWindow, gameState):

  #GAME LOGIC
  gameState.canon.manageEntity(gameState)

  for alien in gameState.listAlien :
    alien.manageEntity(gameState)

  for proj in gameState.listProjectiles:
    proj.manageEntity(gameState)

  projectileCollisionsBarrier(mainWindow, gameState)
  projectileCollisionsAlien(mainWindow, gameState)
  lazerCollisionsBarrier(mainWindow, gameState)
  lazerCollisionsCanon(mainWindow, gameState)


  #DISPLAYING STUFF
  mainWindow.currentLivesLabel["text"] = "Lives : " + str(gameState.healthPoint)

  mainWindow.gameCanvas.updateCanvas(gameState)

  #TODO condition to stop the gameLoop
  mainWindow.after(int(1000/framesPerSecond), lambda: gameLoop (mainWindow, gameState))
  
