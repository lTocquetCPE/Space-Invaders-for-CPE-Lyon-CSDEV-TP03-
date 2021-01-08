"""
main.py

entry point for the Space Invaders Game

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from tkinter import Tk, Label, Button, Canvas

from classes.MainWindow import MainWindow
from classes.AnimatedSprite import AnimatedSprite
from classes.GameState import GameState
from funcs.gameLoop import gameLoop


mainWindow = MainWindow()
gameState = GameState()
gameState.canon.sprite.setSpriteScale(1)
gameLoop(mainWindow, gameState)

mainWindow.manageEvent(gameState)

mainWindow.mainloop()