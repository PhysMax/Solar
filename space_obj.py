""" Contains class space_obj, parent class for space objects such as asteroids, planets, etc """


class space_obj:
    def __init__(self, m, x, y, vx, vy, size, player):
        self.m = m
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.size = size
        self.player = player
        self.force_x = 0
        self.force_y = 0

    # Protected
    def _screen_coords(self):
        return self.x - self.player.x, self.y - self.player.y

    @abstractmethod
    def draw(self):
        pass

    def move(self, dt):
        self.x += self.vx * dt
        self.y += self.vy * dt
        self.vx = self.force_x / self.m * dt
        self.vy = self.force_y / self.m * dt

    def apply_force(self, force_x, force_y):
        self.force_x += force_x
        self.force_y += force_y

    def set_force(self, force_x, force_y):
        self.force_x = force_x
        self.force_y = force_y
