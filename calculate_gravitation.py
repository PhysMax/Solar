""" Function which calculate gravitation. Return force_x, force_y """
from phys_constants import *


def calculate_gravitation(space_objects):
    """Calculate gravitation and return force_x, force_y"""
    for main_obj in space_objects:
        main_obj.force_x = 0
        main_obj.force_y = 0
        for obj in space_objects:
            # Object doesn't interact with yourself
            if main_obj == obj:
                continue
            if main_obj.m >= max_mass_ratio * obj.m:
                continue
            r = ((main_obj.x - obj.x) ** 2 + (main_obj.y - obj.y) ** 2) ** 0.5
            # At a certain distance dependent on masses the objects don't
            # interact
            """ max_length = main_obj.m / obj.m * length_const
            if r > max_length:
                continue"""
            F = gravitational_constant * (main_obj.m * obj.m) / r ** 2
            main_obj.force_x += F * (obj.x - main_obj.x) / r
            main_obj.force_y += F * (obj.y - main_obj.y) / r
