def make_move():
    WORLD_SIZE = get_world_size()
    if get_pos_y() == WORLD_SIZE - 1:
        move(East)
    move(North)
