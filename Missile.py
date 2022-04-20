from tkinter import *
import time,random

class Missile:
    def __init__(self, canvas, ceiling_height = 0, inc = 5, color = "orange", width = 8, height = 25):
        self.canvas = canvas
        self.ceiling_height = ceiling_height
        self.inc = inc
        self.color = color
        self.width = width
        self.height = height
        self.__active = False

    def activate(self, x, y):
        self.x = x #x is center
        self.y = y #y is bottom
        self.__active = True
        self.id = self.canvas.create_rectangle(x - self.width // 2, y - self.height, x + self.width // 2, y, fill = self.color, outline = self.color)

    def deactivate(self):
        self.__active = False
        self.canvas.delete(self.id)

    def is_active(self):
        return self.__active

    def next(self):
        if self.__active == True:
            self.canvas.move(self.id, 0, -5)
            self.y -= 5
            if self.y - self.height <= self.ceiling_height:
                self.deactivate()



    @staticmethod
    def add_missile(canvas, missiles, x, y, ceiling, inc = 5, color="orange"):
        i = len(missiles) - 1
        while i >= 0:
            if missiles[i].is_active() == False:
                del missiles[i]
            i -= 1
        missile = Missile(canvas, ceiling, inc, color)
        missile.activate(x, y)
        missiles.append(missile)

       #### to complete















###################################################
###################################################

        
def main():

        ##### create a window, canvas and ball object
        root = Tk() # instantiate a tkinter window
        w,h=800,1000
        canvas = Canvas(root, width=w,height=h,bg="black") # create a canvas width*height
        
        canvas.pack()
        root.update()   # update the graphic (if not cannot capture w and h for canvas if needed)

        #Initialize list of Missiles
        missiles=[]
        
        
        ############################################
        ####### start simulation
        ############################################
        t=0                # initialize time clock

        while True:
            if t % 50 == 0:
                y = h
                x = random.randint(0, w)
                ceiling = random.randint(0, h)
                inc = random.randint(2, 7)
                items = ["red", "green", "blue", "yellow", "white", "orange", "purple"]
                color = random.choice(items)
                print(ceiling)
                Missile.add_missile(canvas, missiles, x, y, ceiling, inc, color)
            t += 1


            for m in missiles:
                m.next()

            # check active status of list of booms (for debugging)
            for m in missiles:
                print(m.is_active(), end=" ")
            print()

            root.update()  # redraw
            time.sleep(0.01) #not this because sleep p


        root.mainloop()

if __name__ == "__main__":
    main()
