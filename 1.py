import tkinter
from time import sleep
from math import sin
from math import cos
from math import pi


def start_button_click():
    speed = int(speed_options.get())
    if direction_options.get() == 'Clockwise':
        direction = 1
    else:
        direction = -1
    
    for i in range(0, 100 * direction, direction):
        canvas.create_oval(size//2 + r*cos(2*pi*i/100) - 3, size//2 + r*sin(2*pi*i/100) - 3, size//2 + r*cos(2*pi*i/100) + 3, size//2 + r*sin(2*pi*i/100) + 3, tags='dot', fill='green')
        root.update()
        sleep(0.05 / speed)
        canvas.delete('dot')
        root.update()



size = 600
root = tkinter.Tk()
root.title('Traveling dot')
lbl1 = tkinter.Label(root, text='Choose dot speed:')
lbl1.pack(anchor='nw')
speed_options = tkinter.StringVar(root)
speed_options.set('1')
spd_opt_menu = tkinter.OptionMenu(root, speed_options, '1', '2', '3')
spd_opt_menu.pack(anchor='nw')
canvas = tkinter.Canvas(root, width=size, height=size)
lbl2 = tkinter.Label(root, text='Choose direction of roration:')
lbl2.pack(anchor='nw')
direction_options = tkinter.StringVar(root)
direction_options.set('Clockwise')
drct_opt_menu = tkinter.OptionMenu(root, direction_options, 'Clockwise', 'Counterclockwise')
drct_opt_menu.pack(anchor='nw')
start_button = tkinter.Button(text='Start', command=start_button_click)
start_button.pack()
canvas.pack()

r = 200
canvas.create_oval(size//2 - r, size//2 - r, size//2 + r, size//2 + r)
root.update()
root.mainloop()