import tkinter as tk

from misc_obj import *
from calculate_gravitation import *
from satellites_formation import *
from keypress import *
from objects_generator import *

root = tk.Tk()

# Time interval between redrawings
dtime_render = 1
# Step of modelling time
dtime_phys = 1

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
        obj.apply_force(obj.key_force_x, obj.key_force_y)
        obj.move(dtime_phys)
    satellites_formation(space_objects)
    canv.after(dtime_phys, step)


def gravity():
    calculate_gravitation(space_objects)
    canv.after(dtime_phys, gravity)


def gen():
    generate(player, space_objects, canv)



space_objects = list()

player = Planet(1000000, 0, 0, 0, 0, 10, None, canv)
ast_1 = Asteroid(1, -170, 0, 0, 0.04, 30, player, canv)
space_objects.append(player)
space_objects.append(ast_1)

ast_2 = Asteroid(1, -130, 0, 0, -0.02, 30, player, canv)
space_objects.append(ast_2)
ast_3 = Asteroid(1, -60, 30, 0.01, 0, 30, player, canv)
space_objects.append(ast_3)
planet = Planet(100, -150, 0, 0.01, -0.01, 30, player, canv)
space_objects.append(planet)

star = Star(10000, -110, 90, 0.05, 0.05, 10, player, canv)
space_objects.append(star)


gravity()
step()
render()
gen()

root.bind("<KeyPress-w>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-w>", lambda event, p=player: stop_player(event, p))
root.bind("<KeyPress-s>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-s>", lambda event, p=player: stop_player(event, p))
root.bind("<KeyPress-d>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-d>", lambda event, p=player: stop_player(event, p))
root.bind("<KeyPress-a>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-a>", lambda event, p=player: stop_player(event, p))

root.mainloop()
