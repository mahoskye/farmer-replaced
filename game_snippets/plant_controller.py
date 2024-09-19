def plant_controller(to_plant):
    if can_harvest():
        harvest()

    if get_ground_type() != Grounds.Soil:
        till()

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)

    if get_entity_type() != to_plant:
        plant(to_plant)
