clear()

PUMPKIN_PATCH_SIZE = 16
MOVE_DIR = North
CYCLE = 1
HIGHEST_FLOWER = 0
HF_x, HF_y = 0, 0

while True:
    do_trade(16)
    make_move()

    if get_entity_type() != Entities.Sunflower:
        sunflowers()

    if get_pos_x() == 0 and get_pos_y() == 0:
        CYCLE += 1
    if CYCLE % 2 == 0 and get_entity_type() == Entities.Sunflower:
        if measure() > HIGHEST_FLOWER:
            HIGHEST_FLOWER = measure()
            HF_x, HF_y = get_pos_x(), get_pos_y()
    elif CYCLE % 2 == 1 and get_entity_type() == Entities.Sunflower:
        if get_pos_x() == HF_x and get_pos_y() == HF_y:
            plant_controller(Entities.Sunflower)
            HIGHEST_FLOWER = 0
            HF_x, HF_y = 0, 0
            CYCLE = 1
