from PIL import ImageTk, Image


def fill_bg(bg_obj):
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x - bg_obj.w, bg_obj.y - bg_obj.h,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x, bg_obj.y - bg_obj.h,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x + bg_obj.w, bg_obj.y - bg_obj.h,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x - bg_obj.w, bg_obj.y,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(bg_obj.canvas.create_image(bg_obj.x, bg_obj.y,
                                                  anchor='nw',
                                                  image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x + bg_obj.w, bg_obj.y,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x - bg_obj.w, bg_obj.y + bg_obj.h,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x, bg_obj.y + bg_obj.h,
                                   anchor='nw',
                                   image=bg_obj.image))
    bg_obj.list.append(
        bg_obj.canvas.create_image(bg_obj.x + bg_obj.w, bg_obj.y + bg_obj.h,
                                   anchor='nw',
                                   image=bg_obj.image))


def set_bgcoords(bg_obj):
    bg_obj.canvas.coords(bg_obj.list[0], bg_obj.x - bg_obj.w,
                         bg_obj.y - bg_obj.h)
    bg_obj.canvas.coords(bg_obj.list[1], bg_obj.x, bg_obj.y - bg_obj.h)
    bg_obj.canvas.coords(bg_obj.list[2], bg_obj.x + bg_obj.w,
                         bg_obj.y - bg_obj.h)
    bg_obj.canvas.coords(bg_obj.list[3], bg_obj.x - bg_obj.w, bg_obj.y)
    bg_obj.canvas.coords(bg_obj.list[4], bg_obj.x, bg_obj.y)
    bg_obj.canvas.coords(bg_obj.list[5], bg_obj.x + bg_obj.w, bg_obj.y)
    bg_obj.canvas.coords(bg_obj.list[6], bg_obj.x - bg_obj.w,
                         bg_obj.y + bg_obj.h)
    bg_obj.canvas.coords(bg_obj.list[7], bg_obj.x, bg_obj.y + bg_obj.h)
    bg_obj.canvas.coords(bg_obj.list[8], bg_obj.x + bg_obj.w,
                         bg_obj.y + bg_obj.h)


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
        self.list = []
        self.w = int(self.canvas.cget('width'))
        self.h = int(self.canvas.cget('height'))

    def draw(self):
        if self.image_sprite is None:
            self.image_sprite = 1
            fill_bg(self)
        else:
            set_bgcoords(self)

    def move(self, dt):
        self.vx = - self.player.vx * self.k
        self.vy = - self.player.vy * self.k
        self.x += self.vx * dt
        self.y += self.vy * dt
        if self.x <= -self.w or self.x >= self.w:
            self.x = 0
        elif self.y <= -self.h or self.y >= self.h:
            self.y = 0
