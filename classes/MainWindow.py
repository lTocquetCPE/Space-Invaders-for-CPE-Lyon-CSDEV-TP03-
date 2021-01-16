"""
MainWindow.py

Class describing the widgets in the game window

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
TODO disable window
"""

from tkinter import Tk, Label, Button, Canvas
from classes.GameCanvas import GameCanvas

class MainWindow(Tk) :
    #init manages the layout of the window
    def __init__(self, gameState):
        Tk.__init__(self)

        #window option
        self.title("Space Invader")

        #widget
        self.gameCanvas = GameCanvas()
        self.gameButton = Button(self, text="New Game",command=gameState.startNewGame, bg='black', font='terminal', fg='white',relief='flat')
        self.quitButton = Button(self, text="Quit", command=self.destroy, bg='black', font='terminal', fg='white',relief='flat')

        #pack
        self.gameCanvas.pack()
        self.gameButton.place(x=4,y=465)
        self.quitButton.place(x=728,y=465)

    #detect board click and add keycode to function 
    def manageEvent (self, gameState):
        self.bind('<KeyPress>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_PRESS"))
        self.bind('<KeyRelease>', lambda event : gameState.canon.handleKeyboardEvent(event.keysym, "KEY_RELEASE"))
    
