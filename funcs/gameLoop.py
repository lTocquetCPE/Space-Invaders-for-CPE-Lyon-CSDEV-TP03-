"""
gameLoop.py

Function managing the game and drawing loop

18/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

framesPerSecond = 60

def gameLoop(mainWindow, gameState):

  #GAME LOGIC
  gameState.canon.manageEntity(gameState)

  for alien in gameState.listAlien :
    alien.manageEntity()

  for proj in gameState.listProjectiles:
    proj.manageEntity(gameState)
  #DISPLAYING STUFF

  mainWindow.gameCanvas.updateCanvas(gameState)

  #TODO condition to stop the gameLoop
  mainWindow.after(int(1000/framesPerSecond), lambda: gameLoop (mainWindow, gameState))
  