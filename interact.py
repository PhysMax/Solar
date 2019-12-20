""" Interaction between objects """

from misc_obj import *
from calculate_gravitation import * 
from calc_collision import *

def act(obj1, obj2: 'space_obj'):
    """ Interact obj1 with other """
    F = calculate_gravitation(obj1, obj2)
    obj1.apply_force(F[0], F[1])
    obj2.apply_force(-F[0], -F[1])

    if obj1.check_collision(obj2):
       if obj1.satellite_of is None and obj2.satellite_of is None:
           v = calc_collision(obj1, obj2)
           obj1.vx = v[0]
           obj1.vy = v[1]
           obj2.vx = v[2]
           obj2.vy = v[3]

def interact(space_objects: 'list'):
    length = len(space_objects)
    i = 0
    for obj1 in space_objects:
        for j in range(i + 1, length):
            act(obj1, space_objects[j])
        i += 1
