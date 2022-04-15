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

        t = 0  # initialize time clock

        while True:
                if t % 50 == 0:
                        y = h
                        x = random.randint(0, w)
                        ceiling = random.randint(h//4, 3*h//4)
                        inc = random.randint(2, 7)
                        items = ["red", "green", "blue", "yellow", "white", "orange", "purple"]
                        color = random.choice(items)
                        Missile.add_missile(canvas, missiles, x, y, ceiling, inc, color)

                t += 1

                for m in missiles:
                        m.next()
                        if m.is_active() == False:
                                Explosion.add_explosion(canvas, booms, m.x, m.y, random.randint(100,300), "rainbow")
                for boom in booms:
                        boom.next()

                # check active status of list of booms (for debugging)
                for m in missiles:
                        print(m.is_active(), end=" ")
                print()

                root.update()  # redraw
                time.sleep(0.01)  # not this because sleep p

        root.mainloop()



        ### To complete







        

if __name__=="__main__":
    main()

