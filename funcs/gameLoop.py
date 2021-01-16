"""
gameLoop.py

Function managing the game and drawing loop

18/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from funcs.collisionFuncs import projectileCollisionsBarrier, projectileCollisionsAlien, lazerCollisionsBarrier, lazerCollisionsCanon
from classes.GameState import GameState

framesPerSecond = 30

 
def nextLevel(mainWindow, gameState):
  if gameState.level < 3:
    gameState.startNewGame(gameState.level, gameState.score)

def gameLoop(mainWindow, gameState):

  #GAME LOGIC
  gameState.canon.manageEntity(gameState)

  for alien in gameState.listAlien :
    alien.manageScreenLimits(gameState)

  for alien in gameState.listAlien :
    alien.manageEntity(gameState)

  for proj in gameState.listProjectiles:
    proj.manageEntity(gameState)

  projectileCollisionsBarrier(mainWindow, gameState)
  projectileCollisionsAlien(mainWindow, gameState)
  lazerCollisionsBarrier(mainWindow, gameState)
  lazerCollisionsCanon(mainWindow, gameState)



  #winning condition
  if gameState.state == "started":
    if len(gameState.listAlien) == 0:
      gameState.state = "win"
      mainWindow.after(3000, lambda: nextLevel(mainWindow, gameState))



  #DISPLAYING STUFF
  mainWindow.gameCanvas.updateCanvas(gameState)

  #TODO condition to stop the gameLoop
  mainWindow.after(int(1000/framesPerSecond), lambda: gameLoop (mainWindow, gameState))
  
