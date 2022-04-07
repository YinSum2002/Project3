from tkinter import *

class SpaceShip:


 

    
def main():
    ##### create a window and canvas
    root = Tk() # instantiate a tkinter window
    #my_image=PhotoImage(file="space1.png")
    my_image=PhotoImage(file="space2.png")
    
    w=my_image.width()
    h=my_image.height()
    canvas = Canvas(root, width=w,height=h) # create a canvas width*height
    canvas.create_image(0,0,anchor=NW,image=my_image)
   
    canvas.pack()
    root.update()   # update the graphic (if not cannot capture w and h for canvas)


    #Initialize the ship
    ship=SpaceShip(canvas)
    ship.activate()
    
    
    ####### Tkinter binding mouse actions
    root.bind("<Left>",lambda e:ship.shift_left())
    root.bind("<Right>",lambda e:ship.shift_right())

    root.mainloop() # wait until the window is closed
    

if __name__=="__main__":
    main()

