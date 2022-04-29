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
    
def shoot(canvas, missiles, ship):
    if ship.is_active():
        Missile.add_missile(canvas, missiles, ship.x, canvas.winfo_height() - ship.height, 0, inc=5, color="orange")



    
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
    record = {'blue': 0, 'red': 0, 'green': 0}
    stats = []

    ship = SpaceShip(canvas)
    ship.activate()

    root.bind("<Left>", lambda e: ship.shift_left())
    root.bind("<Right>", lambda e: ship.shift_right())
    root.bind("<Up>", lambda e: shoot(canvas, missiles, ship))
    root.bind("<Escape>", lambda e: stop_game())

    t = 0
    blow = None
    while not game_over and amunition.val>=0: #see what you can do about getting down to 0
        if t % 100 == 0:
            Alien.add_alien(canvas, aliens)
        if t % 100 == 0:
            stats.append(tuple(record.values()))
        t += 1
        for e in explosions:
            e.next()

        for m in missiles:
            m.next()

        for a in aliens:
            a.next()
            if a.is_active():
                for m in missiles:
                    if a.is_shot(m.x,m.y): # and a.is_active == True:
                        record[a.color] += 1
                        amunition.increment(a.pval)  # main function, call Counter class
                        Explosion.add_explosion(canvas, explosions, a.x, a.y, 30, color=a.color)
                        a.deactivate()
                        m.deactivate()
                        break

                if ship.is_active() and ship.is_shot(a.x, a.y):
                    blow = Explosion.add_explosion(canvas, explosions, ship.x, ship.y, 50, color="rainbow")
                    amunition.increment(-10)
                    ship.deactivate()
                    a.deactivate()

        if blow and blow.is_active() == False:
            blow = None
            ship.activate()

        root.update()  # update the graphic (redraw)
        time.sleep(0.01)  # wait 0.01 second (simulation)
        #### to complete


    canvas.create_text(w // 2, h // 2, text="GAME OVER", fill="orange", font=("Courier", 25))

    print(record)
    f1 = open("game2.txt","w")
    for t in stats:
        f1.write(f'{t[0]} {t[1]} {t[2]}\n')
    f1.close()

    root.mainloop()

if __name__=="__main__":
    main()

