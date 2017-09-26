from tkinter import *
from tkinter import ttk, Image

import sys

root = Tk()
root.title("Johnny's Vending Machines")

mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

drag = ttk.Frame(root, padding = "5 10") # creating another Frame to put the image in
drag.grid(column = 2, row = 2, sticky = (N,E))
drag.columnconfigure(0, weight=1)
drag.rowconfigure(0, weight=1)
canvas = Canvas(drag, width=800, height=600)
canvas.pack()

s = ttk.Style()
s.configure('my.TButton', font=('', 12)) # changes font size of buttons to 12

def vending(*args): #clicking vending button will add the image which this function does
    ttk.Label.pack_forget(root)
    sk = ttk.Label(root, text="Johnny's Vending Machines", foreground='blue', font=('', 47))
    sk.grid(column=2, row=1, sticky=(N, E))
    ttk.Label(root, 'vending.bmp').grid(column=2, row=2)
    #canvas.image = im
    #canvas.create_image(0, 0, image=canvas.image, anchor="nw")

def toilet(*args): #clicking toilet button will add the image which this function does
    ttk.Label.pack_forget(root)
    ttk.Label(root, text="            Johnny's Toilets       ", foreground='blue', font=('', 47)).grid(column=2, row=1,sticky=(N, E))
    im = Image.open('dune-toilet.bmp')
    canvas.image = im
    canvas.create_image(0, 0, image=canvas.image, anchor="nw")
vending()
ttk.Button(root, text="Johnny's Toilets", command=toilet, style = 'my.TButton').grid(column=1, row=3, sticky=E)
ttk.Button(root, text="Johnny's Vending" , command=vending, style = 'my.TButton').grid(column=3, row=3, sticky=W)

for child in mainframe.winfo_children(): child.grid_configure(padx=5, pady=5)

root.mainloop()