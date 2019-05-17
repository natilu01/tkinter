#ejercicio que muestra un cuadro de una sola seleccion
from tkinter import *
root = Tk()
v = IntVar() # tipo de variable que vamos a ocupar
Label(root,text="""Choose a programming language:""",justify = LEFT,padx = 20).pack()#modificaciones del texto en el tipo de letra, la jsutificacion
Radiobutton(root,text="Python",padx = 20,variable=v,value=1).pack(anchor=W)#modificaciones en los botones el tipo de letra el ancho, etc
Radiobutton(root,text="Perl",padx = 20,variable=v,value=2).pack(anchor=W)#modificaciones en los botones el tipo de letra el ancho, etc
mainloop()