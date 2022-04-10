from tkinter import *
import math,time,random
from Dot import Dot


class Explosion:
    def __init__(self, canvas, max_radius = 80, color = "rainbow"):
        self.dots = 15
        self.dotlist = []
        self.__active = False
        self.canvas = canvas
        self.max_radius = max_radius
        self.color = color

    def activate(self, x, y):
        self.x = x #I suspect x and y might actually turn out to be something different
        self.y = y
        self.r = 0
        self.__active = True

    @staticmethod
    def add_explosion(canvas,booms,x,y):
        pass
    def __next__(self):
        if self.__active == True:
            self.r += 1












        
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

