from tkinter import *
root = Tk()

font = 'Verdana', 16
username_label = Label(text='Enter Username:', font=font, width=20)
password_label = Label(text = 'Enter Password:', font=font, width=20)
username_label.grid(row=0,column=0)
password_label.grid(row=1,column=0)

username_entry = Entry(font=font, width=20)
password_entry = Entry(font=font, width=20, show="*")
username_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

mainloop()