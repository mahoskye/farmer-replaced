def tree():
    if can_harvest():
        harvest()

    if get_ground_type() != Grounds.Soil:
        till()

    if get_entity_type() != Entities.Tree:
        plant(Entities.Tree)

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)
