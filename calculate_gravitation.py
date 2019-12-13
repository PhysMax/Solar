""" Function which calculate gravitation. Return force_x, force_y """
from constants import *

def calculate_gravitation(space_objects):
    for main_obj in space_objects:
        main_obj.force_x = 0
        main_obj.force_y = 0
        for obj in space_objects:
            if main_obj == obj:
                continue
            r = ((main_obj.x - obj.x) ** 2 + (main_obj.y - obj.y) ** 2) ** 0.5
            F = gravitational_constant * (main_obj.m * obj.m) / r ** 2
            main_obj.force_x += F * (obj.x - main_obj.x) / r
            main_obj.force_y += F * (obj.y - main_obj.y) / r
