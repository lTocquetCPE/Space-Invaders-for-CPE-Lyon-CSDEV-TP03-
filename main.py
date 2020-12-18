"""
main.py

entry point for the Space Invaders Game

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from tkinter import Tk, Label, Button, Canvas

from classes.MainWindow import MainWindow
from classes.AnimatedSprite import AnimatedSprite
from funcs.gameLoop import gameLoop


mainWindow = MainWindow()

firstSprite = AnimatedSprite(mainWindow.gameCanvas, "./ressources/pikatest.png", (0,0))
gameLoop(mainWindow, None)

mainWindow.manageEvent()

mainWindow.mainloop()