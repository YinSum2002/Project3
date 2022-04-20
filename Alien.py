from tkinter import *
import math
import time, random

class Alien:
    def __init__(self, canvas, inc = 4, color = "yellow", width = 50, height = 50, pval = 1):
        self.canvas = canvas
        self.inc = inc
        self.color = color
        self.width = width
        self.height = height
        self.pval = pval
        self._active = False

    def activate(self):
        x = random.randint(self.width//2, self.canvas.winfo_width()-self.width//2)
        self.x = x
        self.y = 0
        left = x - self.width // 2
        right = x + self.width // 2
        bottom = self.y + self.height // 2
        top = self.y  - self.height // 2
        self._active = True
        self.id = self.canvas.create_rectangle(left, bottom, right, top, fill = self.color, outline = self.color)

    def is_active(self):
        return self._active

    def deactivate(self):
        self._active = False
        self.canvas.delete(self.id)

    def next(self):
        if self._active == True:
            self.canvas.move(self.id, 0, self.inc)
            self.y += self.inc
            if self.y >= self.canvas.winfo_height():
                self.deactivate()

    def is_shot(self, x0, y0):
        top = self.y - self.height//2
        bottom = self.y + self.height//2
        left = self.x - self.width//2
        right = self.x + self.width//2
        return left <= x0 and x0 <= right and top <= y0 and y0 <= bottom






################################################################
################################################################

class Alien_red(Alien):
    def __init__(self,c):
        self.image=PhotoImage(file="alien_red.png")  # keep a reference (avoid garbage collector)
        width=self.image.width()
        height=self.image.height()

        # contstructor to complete
        super().__init__(c, inc = 4, color="red", width = self.image.width(), height = self.image.height(), pval = 2)
    # to complete
    def activate(self):
        x = random.randint(self.width // 2, self.canvas.winfo_width() - self.width // 2)
        self.x = x
        self.y = 0
        self._active = True
        self.id = self.canvas.create_image(x,self.y,anchor = CENTER, image = self.image)


###############################################################
###############################################################

class Alien_green(Alien_red):
    def __init__(self, c):
        self.image = PhotoImage(file="alien_green.png")  # keep a reference (avoid garbage collector)
        width = self.image.width()
        height = self.image.height()
        Alien.__init__(self, c, inc=4, color = "green", pval = 4)

    def next(self):
        if self._active == True:
            self.canvas.move(self.id, random.randint(-5,5), self.inc)
            self.y += self.inc
            self.x += random.randint(-5,5)
            #print(self.x)
            if self.y >= self.canvas.winfo_height():
                self.deactivate()

###############################################################
###############################################################
                


class Alien_blue(Alien_red):
    def __init__(self, c):
        self.d = math.pi * random.randint(200, 340)/180
        self.image = PhotoImage(file="alien_blue.png")  # keep a reference (avoid garbage collector)
        width = self.image.width()
        height = self.image.height()
        Alien.__init__(self, c, inc=4, color = "blue", pval = 3)

        
    def next(self):
        if self._active == True:
            x = self.inc * math.cos(self.d)
            y = -self.inc * math.sin(self.d)
            print(self.d, self.x, self.canvas.winfo_width(), self.width)
            if self.x + x <= self.width//2:
                self.d = math.pi - self.d
            elif self.x + x >= self.canvas.winfo_width() - self.width//2: #by using self.x + x,
                self.d = -math.pi - self.d
            self.canvas.move(self.id, x, y)
            self.y += y
            self.x += x
            if self.y >= self.canvas.winfo_height():
                self.deactivate()





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
        #alien=Alien(canvas)
        #alien=Alien_red(canvas)
        #alien=Alien_green(canvas)
        alien=Alien_blue(canvas)

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

