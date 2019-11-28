from phys_constants import *


def type_definition(main_obj, obj):
    """Function compares types of space objects, Return True when active object (obj) equal or greater than
    main object (main_obj)."""

    if main_obj.type == "star":
        if obj.type == "star":
            return True
        else:
            return False
    if main_obj.type == "planet":
        if obj.type == "star" or "planet":
            return True
        else:
            return False
    if main_obj.type == "asteroid":
        return True


def calculate_gravitation(space_objects):
    """Calculate gravitation and return force_x, force_y"""
    for main_obj in space_objects:
        for obj in space_objects:
            # Object doesn't interact with yourself
            if main_obj == obj:
                continue
            if not type_definition(main_obj, obj):
                continue
            r = ((main_obj.x - obj.x) ** 2 + (main_obj.y - obj.y) ** 2) ** 0.5
            # At a certain distance dependent on masses the objects don't interact
            max_length = main_obj.m / obj.m * length_const
            if r > max_length:
                continue
            F = gravitational_constant * (main_obj.m * obj.m) / r ** 2
            main_obj.force_x += F * (obj.x - main_obj.x) / r
            main_obj.rorce_y += F * (obj.y - main_obj.y) / r
