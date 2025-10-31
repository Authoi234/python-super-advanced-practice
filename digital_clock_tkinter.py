from tkinter import *
from datetime import datetime

root = Tk()
root.title('Digital Clock')
root.minsize(520, 100)

font1 = ("fangsong ti", 72, "bold")
font2 = ("fangsong ti", 48, "bold")
font3 = ("Verdana", 72)

time_str= StringVar()
sec_str= StringVar()
time_format = IntVar()
am_pm_str = StringVar()

time_str.set('00:00')
sec_str.set('00')
time_format.set(0)
am_pm_str.set('')

time_label = Label(textvariable=time_str, font=font1)
sec_label = Label(textvariable=sec_str, font=font2)
am_pm_label = Label(textvariable=am_pm_str, font=font3, width=3)

time_label.grid(row=0, column=0, sticky="S")
sec_label.grid(row=0, column=1, sticky="S")
am_pm_label.grid(row=0, column=3, sticky='S')

def update():
    now = datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second

    if time_format.get() == 1:
        if hour>12:
            am_pm_str.set("PM")
            hour %= 12
        else:
            am_pm_str.set("PM")
    else:
        am_pm_str.set("")

    time_str.set('{:02d}:{:02d}'.format(hour, minute))
    sec_str.set('{:02d}'.format(second))

    root.after(1000, update)

update()

def settings():
    global time_format
    settings_win = Toplevel()
    settings_win.title("Setttings")
    twentyfour = Radiobutton(settings_win, text="24-hour format", var=time_format, value=0)
    twelve = Radiobutton(settings_win, text="AM/PM format", var=time_format, value=1)
    twentyfour.grid(row=0, column=0)
    twelve.grid(row=0, column=1)

menu = Menu()
root.configure(menu=menu)

file_menu = Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=file_menu)

file_menu.add_command(label='Settings', command=settings)
file_menu.add_separator()
file_menu.add_command(label='Exit', command=root.destroy)


mainloop()