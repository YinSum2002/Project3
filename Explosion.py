from tkinter import *
import math,time,random
import numpy as np
from Dot import Dot


class Explosion:
    def __init__(self, canvas, max_radius = 80, color = "rainbow"):
        self.dots = 15
        self.dotlist = []
        self._active = False
        self.canvas = canvas
        self.max_radius = max_radius
        self.color = color

    def activate(self, x, y):
        self.x = x
        self.y = y
        self.r = 0
        self._active = True

    def is_active(self):
        return self._active

    def next(self):
        if self.is_active() == True:
            if self.r < self.max_radius:
                self.r += 1

                for i in range(self.dots):
                    d = random.randint(0,359)
                    theta = math.pi * d/180
                    x = self.x + self.r * math.cos(theta)
                    y = self.y + self.r * math.sin(theta)
                    dot = Dot(self.canvas, x, y, self.color)
                    self.dotlist.append(dot)
            else:
                self.deactivate()

    def deactivate(self):
        self._active = False
        for dot in self.dotlist:
            self.canvas.delete(dot.id)
        self.dotlist = []

    @staticmethod
    def add_explosion(canvas, epl_list, x, y, max_rad = 80, color = "rainbow"):
        i = len(epl_list) - 1
        while i >= 0:
            if epl_list[i].is_active() == False:
                del epl_list[i]
            i -= 1

        choice = random.randint(1,2)
        if choice == 1:
            explosion = Explosion(canvas, max_rad, color)
        else:
            explosion = Explosion_gravity(canvas, max_radius = 80, color = "rainbow")
        explosion.activate(x, y)
        epl_list.append(explosion)
        return explosion

class Explosion_gravity(Explosion):
    def __init__(self, canvas, max_radius = 80, color = "rainbow"):
        super().__init__(canvas, max_radius = 80, color="rainbow")
        self.angle = np.random.randint(0,359, size=self.dots)
        self.v = np.random.randint(1,5, size=self.dots)

    def next(self):
        if self.is_active() == True:
            if self.r < self.max_radius:
                self.r += 1
                g = -0.06
                for i in range(self.dots):
                    theta = math.pi * self.angle[i]/180
                    x = self.x + self.r * math.cos(theta) * self.v[i]
                    y = self.y + self.r * math.sin(theta) * self.v[i] - (g/2) * self.r**2
                    dot = Dot(self.canvas, x, y, self.color)
                    self.dotlist.append(dot)
            else:
                self.deactivate()








        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root,width=w,height=h,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        #Initialize list of Explosions
        booms=[]
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Explosion.add_explosion(canvas,booms,e.x,e.y) )
        
        ############################################
        ####### start simulation
        ############################################
        
        while True:
            # scan booms list and execute next time step
            for boom in booms:
                boom.next()
                
            # check active status of list of booms (for debugging)
            for b in booms:
                print(b.is_active(),end=" ")
            print()

            # update the graphic and wait time
            root.update()    #redraw
            time.sleep(0.03) #pause

        
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

