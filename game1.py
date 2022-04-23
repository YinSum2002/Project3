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
    
def shoot(canvas, a_list, e_list, counter, x, y):
        hit = 0
        for a in a_list:
                if a.is_active() == True:
                        if a.is_shot(x,y) == True:

                                counter.increment(a.pval) #main function, call Counter class
                                a.deactivate()
                                hit += 1
                                Explosion.add_explosion(canvas, e_list, x, y, 30, color = a.color)

        #write seperate function for if miss EVERYONE
        if hit == 0:
                print(f'Miss, {x}, {y}')
                Explosion.add_explosion(canvas, e_list, x, y, 30, color= "white")
                counter.increment(-3) #capital or lower case C?

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

        t = 0
        while not game_over and amunition.val > 0:
                if t % 50 == 0:
                        Alien.add_alien(canvas, aliens)
                t += 1
                for a in aliens:
                        a.next()  # next time step

                for b in booms:
                        b.next()
                root.update()  # update the graphic (redraw)
                time.sleep(0.01)

        canvas.create_text(w//2, h//2, text="GAME OVER", fill="orange", font=("Courier", 25))

        root.mainloop() # wait until the window is closed
        

if __name__=="__main__":
    main()

