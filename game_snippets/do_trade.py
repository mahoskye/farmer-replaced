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
        # if nums_unlocked(Unlocks.Multi_Trade) > 0:
        if items_in_stock < purchase[1]:
            trade(purchase[0], purchase[1] - items_in_stock)
        # else:
        #     for i in range(purchase[1]):
        #        trade(purchase[0])
