#Hanzala Siddiqui
#bucky.py
#Version 3.0
#GNU
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program. If not, see <http://www.gnu.org/licenses/>.
#####
#Hanzala N Siddiqui
#bucky.py


from tkinter import *
from tkinter import ttk

def doNothing():
    print('ok ok i wont...')

root = Tk()

menu=Menu(root)
root.config(menu=menu)

subMenu=Menu(menu)
menu.add_cascade(label='File', menu=subMenu)
subMenu.add_command(label='New Project...',command=doNothing)
subMenu.add_command(label='New ...',command=doNothing)
subMenu.add_separator()
subMenu.add_command(label='Exit',command=doNothing)

editMenu=Menu(menu)
menu.add_cascade(label='Edit', menu=editMenu)
editMenu.add_command(label='Redo',command=doNothing)

root.mainloop()