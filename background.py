""" Class to contain, draw and move background """

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
        self.canv_objects = []
        self.w = int(self.canvas.cget('width'))
        self.h = int(self.canvas.cget('height'))

    def fill_bg(self):
        self.canv_objects.append(
            self.canvas.create_image(self.x - self.w, self.y - self.h,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x, self.y - self.h,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x + self.w, self.y - self.h,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x - self.w, self.y,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
	    self.canvas.create_image(self.x, self.y,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x + self.w, self.y,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x - self.w, self.y + self.h,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x, self.y + self.h,
                                     anchor='nw',
                                     image=self.image))
        self.canv_objects.append(
            self.canvas.create_image(self.x + self.w, self.y + self.h,
                                     anchor='nw',
                                     image=self.image))

    def set_bgcoords(self):
        self.canvas.coords(self.canv_objects[0], self.x - self.w,
                           self.y - self.h)
        self.canvas.coords(self.canv_objects[1], self.x, self.y - self.h)
        self.canvas.coords(self.canv_objects[2], self.x + self.w,
                           self.y - self.h)
        self.canvas.coords(self.canv_objects[3], self.x - self.w, self.y)
        self.canvas.coords(self.canv_objects[4], self.x, self.y)
        self.canvas.coords(self.canv_objects[5], self.x + self.w, self.y)
        self.canvas.coords(self.canv_objects[6], self.x - self.w,
                           self.y + self.h)
        self.canvas.coords(self.canv_objects[7], self.x, self.y + self.h)
        self.canvas.coords(self.canv_objects[8], self.x + self.w,
                           self.y + self.h)

    def draw(self):
        if self.image_sprite is None:
            self.image_sprite = 1
            self.fill_bg()
        else:
            self.set_bgcoords()

    def move(self, dt):
        self.vx = -self.player.vx * self.k
        self.vy = -self.player.vy * self.k
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.x <= -self.w or self.x >= self.w:
            self.x = 0
        elif self.y <= -self.h or self.y >= self.h:
            self.y = 0
