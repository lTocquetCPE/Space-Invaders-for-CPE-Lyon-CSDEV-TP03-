"""
main.py

entry point for the Space Invaders Game

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from tkinter import Tk, Label, Button, Canvas

from classes.MainWindow import MainWindow
from classes.AnimatedSprite import AnimatedSprite
from classes.Alien import Alien
from funcs.gameLoop import gameLoop


mainWindow = MainWindow()

#firstSprite = AnimatedSprite(mainWindow.gameCanvas, "./ressources/SpriteSheet.png", (0,0), (12, 8))
#firstSprite.setSpriteSheetPos(mainWindow.gameCanvas, (0,0), (20,20))
#gameLoop(mainWindow, None)

Alien1=Alien(Squid)
Alien1.manageType()
Alien1.setSprite()

mainWindow.manageEvent()

mainWindow.mainloop()