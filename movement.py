def move_to(x, y):
    while get_pos_x() < x:
        if x - get_pos_x() > get_world_size() / 2:
            move(West)
        else:
            move(East)
    while get_pos_x() > x:
        if get_pos_x() - x > get_world_size() / 2:
           move(East)
        else:
           move(West)
    while get_pos_y() < y:
        if y - get_pos_y() > get_world_size() / 2:
            move(South)
        else:
            move(North)
    while get_pos_y() > y:
        if get_pos_y() - y > get_world_size() / 2:
            move(North)
        else:
            move(South)


