from Tkinter import *

##root = Tk()
##
##name = Label(root, text = "Travel App")
##name.pack()
##
##root.mainloop()


class App:

    def __init__(self, master):
        frame = Frame(master)
        frame.pack()

        self.button = Button(
            frame, text = "QUIT", fg = "red", command=frame.quit
            )
        self.button.pack(side=LEFT)

root = Tk()
app = App(root)
root.mainloop()
root.destroy()
