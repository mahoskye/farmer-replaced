def create_maze():
    if get_entity_type() != Entities.Bush:
        plant(Entities.Bush)

    while get_entity_type() != Entities.Hedge:
        if num_items(Items.Fertilizer) < 1:
            trade(Items.Fertilizer, 100)
        use_item(Items.Fertilizer)


def find_treasure():
    directions = [North, East, South, West]
    index = 0

    while get_entity_type() != Entities.Treasure:
        move_attempts = [
            (index - 1) % 4,
            (index) % 4,
            (index + 1) % 4,
            (index + 2) % 4
        ]
        for i in range(len(move_attempts)):
            if move(directions[move_attempts[i]]):
                index = move_attempts[i]
                break


clear()

while True:
    if get_entity_type() != Entities.Hedge:
        create_maze()

    find_treasure()

    if get_entity_type() == Entities.Treasure:
        if can_harvest():
            harvest()

    clear()
