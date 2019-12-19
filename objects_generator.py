from random import randint, choice, uniform

from misc_obj import *
from constants import *

space_objects = []


def generate(player, space_objects,  canv):
    """Generates the parameters of a new object"""
    x1 = round(uniform(player.x + window_width / 2, player.x + 2 * window_width))
    x2 = round(uniform(player.x - window_width / 2, player.x - 2 * window_width))
    x = choice([x1, x2])
    y1 = round(uniform(player.y + window_height / 2, player.y + 2 * window_height))
    y2 = round(uniform(player.y - window_height / 2, player.y - 2 * window_height))
    y = choice([y1, y2])
    print(x, y)
    """Speed always directed towards the player"""
    if x > player.x:
        vx = uniform(-0.005, 0)
    else:
        vx = uniform(0, 0.005)
    if y > player.x:
        vy = uniform(-0.005, 0)
    else:
        vy = uniform(0, 0.005)
    """Distribution of objects by type"""
    asteroids = ['asteroid'] * 5
    planets = ['planet'] * 3
    stars = ['star'] * 1
    type_obj = choice(asteroids + planets + stars)
    if type_obj == 'star':
        mass = randint(5000, 20000)
        obj = Star(mass, x, y, vx, vy, 10, player, canv)
    elif type_obj == 'planet':
        mass = randint(80, 300)
        obj = Planet(mass, x, y, vx, vy, 10, player, canv)
    else:
        mass = randint(1, 20)
        obj = Asteroid(mass, x, y, vx, vy, 10, player, canv)
    space_objects.append(obj)


def check_live_field(player, space_objects, quantity_obj,  canv):
    """Always generate definite quantity of objects"""
    while len(space_objects) <= quantity_obj:
        generate(player, space_objects, canv)
    for obj in space_objects:
        if abs(obj.x - player.x) > 3 * window_width or abs(obj.y - player.y) > 3 * window_height:
            obj.destroy(space_objects)
