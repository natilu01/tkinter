#ejercicio 5 con un menu de una sola opcion
from tkinter import *
root = Tk()
v = IntVar()#tipo de variable
v.set(1) # initializing the choice, i.e. Python
languages = [("Python",1),("Perl",2),("Java",3),("C++",4),("C",5)]#arreglo de 5 opciones donde definimos la posicion que cada uno ocupa
def ShowChoice():#nos permite hacer una eleccion 
	print (v.get())
Label(root,text="""Choose your favourite programming language:""",justify = LEFT,padx = 20).pack()#texto de la ventana a ejecutar 
for txt, val in languages: #nos permite crear los botones de acuerdo al ciclo que tenemos definido en nuestro arreglo 
	Radiobutton(root,text=txt,padx = 30,variable=v,command=ShowChoice,value=val).pack(anchor=W)
mainloop()