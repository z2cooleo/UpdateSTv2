from tkinter import *
from tkinter import ttk

 
root = Tk()
root.title("Графическая программа на Python")
root.geometry("400x300")

lblVersion = Label(text="6.0.1243", font="Arial 14").grid(row=0, column=2)
lblPercent = Label(text="63%", font="Arial 12").grid(row=1, column=0)
lblNetSpeed = Label(text="3Mb\s", font="Arial 7").grid(row=1, column=1)
s = ttk.Style()
s.theme_use('alt')
s.configure("red.Horizontal.TProgressbar", foreground='blue', background='blue')
mpb = ttk.Progressbar(root, style="red.Horizontal.TProgressbar", orient ="horizontal",length = 200, mode ="determinate")
mpb["maximum"] = 100
mpb["value"] = 50
lblChange = Label(text="List of changes", font="Arial 7").grid(row=2, column=3)


root.mainloop()


