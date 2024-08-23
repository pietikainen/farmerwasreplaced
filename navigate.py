def move_to(x, y):
    while get_pos_x() < x:
            if get_pos_x() - x > 5:
                move(West)
            else:
                move(East)
    while get_pos_x() > x:
            move(West)
    while get_pos_y() < y:
            move(North)
    while get_pos_y() > y:
            move(South)


