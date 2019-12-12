def move_player(event, player):
    if event.keysym == 'w':
        player.key_force_y = -100
    if event.keysym == 's':
        player.key_force_y = 100
    if event.keysym == 'd':
        player.key_force_x = 100
    if event.keysym == 'a':
        player.key_force_x = -100


def stop_player(event, player):
    if event.keysym == 'w' or 's':
        player.key_force_y = 0
    if event.keysym == 'd' or 'a':
        player.key_force_x = 0


