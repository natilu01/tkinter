from tkinter import *
master = Tk()
whatever_you_do = "Whatever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"#mensaje
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))#modifica el tipo de letra, el fondo y el tamaño
msg.pack( )
mainloop( )