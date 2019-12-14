import tkinter as tk
from PIL import ImageTk, Image
from calculate_gravitation import *
from satellites_formation import *
from keypress import *
from objects_generator import *

root = tk.Tk()

# Time interval between redrawings
dtime_render = 10
# Time interval of recalling step()
dtime_real = 1
# Recounting frequency
rec_freq = 1

space_objects = list()

canv = tk.Canvas(root, width=window_width, height=window_height, bg="black")
canv.pack(side=tk.TOP)

# Experimental
label_1 = tk.Label(root, text='Planet', bg='black', fg='white', width=114)
label_1.pack()


pilImage = Image.open("image_space_3_1.jpg")
image = ImageTk.PhotoImage(pilImage)
image_sprite = canv.create_image(0, 0, anchor='nw', image=image)


def render():
    for obj in space_objects:
        obj.draw()

    canv.after(dtime_render, render)


# Experimental
def lab_config():
    if isinstance(player, Asteroid):
        label_1.configure(text='Asteroid'+' '+str(player.m), fg='burlywood3')
    elif isinstance(player, Planet):
        label_1.configure(text='Planet'+' '+str(player.m), fg='LightSkyBlue2')
    else:
        label_1.configure(text='Star'+' '+str(player.m), fg='yellow')


# Trial
def destroy(obj, space_objcts):
    if not(obj.satellite_of is None):
        if (obj.x - obj.satellite_of.x) ** 2 + (
                obj.y - obj.satellite_of.y) ** 2 < \
                obj.satellite_of.r ** 2:
            obj.destroy(space_objcts)


def step():
    dtime_phys = dtime_real / rec_freq
    for i in range(rec_freq):
        satellites_formation(space_objects)
        for obj in space_objects:
            obj.apply_force(obj.key_force_x, obj.key_force_y)
            obj.move(dtime_phys)
            destroy(obj, space_objects)
        calculate_gravitation(space_objects)
    lab_config()
    canv.after(dtime_real, step)


def gen():
    quantity_obj = 40
    check_live_field(player, space_objects, quantity_obj, canv)
    root.after(25, gen)


player = Planet(100, 0, 0, 0, 0, 10, None, canv)
ast_1 = Asteroid(1, -170, 0, 0, 0.04, 30, player, canv)
space_objects.append(player)
space_objects.append(ast_1)

ast_2 = Asteroid(1, -130, 0, 0, -0.02, 30, player, canv)
space_objects.append(ast_2)
ast_3 = Asteroid(1, -40, 20, 0.01, 0, 30, player, canv)
space_objects.append(ast_3)
ast_4 = Asteroid(1, -40, 20, 0.01, 0, 30, player, canv)
space_objects.append(ast_4)
ast_5 = Asteroid(1, -40, 20, 0.01, 0, 30, player, canv)
space_objects.append(ast_5)
ast_5 = Asteroid(1, -40, 20, 0.01, 0, 30, player, canv)
space_objects.append(ast_5)
planet = Planet(100, -150, 0, 0.01, -0.01, 30, player, canv)
space_objects.append(planet)

star = Star(10000, -110, 90, 0.1, 0.1, 10, player, canv)
space_objects.append(star)

gen()
step()
render()

root.bind("<KeyPress-w>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-w>", lambda event, p=player: stop_player(event, p))
root.bind("<KeyPress-s>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-s>", lambda event, p=player: stop_player(event, p))
root.bind("<KeyPress-d>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-d>", lambda event, p=player: stop_player(event, p))
root.bind("<KeyPress-a>", lambda event, p=player: move_player(event, p))
root.bind("<KeyRelease-a>", lambda event, p=player: stop_player(event, p))


def absorb(event):
    player.consume()


root.bind('<space>', absorb)

root.mainloop()
