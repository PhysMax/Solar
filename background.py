from PIL import ImageTk, Image


class Background:
    def __init__(self, canvas, x, y, im_file, player):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.pilImage = Image.open(im_file)
        self.player = player

        self.image = ImageTk.PhotoImage(self.pilImage)
        self.image_sprite = None
        self.vx = 0
        self.vy = 0
        self.k = 0.01

    def draw(self):
        if self.image_sprite is None:
            self.image_sprite = self.canvas.create_image(self.x, self.y,
                                                         anchor='nw',
                                                         image=self.image)
        else:
            self.canvas.coords(self.image_sprite, self.x, self.y)

    def move(self, dt):
        self.vx = - self.player.vx * self.k
        self.vy = - self.player.vy * self.k
        self.x += self.vx * dt
        self.y += self.vy * dt
