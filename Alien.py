from tkinter import *
import math
import time, random

class Alien:
    ### to complete
        
################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,c):
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()
        # contstructor to complete

    # to complete
        


###############################################################
###############################################################

class Alien_green(Alien_red):

    # to complete


###############################################################
###############################################################
                


class Alien_blue(Alien_red):


    # to complete




###############################################################
################################################################
def shoot(alien,x,y):
    if alien.is_shot(x,y):
        result="hit!"
    else:
        result="miss!"
    print(x,y,result)


    
def main(): 
        
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (neede to capture w and h for canvas)
        

        #Initialize alien
        alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        #alien=Alien_blue(canvas)

        alien.activate()
        

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(alien,e.x,e.y))

        
        ############################################
        ####### start simulation
        ############################################
        #t=0               # time clock
        while True:

            if (not alien.is_active()):
                alien.activate()
              
            alien.next() # next time step
                    
            root.update()   # update the graphic (redraw)
            time.sleep(0.01)  # wait 0.01 second (simulation
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

