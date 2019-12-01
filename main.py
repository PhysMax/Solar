import tkinter as tk
from misc_objects import *

root = tk.Tk()

window_width = 800
window_height = 600

# Time interval between redrawings
dtime_render = 1
# Step of modelling time
dtime_phys = 10


space_objects = list()


canv = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canv.pack(side=tk.TOP)


def render():
    for obj in space_objects:
        obj.draw()
    canv.after(dtime_render, render)


def step():
    for obj in space_objects:
        obj.move(dtime_phys)
    canv.after(dtime_phys, step)


player = Planet(10, 0, 0, 0, 0, 10, None, canv)
space_objects.append(player)

step()
render()

root.mainloop()
