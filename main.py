"""
main.py

entry point for the Space Invaders Game

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""
from tkinter import Tk, Label, Button, Canvas

from classes.MainWindow import MainWindow
from funcs.gameLoop import gameLoop


mainWindow = MainWindow()

gameLoop(mainWindow, None)

mainWindow.mainloop()
