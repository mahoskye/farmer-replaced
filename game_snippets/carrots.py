def carrots():
    if can_harvest():
        harvest()

    if num_items(Items.Carrot_Seed) < 1:
        trade(Items.Carrot_Seed)

    if get_ground_type() != Grounds.Soil:
        till()

    if get_entity_type() != Entities.Carrots:
        plant(Entities.Carrots)

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)
