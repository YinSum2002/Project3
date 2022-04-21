from tkinter import *

class Counter:
    def __init__(self, canvas, val = 0):
        self.canvas = canvas
        self.val = val
        self.counter = self.canvas.create_text(70, 20, text = str(self.val), fill = "orange", font = ("Courier", 25))

    def increment(self, inc):
        self.val += inc
        self.canvas.itemconfig(self.counter, text = str(self.val))


#########################




def main():
    root = Tk()  # instantiate a tkinter window
    # my_image=PhotoImage(file="space1.png")
    my_image = PhotoImage(file="space2.png")

    w = my_image.width()
    h = my_image.height()
    canvas = Canvas(root, width=w, height=h)  # create a canvas width*height
    canvas.create_image(0, 0, anchor=NW, image=my_image)

    canvas.pack()
    root.update()

    counter = Counter(canvas, 10)

    root.bind("<Left>", lambda e: Counter.increment(counter, -1))
    root.bind("<Right>", lambda e: Counter.increment(counter, 1))

    root.mainloop()


    # to complete




if __name__=="__main__":
    main()



        
