import tkinter as tk

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
        obj.draw(canv)
    canv.after(dtime_render, render)


def step():
    for obj in space_objects:
        obj.move(dtime_phys)
    canv.after(dtime_phys, step)


step()
render()

root.mainloop()
