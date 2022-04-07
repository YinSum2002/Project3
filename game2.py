from tkinter import *
import time
from Alien import *
from Explosion import Explosion
from SpaceShip import SpaceShip
from Counter import Counter
from Missile import Missile


        
########## global variable
game_over=False

######### Function
def stop_game():
    global game_over
    game_over=True
    

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)





    #### to complete







if __name__=="__main__":
    main()

