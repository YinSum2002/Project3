from tkinter import *
import time
from Explosion import Explosion
from Counter import Counter
from Alien import *


########## global variable
game_over=False

######### Functions

def stop_game():
    global game_over
    game_over=True
    
def shoot 
    ####### to complete




################
    
def main(): 
       
        ##### create a window, canvas 
        root = Tk() # instantiate a tkinter window
        my_image=PhotoImage(file="space1.png")
        #my_image=PhotoImage(file="space2.png")

        w=my_image.width()
        h=my_image.height()
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height

        canvas.create_image(0,0,anchor=NW,image=my_image)
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas)
        
        
        #Initialize list of Explosions
        booms=[]
        #Initialize list of Aliens
        aliens=[]
        #Initialize counter ammunition
        amunition=Counter(canvas,10)

        ####### Tkinter binding mouse actions
        root.bind("<Button-1>",lambda e:shoot(canvas,aliens,booms,amunition,e.x,e.y))
        root.bind("<Escape>",lambda e:stop_game())

        
        ############################################
        ####### start simulation
        ############################################



        #To complete (time sleep is 0.01s)




          
           
        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

