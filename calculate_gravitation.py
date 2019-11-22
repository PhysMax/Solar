""" Function which calculate gravitation. Return force_x, force_y """


gravitational_constant = 6.67E-11


def calculate_gravitation(space_objects):
    for main_obj in space_objects:
        for obj in space_objects:
            if main_obj == obj:
                continue
            r = (main_obj.x - obj.x) ** 2 + (main_obj.y - obj.y) ** 2
            F = gravitational_constant * (main_obj.m * obj.m) / r
            main_obj.force_x += F * (obj.x - main_obj.x) / (r ** 0.5)
            main_obj.rorce_y += F * (obj.y - main_obj.y) / (r ** 0.5)
