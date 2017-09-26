#Hanzala Siddiqui
#tklogin.py
#Version 3.0
# GNU
from tkinter import *
from tkinter import ttk



root = Tk()
root.title("Create User")


mainframe = ttk.Frame(root, padding="5 10")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

def submit(*args):
    if(un.get()==''or pw.get()==''or gender.get()==''or usertype.get()=='0' or dept.get()==''):
        ttk.Label(mainframe, text="Error             ", font=("", 15)).grid(column=3, row=5, sticky=W)
        #clears
        un.set('')
        pw.set('')
        gender.set('')
        usertype.set('0')
        dept.set('')

    else:
        ttk.Label(mainframe, text="User Created!", font=("", 15)).grid(column=3, row=5, sticky=W)
        l=[]
        fileref = open("database.txt", "a")

        info=(un.get()+" "+pw.get()+" "+gender.get()+" "+usertype.get()+" "+dept.get()+" \n")
        fileref.write(info)
        fileref.close()
        un.set('')
        pw.set('')
        gender.set('')
        usertype.set('0')
        dept.set('')



#Labels
ttk.Label(mainframe, text="Create User", font = ("", 15)).grid(column=0, row=0, sticky=W)
ttk.Label(mainframe, text="Username").grid(column=1, row=1, sticky=E)
ttk.Label(mainframe, text="Password").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="User type", font = ("", 10)).grid(column=0, row=5, sticky=W)
ttk.Button(mainframe, text="Submit",command=submit).grid(column=3, row=3, sticky=W)

#Variables
un=StringVar()
pw=StringVar()
gender=StringVar()
usertype=StringVar()
dept=StringVar()


#Username
username=ttk.Entry(mainframe, width=17, textvariable=un)
username.grid(column=0,row=1,sticky=W)

#Password
password=ttk.Entry(mainframe, width=17, textvariable=pw,show='*')
password.grid(column=0,row=2,sticky=W)

#radiobuttons
male = ttk.Radiobutton(mainframe, text='Male', variable=gender, value='male')
female = ttk.Radiobutton(mainframe, text='Female', variable=gender, value='female')
male.grid(column=0,row=3,sticky=W)
female.grid(column=0,row=4,sticky=W)

#checkbox
admin=ttk.Checkbutton(mainframe, text='Admin', variable=usertype, onvalue='admin',offvalue=0)
user=ttk.Checkbutton(mainframe, text='User', variable=usertype, onvalue='user',offvalue=0)
guest=ttk.Checkbutton(mainframe, text='Guest', variable=usertype, onvalue='guest',offvalue=0)
admin.grid(column=0,row=6,sticky=W)
user.grid(column=0,row=7,sticky=W)
guest.grid(column=0,row=8,sticky=W)

#Combobox
department = ttk.Combobox(mainframe, state="readonly",textvariable=dept,values = ('IT', 'HR', 'Sales', 'Maintenance', 'Other'))

#department.set('')
department['values'] = ('IT', 'HR', 'Sales', 'Maintenance', 'Other')
department.grid(column=0,row=9,sticky=W)

root.mainloop()