"""
GameCanvas.py

class describing the elements on the game canvas. There are two "screens" the game one and the menu one.

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

from tkinter import Canvas


#Contains all the elements necessary for display
class GameCanvas(Canvas):
    def __init__(self):

        self.height = 500
        self.width = 800
        Canvas.__init__(self, width = self.width, height = self.height)


        
    
    #TODO updates everything on the canvas (calls a special function in each element)
    def updateCanvas(self, gameState):
        self.delete('all')
        gameState.canon.draw(self)
        for alien in gameState.listAlien :
            alien.draw(self)
        


