""" Planet, asteroid and star """
from random import choice
from space_obj import space_obj

colors_planet = ['green', 'blue', 'olive drab', 'LightSkyBlue2']
colors_asteroid = ['burlywood3', 'gray53']
colors_star = ['red', 'yellow', 'gold', 'orange red']


def draw(obj: 'space_obj', r: 'float', color):
    width = int(obj.canvas.cget('width'))
    height = int(obj.canvas.cget('height'))
    scr_x = (width / 2) + obj.screen_coords()[0]
    scr_y = (height / 2) + obj.screen_coords()[1]
    if obj.id is None:
        obj.id = obj.canvas.create_oval(
            scr_x - r,
            scr_y - r,
            scr_x + r,
            scr_y + r,
            fill=color
        )
    else:
        obj.canvas.coords(
            obj.id,
            scr_x - r,
            scr_y - r,
            scr_x + r,
            scr_y + r
        )


class Planet(space_obj):
    def __init__(self, m, x, y, vx, vy, size, player, canvas):
        super().__init__(m, x, y, vx, vy, size, player, canvas)

        self.r = 6
        self.color = choice(colors_planet)

    def draw(self):
        draw(self, self.r, self.color)


class Asteroid(space_obj):
    def __init__(self, m, x, y, vx, vy, size, player, canvas):
        super().__init__(m, x, y, vx, vy, size, player, canvas)

        self.r = 3
        self.color = choice(colors_asteroid)

    def draw(self):
        draw(self, self.r, self.color)


class Star(space_obj):
    def __init__(self, m, x, y, vx, vy, size, player, canvas):
        super().__init__(m, x, y, vx, vy, size, player, canvas)

        self.r = 15
        self.color = choice(colors_star)

    def draw(self):
        draw(self, self.r, self.color)
