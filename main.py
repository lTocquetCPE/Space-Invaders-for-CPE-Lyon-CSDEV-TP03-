"""
main.py

entry point for the Space Invaders Game

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from tkinter import Tk, Label, Button, Canvas

from classes.MainWindow import MainWindow
from classes.AnimatedSprite import AnimatedSprite
from classes.GameState import GameState
from classes.Alien import Alien
from funcs.gameLoop import gameLoop


mainWindow = MainWindow()
gameState = GameState()
gameState.canon.sprite.setSpriteScale(1)
gameLoop(mainWindow, gameState)


#firstSprite = AnimatedSprite(mainWindow.gameCanvas, "./ressources/SpriteSheet.png", (0,0), (12, 8))
#firstSprite.setSpriteSheetPos(mainWindow.gameCanvas, (0,0), (20,20))
#gameLoop(mainWindow, None)

Alien1=Alien("Squid")
Alien1.setSprite()
mainWindow.manageEvent(gameState)
mainWindow.mainloop()