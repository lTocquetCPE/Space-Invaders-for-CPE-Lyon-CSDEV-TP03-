"""
gameLoop.py

Function managing the game and drawing loop

18/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

framesPerSecond = 30

def gameLoop(window, gameState):

  #GAME LOGIC
  print("Welcome to the gameLoop")
  #DISPLAYING STUFF


  #TODO condition to stop the gameLoop
  window.after(int(1000/framesPerSecond), lambda: gameLoop ())
  