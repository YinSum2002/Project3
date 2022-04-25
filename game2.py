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
    amunition = Counter(canvas, 0)

    ship = SpaceShip(canvas)
    ship.activate()

    root.bind("<Left>", lambda e: ship.shift_left())
    root.bind("<Right>", lambda e: ship.shift_right())
    root.bind("<Up>", lambda e: Missile.add_missile(canvas, missiles, ship.x, h-ship.height, 0, inc = 5, color = "orange"))
    root.bind("<Escape>", lambda e: stop_game())

    t = 0
    while not game_over and amunition.val>=0: #see what you can do about getting down to 0
        if t % 100 == 0:
            Alien.add_alien(canvas, aliens)
        t += 1
        for e in explosions:
            e.next()

        for m in missiles:
            m.next()

        for a in aliens:
            a.next()
            for m in missiles:
                if a.is_shot(m.x,m.y): # and a.is_active == True:
                    amunition.increment(a.pval)  # main function, call Counter class
                    Explosion.add_explosion(canvas, explosions, a.x, a.y, 30, color=a.color)
                    a.deactivate()
                    m.deactivate()
                    break

            if ship.is_shot(a.x, a.y):
                Explosion.add_explosion(canvas, explosions, ship.x, ship.y, 50, color="rainbow")
                amunition.increment(-10)
                ship.deactivate()
                a.deactivate()
        t += 1
        root.update()  # update the graphic (redraw)
        time.sleep(0.01)  # wait 0.01 second (simulation)
        #### to complete







if __name__=="__main__":
    main()

