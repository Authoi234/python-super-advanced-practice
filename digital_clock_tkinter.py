from tkinter import *
from datetime import datetime

root = Tk()
root.title('Digital Clock')
root.minsize(520, 100)

font1 = ("Cursed Timer ULiL", 72)
font2 = ("Cursed Timer ULiL", 48)

time_str= StringVar()
sec_str= StringVar()

time_str.set('00:00')
sec_str.set('00')

time_label = Label(textvariable=time_str, font=font1)
sec_label = Label(textvariable=sec_str, font=font2)

mainloop()