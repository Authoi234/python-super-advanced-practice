from tkinter import *
root = Tk()

font = 'Verdana', 16
clicked_label = Label(text='Not Clicked', font=font, width=20)
clicked_label.grid(row=0, column=0)

def callback():
    clicked_label.configure(text = 'Button was Clicked')

clicker_button = Button(text='Click here', font = font, width=10, command=callback)
clicker_button.grid(row=1, column=0)

mainloop()