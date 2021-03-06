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
        Canvas.__init__(self, width = self.width, height = self.height , bg="black")

        
    #Main drawing function. Calls all the other entity related draw function
    def updateCanvas(self, gameState):
        self.delete('all')
        gameState.canon.draw(self)
        for alien in gameState.listAlien :
            alien.draw(self)
        for projectile in gameState.listProjectiles:
            projectile.draw(self)
        for barrier in gameState.listBarrier:
            barrier.draw(self)

        self.level=str(gameState.level)
        self.textlevel=self.create_text(50,25,text='LV'+self.level, fill='white', font='terminal')

        self.score=str(gameState.score)
        self.textscore=self.create_text(150,25,text='Score : '+self.score, fill='white', font='terminal')

        self.lives=str(gameState.healthPoint)
        self.textlives=self.create_text(725,25,text='Lives '+self.lives, fill='white', font='terminal')

        if gameState.state=='notStarted':
            self.textTitle=self.create_text(400,190,text='SPACE', fill='yellow', font=('terminal',90))
            self.textTitle=self.create_text(400,310,text='INVADERS', fill='yellow', font=('terminal',90))

        if gameState.state=='lose':
            self.textGameOver=self.create_text(400,250,text='GAME OVER', fill='red', font=('terminal',100))

        if gameState.state == "win":
            self.winText=self.create_text(400,250,text='YOU WON !', fill='white', font=('terminal',100))


        
        


