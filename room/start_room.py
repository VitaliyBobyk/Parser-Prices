from tkinter import *

root = Tk()

root.resizable(width=False, height=False)
root.geometry('200x200')
root.title('Hello!')

el = Label(root, text="Apple Room Price", width=50, height=1, bg="black", fg='white', font='arial 14')

b1 = Button(root, text="New", width=9, height=1, bg='#808080', fg='black', font='arial 14')

b2 = Button(root, text="Used", width=9, height=1, bg='#808080', fg='black', font='arial 14')


def leftclick1(event):
    from room.room import AppleRoom
    start = AppleRoom()
    start.new()


def leftclick2(event):
    from room.room import AppleRoom
    start = AppleRoom()
    start.used()


el.pack()
b1.pack(padx=20, pady=20)
b2.pack()
b1.bind('<Button-1>', leftclick1)
b2.bind('<Button-1>', leftclick2)
root.mainloop()
