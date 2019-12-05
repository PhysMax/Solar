""" Catching satellites """

from misc_obj import *


def catch_satellite(main_obj, obj, max_distance, max_speed):
    if (main_obj.x - obj.x) ** 2 + (
            main_obj.y - obj.y) ** 2 < max_distance ** 2:
        if (main_obj.vx - obj.vx) ** 2 + (
                main_obj.vy - obj.vy) ** 2 < max_speed ** 2:
            main_obj.add_satellite(obj)
            obj.become_satellite(main_obj)


def satellites_formation(space_objects):
    for main_obj in space_objects:
        if isinstance(main_obj, Planet):
            for obj in space_objects:
                if isinstance(obj, Asteroid):
                    if obj.satellite_of is None and obj != obj.player:
                        catch_satellite(main_obj, obj, 50, 0.5)
        elif isinstance(main_obj, Star):
            for obj in space_objects:
                if isinstance(obj, Planet):
                    if obj.satellite_of is None and obj != obj.player:
                        catch_satellite(main_obj, obj, 100, 0.7)
