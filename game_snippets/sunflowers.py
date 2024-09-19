

def sunflowers():
    if get_ground_type() != Grounds.Soil:
        till()

    if get_water() <= 0.25:
        use_item(Items.Water_Tank)

    if get_entity_type() != Entities.Sunflower:
        plant(Entities.Sunflower)
