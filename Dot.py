########################
## Team Members
## Name1:         
## Name2:
#########################

from tkinter import *
import random


class Dot:
        def __init__(self, canvas, x, y, color, display=False):
                self.canvas = canvas
                self.x = x
                self.y = y
                items = ["red", "green", "blue", "yellow", "white", "orange", "purple"]
                if color == "rainbow":
                        self.color = random.choice(items)
                else:
                        self.color = color
                self.id = canvas.create_oval(self.x-1,self.y-1,self.x+1,self.y+1, fill = self.color, outline = self.color)
                if display == True:
                        print(self.x, self.y, self.color)








        
#################################################################
#################################################################
    
def main(): 

        ##### create a window, canvas
        root = Tk() # instantiate a tkinter window
        canvas = Canvas(root,width=800,height=1000,bg="black") # create a canvas width*height
        canvas.pack()
        root.update()   # update the graphic
        
        
        # Tkinter binding action (mouse click)
        root.bind("<Button-1>",lambda e:Dot(canvas,e.x,e.y,"rainbow",True))
        root.bind("<Button-2>", lambda e: Dot(canvas, e.x, e.y, "red", True))
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

