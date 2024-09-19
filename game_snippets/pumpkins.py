def pumpkins():
    if can_harvest():
        harvest()

    if num_items(Items.Pumpkin_Seed) < 1:
        trade(Items.Pumpkin_Seed)

    if get_ground_type() != Grounds.Soil:
        till()

    if get_entity_type() != Entities.Pumpkin:
        plant(Entities.Pumpkin)

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)
