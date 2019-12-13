""" Contains class space_obj, parent class for space objects such as asteroids,
planets, etc """

from abc import abstractmethod
from random import uniform


class space_obj:
    def __init__(self, m, x, y, vx, vy, size, player, canvas):
        self.m = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        if player is None:
            player = self
        self.player = player
        self.force_x = 0
        self.force_y = 0
        self.key_force_x = 0
        self.key_force_y = 0
        self.canvas = canvas
        self.id = None
        # Satellites
        self.satellites = []
        self.satellite_of = None
        self.sat_num = None
        # Angular velocity
        self.omg = None
        # Absorbing
        self.absorbed = False
        self.rel_p = 1

    # Protected
    def screen_coords(self):
        return self.x - self.player.x, self.y - self.player.y

    @abstractmethod
    def draw(self):
        pass

    def move(self, dt):
        if self.satellite_of is None:
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.vx += self.force_x / self.m * dt
            self.vy += self.force_y / self.m * dt
            self.force_x = 0
            self.force_y = 0
        elif self.absorbed:
            # Test
            self.rel_p *= 0.9999
            #
            self.x = self.satellite_of.x + (
                    self.x - self.satellite_of.x) * self.rel_p
            self.y = self.satellite_of.y + (
                    self.y - self.satellite_of.y) * self.rel_p
            self.vx = self.satellite_of.vx - self.omg * (
                    self.y - self.satellite_of.y)
            self.vy = self.satellite_of.vy + self.omg * (
                    self.x - self.satellite_of.x)
            self.x += self.vx * dt
            self.y += self.vy * dt
        else:
            self.x += self.vx * dt
            self.y += self.vy * dt
            self.vx = self.satellite_of.vx - self.omg * (
                    self.y - self.satellite_of.y)
            self.vy = self.satellite_of.vy + self.omg * (
                    self.x - self.satellite_of.x)

    def add_satellite(self, obj):
        self.satellites.append(obj)

    # Experimental
    def set_orbit(self, obj):
        orbit_r0 = ((self.x - obj.x) ** 2 + (self.y - obj.y) ** 2) ** 0.5
        orbit_r = obj.m ** 0.5 + 10 * self.sat_num
        self.x = obj.x + (self.x - obj.x) * orbit_r / orbit_r0
        self.y = obj.y + (self.y - obj.y) * orbit_r / orbit_r0

    def become_satellite(self, obj):
        self.omg = uniform(0.005, 0.01) / (self.m ** 0.5)
        self.satellite_of = obj
        # Experimental
        self.sat_num = len(obj.satellites) + 1
        self.set_orbit(obj)
        for satellite in self.satellites:
            satellite.set_orbit(self)

    def consume(self):
        if len(self.satellites) != 0:
            self.satellites[len(self.satellites) - 1].absorbed = True
            self.increase(self.satellites.pop())

    # Trial
    def destroy(self, space_objects):
        if not (self.satellite_of is None):
            if self.satellite_of.satellites.count(self):
                self.satellite_of.satellites.remove(self)
        for satellite in self.satellites:
            satellite.satellite_of = None
        self.satellites.clear()
        space_objects.remove(self)
        self.canvas.delete(self.id)

    # Superfluity
    def increase(self, obj):
        self.m += obj.m

    def apply_force(self, force_x, force_y):
        self.force_x += force_x
        self.force_y += force_y

    def set_force(self, force_x, force_y):
        self.force_x = force_x
        self.force_y = force_y
