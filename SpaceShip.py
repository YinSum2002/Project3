from tkinter import *

class SpaceShip:
    def __init__(self, canvas):
        self.canvas = canvas
        self.image = PhotoImage(file="ship.png")  # keep a reference (avoid garbage collector)
        self.width = self.image.width()
        self.height = self.image.height()
        self.__active = False

    def activate(self):
        self.x = self.canvas.winfo_width()//2
        self.y = self.canvas.winfo_height()
        self.__active = True
        self.id = self.canvas.create_image(self.x, self.y, anchor = "s", image = self.image)

    def deactivate(self):
        self.__active = False
        self.canvas.delete(self.id)

    def is_active(self):
        return self.__active

    def shift_left(self):
        if self.__active == True:
            new_pos = self.x - 15
            if new_pos < self.width//2:
                new_pos = self.width//2
            self.canvas.move(self.id, new_pos - self.x, 0)
            self.x = new_pos
            #print("Left", self.x)

    def shift_right(self):
        if self.__active == True:
            new_pos = self.x + 15
            if new_pos > self.canvas.winfo_width() - self.width//2:
                new_pos = self.canvas.winfo_width() - self.width//2
            self.canvas.move(self.id, new_pos - self.x, 0)
            self.x = new_pos
            #print("Right", self.x)

    def is_shot(self, x0, y0):
        top = self.y - self.height
        bottom = self.y
        left = self.x - self.width//2
        right = self.x + self.width//2
        return left <= x0 and x0 <= right and top <= y0 and y0 <= bottom

    
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

