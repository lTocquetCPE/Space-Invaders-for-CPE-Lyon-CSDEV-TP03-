"""
MainWindow.py

Class describing the widgets in the game window

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from tkinter import Tk, Label, Button, Canvas
from classes.GameCanvas import GameCanvas

class MainWindow(Tk) :
    #init manages the layout of the window
    def __init__(self):
        Tk.__init__(self)

        #window option
        self.title("Space Invader")

        #widget
        self.gameCanvas = GameCanvas()
        self.gameButton = Button(self, text="New Game") #to do add command to start a new game
        self.quitButton = Button(self, text="Quit", command=self.destroy)
        self.currentScoreLabel = Label(self, text="Score :") # to do add score
        self.currentLivesLabel = Label(self, text="Lives :") #to do add lives

        #pack
        self.gameCanvas.pack()
        self.gameButton.pack()
        self.quitButton.pack()
        self.currentScoreLabel.pack()
        self.currentLivesLabel.pack()

    #detect board click and add keycode to function 
    def manageEvent (self, gameState):
        self.bind('<KeyPress>', lambda event : gameState.canon.handleKeyboardEvent(event.keycode, "KEY_PRESS"))
        self.bind('<KeyRelease>', lambda event : gameState.canon.handleKeyboardEvent(event.keycode, "KEY_RELEASE"))
    
