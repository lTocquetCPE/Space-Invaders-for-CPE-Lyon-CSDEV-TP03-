"""
Canon.py

class describing the Canon game entity. 

17/12/20 by Loïc (Pyrrha) TOCQUET and MALOSSE Alice
"""

class Canon ():
    def __init__(self):
        self.position=[0, 0] #TO DO redefine position

    #Move canon : right and left
    def move (self, keycode):
        if keycode=="39" : #right
            #TO DO add condition if x=max, don't change position
            self.position[0] += 1
        elif keycode=="37" and self.position[0]!=0 : #left
            self.position [0] -= 1

    #def shoot (self) :
        