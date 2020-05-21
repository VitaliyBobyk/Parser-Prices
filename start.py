from tkinter import *
TK_SILENCE_DEPRECATION = 1
root = Tk()

root.resizable(width=False, height=False)
root.geometry('200x200')
root.title('Hello!')


b1 = Button(root, text="Apple Room", width=12, height=1, bg='#808080', fg='black', font='arial 14')

b2 = Button(root, text="iPeople ", width=12, height=1, bg='#808080', fg='black', font='arial 14')


def leftclick1(event):
    from room import start_room
    start_room


def leftclick2(event):
    from people import start_ipeople
    start_ipeople


b1.pack(padx=20, pady=20)
b2.pack()
b1.bind('<Button-1>', leftclick1)
b2.bind('<Button-1>', leftclick2)
root.mainloop()
