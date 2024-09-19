while True:
    do_trade(16)
    make_move()
    plant_controller(Entities.Cactus)

    if not get_cost(Unlocks.Dinosaurs) == None:
        if get_cost(Unlocks.Dinosaurs)[Items.Cactus] <= num_items(Items.Cactus):
            unlock(Unlocks.Dinosaurs)
# else:
#     break
