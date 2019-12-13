from random import randint, choice, uniform

from misc_obj import *
from constants import *

space_objects = []


def generate(player, space_objects,  canv):
    quantity_obj = 30  # Generate quantity of objects
    for i in range(1, quantity_obj + 1):
        """Generates the coordinate of a new object in a range of x and y """
        x1 = round(uniform(player.x + window_width / 2, player.x + window_width / 2 + 300))
        x2 = round(uniform(player.x - window_width / 2, player.x - window_width / 2 - 300))
        print(x1, x2)
        x = choice([x1, x2])
        y1 = round(uniform(player.y + window_height / 2, player.y + window_height / 2 + 300))
        y2 = round(uniform(player.y - window_height / 2, player.y - window_height / 2 - 300))
        y = choice([y1, y2])
        vx = uniform(-0.1, 0.1)
        vy = uniform(-0.1, 0.1)
        type_obj = choice(['asteroid', 'planet', 'star'])
        if type_obj == 'star':
            mass = uniform(5000, 20000)
            obj = Star(mass, x, y, vx, vy, 10, player, canv)
        elif type_obj == 'palnet':
            mass = uniform(80, 300)
            obj = Planet(mass, x, y, vx, vy, 10, player, canv)
        else:
            mass = uniform(1, 20)
            obj = Asteroid(mass, x, y, vx, vy, 10, player, canv)
        space_objects.append(obj)