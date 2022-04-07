from tkinter import *
import time,random
from Explosion import Explosion
from Missile import Missile

        
       
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        
        my_image=PhotoImage(file="umass_campus.png")
        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h) # create a canvas width*height

        canvas.create_image(10,10,anchor=NW,image=my_image)
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Explosions
        booms=[]
        #Initialize list of Missiles
        missiles=[]
        

        
        ############################################
        ####### start simulation
        ############################################
      






        ### To complete







        

if __name__=="__main__":
    main()

