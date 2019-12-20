""" Function which calculate gravitation. Return force_x, force_y """
from phys_constants import *


def calculate_gravitation(obj1, obj2):
    """Calculate gravitation and return force_x, force_y acts on obj1"""
    if obj1.m * obj2.m  < min_mass2:
        return 0, 0
    r = ((obj1.x - obj2.x) ** 2 + (obj1.y - obj2.y) ** 2) ** 0.5
    # At a certain distance dependent on masses the objects don't
    # interact
    """ max_length = main_obj.m / obj.m * length_const
    if r > max_length:
       continue"""
    F = gravitational_constant * (obj1.m * obj2.m) / r ** 2
    return F * (obj2.x - obj1.x) / r, F * (obj2.y - obj1.y) / r
