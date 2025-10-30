from tkinter import *
root = Tk()

font1 = ("Verdana",16)
font2 = ("Comic Sans MS",16, "underline")
font3 = ("Arial",16, "bold")

label1 = Label(text = "This is a good day", font=font1)
label2 = Label(text = "This is a good day", font=font2)   
label3 = Label(text = "This is a good day", font=font3) 

label1.grid(row=5, column=0, columnspan=4)
label2.grid(row=7, column=0, columnspan=4, rowspan=2)
label3.grid(row=9, column=0, columnspan=4)

label1.configure(text="This is a sunny day!", font=('Times New Roman', 16))

s = StringVar()
s.set('Good Morning')
label = Label(textvariable=s, font=("Verdana", 16))
label.grid(row=5, column=1, columnspan=4) 
s.set('Nice to meet you!')

labels = []

for i in range(16):
    l = Label(text=str(i), font=("Verdana", 16))
    l.grid(row=i // 4, column=i % 4)
    labels.append(l)

mainloop()