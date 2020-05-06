from tkinter import *

root = Tk()

root.resizable(width=False, height=False)
root.geometry('300x300')
root.title('Hello!')
root['bg'] = 'black'

el = Label(root, text="Apple Room Price", width=50, height=1, bg="black", fg='white', font='arial 14')

b1 = Button(root, text="New", width=9, height=1, bg='#808080', fg='white', font='arial 14')

b2 = Button(root, text="Used", width=9, height=1, bg='#808080', fg='white', font='arial 14')


def leftclick1(event):
    from parcer import AppleRoom
    AppleRoom.new("New")
def leftclick2(event):
    from parcer import AppleRoom
    AppleRoom.used("Used")



el.pack()
b1.pack(padx=20, pady=20)
b2.pack()
b1.bind('<Button-1>', leftclick1)
b2.bind('<Button-1>', leftclick2)
root.mainloop()