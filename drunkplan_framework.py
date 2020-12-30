"""
@author: Amy Jungmin Seo
email: jungmin.seo@postgrad.manchester.ac.uk

"""

import random 

class Drunk():
    
    # init-method, the constructor method for drunks
    
    def __init__(self, town, drunks, pubs, houses):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.town = town
        self.drunks = drunks
        self.pubs = pubs
        self.houses = houses
    
    
    # move the drunks
    
    def move(self):
        
        if random.randint(0,1) < 0.5:     
            self.x = self.x + 1           
        else: 
            self.x = self.x - 1
            
        if random.randint(0,1) < 0.5:
            self.y = self.y + 1
        else:         
            self.y = self.y - 1


    # steps 
    
    def steps(self):
        if self.town[self.y][self.x] > 1:
            self.town[self.y][self.x] -= 1
            self.store += 1
        
    # go home
    
    def go_home(self):
        self.x = self.row + 1
        self.y = self.col + 1
    
    
    # drunks arrived home
    
    def got_home(self, drunks):
        drunks.remove(self)