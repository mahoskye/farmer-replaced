def action(pumpkin_patch_size=16):
    pumpkin_start = get_world_size() - (pumpkin_patch_size ** 0.5)

    if get_pos_x() < pumpkin_start:
        if get_pos_x() % 2 == 0 and get_pos_y() % 2 == 1:
            plant_controller(Entities.Tree)
        elif get_pos_x() % 2 == 1 and get_pos_y() % 2 == 0:
            plant_controller(Entities.Tree)
        else:
            if can_harvest():
                harvest()

    if get_pos_x() >= pumpkin_start:
        if get_pos_y() >= pumpkin_start:
            plant_controller(Entities.Pumpkin)
        else:
            if get_pos_y() >= (pumpkin_start / 2)-1:
                plant_controller(Entities.Carrots)
            else:
                if get_pos_y() >= ((pumpkin_start / 2)-1) / 2:
                    sunflowers()
                else:
                    harvest()
