#import necessary libraries
from tkinter import*

#Setting up main window
root = Tk()
root.geometry("400x300")
root.title("main")

#Function to open new (Top level) window
def topwin():
    #setting up top window
    top = Toplevel()
    top.geometry("100x100")
    top.title("toplevel")
    #Adding a label widget to top window
    l2 = Label(top, text="This is toplevel window")
    l2.pack()

    top.mainloop()

#Adding a label and button widget to root(main) window
l = Label(root, text="This is root window")
btn = Button(root, text="click here to open another window", command=topwin)
#Arranging widgets
l.pack()
btn.pack()

root.mainloop()