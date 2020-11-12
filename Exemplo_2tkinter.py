from tkinter import *
top = Frame(); top.pack()
rotulo = Label(top, text="Rótulo Exemplo", foreground="black")
rotulo.pack()
rotulo.configure(relief="ridge", font="Arial 20 bold", borde=6, background="white")
top.master.title("Fkzcorp")
top.master.geometry("250x250+100+100")
mainloop()