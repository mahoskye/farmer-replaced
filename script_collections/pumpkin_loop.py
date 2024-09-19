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


while True:
    do_trade(16)
    make_move()
    plant_controller(Entities.Pumpkin)
