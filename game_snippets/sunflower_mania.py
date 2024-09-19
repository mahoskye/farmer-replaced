
def move_home():
    while get_pos_x() != 0:
        move(West)
    while get_pos_y() != 0:
        move(South)


def move_to(x, y):
    while get_pos_x() != x:
        move(East)
    while get_pos_y() != y:
        move(North)


def map_field():
    field = {}
    world_size = get_world_size()

    for x in range(world_size):
        for y in range(world_size):
            field[(x, y)] = measure()
            move(North)
        move(East)

    return field


def find_max_field(field_map):
    max_key = (0, 0)
    max_value = 0

    for key in field_map:
        if field_map[key] == None:
            continue
        if field_map[key] > max_value:
            max_key = key
            max_value = field_map[key]
    return max_key


move_home()
field_map = map_field()

while True:

    if not get_cost(Unlocks.Speed) == None:
        if get_cost(Unlocks.Speed)[Items.Power] <= num_items(Items.Power):
            unlock(Unlocks.Speed)

    max_field = find_max_field(field_map)
    m_x, m_y = max_field
    move_to(m_x, m_y)

    if can_harvest():
        harvest()
        while not can_harvest():
            do_trade()
            if num_items(Items.Fertilizer) < 1:
                trade(Items.Fertilizer, 100)
            use_item(Items.Fertilizer)
            if get_entity_type() != Entities.Sunflower:
                sunflowers()
        field_map[(get_pos_x(), get_pos_y())] = measure()
