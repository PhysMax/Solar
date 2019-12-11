import tkinter as tk
from PIL import ImageTk, Image
from misc_obj import *
from calculate_gravitation import *
from satellites_formation import *

root = tk.Tk()

window_width = 800
window_height = 600

# Time interval between redrawings
dtime_render = 1
# Time interval of recalling step()
dtime_real = 1
# Recounting frequency
rec_freq = 100


space_objects = list()


canv = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canv.pack(side=tk.TOP)

label_1 = tk.Label(root, text='')
label_1 = label_1.pack()

pilImage = Image.open("image_space_3_1.jpg")
image = ImageTk.PhotoImage(pilImage)
image_sprite = canv.create_image(0, 0, anchor='nw', image=image)


def render():
    for obj in space_objects:
        obj.draw()
    canv.after(dtime_render, render)


def step():
    dtime_phys = dtime_real / rec_freq
    for i in range(rec_freq):
        satellites_formation(space_objects)
        for obj in space_objects:
            obj.move(dtime_phys)
        # calculate_gravitation(space_objects)
    canv.after(dtime_real, step)


player = Planet(100, 0, 0, 0, 0, 10, None, canv)
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

step()
render()

root.mainloop()
