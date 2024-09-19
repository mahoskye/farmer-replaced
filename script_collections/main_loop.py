clear()

PUMPKIN_PATCH_SIZE = 16
MOVE_DIR = North
CYCLE = 1
HIGHEST_FLOWER = 0
HF_x, HF_y = 0, 0


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


def do_trade(pumpkin_patch_size=16):
    purchases = [
        [Items.Carrot_Seed, (pumpkin_patch_size / 2)],
        [Items.Pumpkin_Seed, pumpkin_patch_size],
        [Items.Sunflower_Seed, 9],
        [Items.Cactus_Seed, 9],
        [Items.Fertilizer, 10],
        [Items.Empty_Tank, 100],
    ]

    for purchase in purchases:
        items_in_stock = num_items(purchase[0])
        if items_in_stock < purchase[1]:
            trade(purchase[0], purchase[1] - items_in_stock)


def make_move():
    WORLD_SIZE = get_world_size()
    if get_pos_y() == WORLD_SIZE - 1:
        move(East)
    move(North)


def plant_controller(to_plant):
    if can_harvest():
        harvest()

    if get_ground_type() != Grounds.Soil:
        till()

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)

    if get_entity_type() != to_plant:
        plant(to_plant)


def sunflowers():
    if get_ground_type() != Grounds.Soil:
        till()

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)

    if get_entity_type() != Entities.Sunflower:
        plant(Entities.Sunflower)


while True:
    do_trade(PUMPKIN_PATCH_SIZE)
    action(PUMPKIN_PATCH_SIZE)
    make_move()
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
