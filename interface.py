from tkinter import *

fenetre = Tk()

label = Label(fenetre, text="Game of la vie")
label.pack()
canvas = Canvas(fenetre, width=150, height=150, background='yellow')
rec1=canvas.create_rectangle(20,20,200,200,fill='black')
canvas.coords(rec1,10,10,20,20)
canvas.pack()
fenetre.mainloop()
