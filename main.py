import tkinter as tk
from misc_obj import *
from calculate_gravitation import *
from satellites_formation import *

root = tk.Tk()

window_width = 800
window_height = 600

# Time interval between redrawings
dtime_render = 1
# Step of modelling time
dtime_phys = 1


space_objects = list()


canv = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canv.pack(side=tk.TOP)


def render():
    for obj in space_objects:
        obj.draw()
    canv.after(dtime_render, render)


def step():
    for obj in space_objects:
        if not (obj.satellite_of is None):
            pass
        obj.move(dtime_phys)
    satellites_formation(space_objects)
    canv.after(dtime_phys, step)


def gravity():
    calculate_gravitation(space_objects)
    canv.after(dtime_phys, gravity)


player = Planet(1, 0, 0, 0, 0, 10, None, canv)
ast_1 = Asteroid(1, -170, 0, 0, 0.02, 30, player, canv)
space_objects.append(player)
space_objects.append(ast_1)

ast_2 = Asteroid(1, -130, 0, 0, -0.02, 30, player, canv)
space_objects.append(ast_2)
ast_3 = Asteroid(1, -60, 30, 0.01, 0, 30, player, canv)
space_objects.append(ast_3)
planet = Planet(1000, -150, 0, 0.01, -0.01, 30, player, canv)
space_objects.append(planet)

star = Star(10, -150, 70, -0.01, 0, 10, player, canv)
space_objects.append(star)

gravity()
step()
render()

root.mainloop()
