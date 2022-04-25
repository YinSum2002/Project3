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

    explosions = []  # explosion list
    missiles = []  # missile list
    aliens = []  # alien list
    counter = 0

    ship = SpaceShip(canvas)
    ship.activate()

    t = 0

    root.bind("<Left>", lambda e: ship.shift_left())
    root.bind("<Right>", lambda e: ship.shift_right())
    root.bind("<Up>", lambda e: Missile.add_missile(canvas, missiles, ship.x, h-ship.height, inc = 5, color = "orange"))
    root.bind("<Escape>", lambda e: stop_game())

    while True:
        # Initialize the ship

        #print(ship.x)

        ####### Tkinter binding mouse actions

        root.update()  # update the graphic (redraw)
        time.sleep(0.01)  # wait 0.01 second (simulation)

        if t % 50 == 0:

            for e in explosions:
                if e.is_active == True:
                    e.next()

            for m in missiles:
                if m.is_active == True:
                    m.next()

            for a in aliens:
                if a.is_active == True:
                    a.next()
                    for m in missiles:
                        if a.y - a.height//2 < m.y < a.y + a.height//2 and a.x - a.width//2 < m.x < a.x + a.width//2:
                            counter.increment(a.pval)  # main function, call Counter class
                            Explosion.add_explosion(canvas, explosions, a.x, a.y, 30, color=a.color)
                            a.deactivate()
                if a.x - a.width//2 < ship.x < a.x + a.width//2 and a.y > ship.y:
                    Explosion.add_explosion(canvas, explosions, ship.x, ship.y, 30, color=a.color)
                    ship.deactivate()
        t += 1
        #### to complete







if __name__=="__main__":
    main()

