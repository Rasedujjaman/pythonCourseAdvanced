# Ditital clock

from tkinter import *
# Tkinter is a graphical user interface (GUI) module for Python,
# you can make desktop apps with Python using tkinter.

from time import strftime


clockWindow = Tk()
clockWindow.title("Digital clock")


def time():
    timeString = strftime('%H:%M:%S')
    label.config(text=timeString)
    label.after(1000, time)  # aftre 1000ms we call time functoin again


label = Label(clockWindow, font=("ds-digital", 100), background="black"\
              , foreground = "cyan")

label.pack(anchor='center')
time()
mainloop()

