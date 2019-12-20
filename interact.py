""" Interaction between objects """

from space_obj import *

def interact(space_objects: 'list'):
    length = len(space_objects)
    i = 0
    for obj1 in space_objects:
        for j in range(i + 1, length):
            obj1.act(space_objects[j])
        i += 1
