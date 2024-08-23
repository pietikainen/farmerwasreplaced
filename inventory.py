def manage_inventory():
    hay = Items.Hay
    hay_min = 100000
    hay_max = 500000

    wood = Items.Wood
    wood_min = 10000
    wood_max = 50000

    carrots = Items.Carrot
    carrots_min = 1000
    carrots_max = 5000

    pumpkins = Items.Pumpkin
    pumpkins_min = 1000
    pumpkins_max = 5000

    seeds_min = 101
    seeds_max = 400

    fertilizer_min = (get_world_size() * get_world_size() * 2)
    fertilizer_max = 4000

    water_tank_min = 10
    water_tank_max = 100

    # Check if we need to refill our water tank
    if num_items(Items.Water_Tank) < water_tank_min:
        trade(Items.Water_Tank, water_tank_max)
    # Check if we need to refill our Items.Fertilizer
    if num_items(Items.Fertilizer) < fertilizer_min:
        trade(Items.Fertilizer, fertilizer_max)
    # Check if we need to refill our seeds
    if num_items(Items.Carrot_Seed) < seeds_min:
        trade(Items.Carrot_Seed, seeds_max)
    if num_items(Items.Pumpkin_Seed) < seeds_min:
        trade(Items.Pumpkin_Seed, seeds_max)
    if num_items(Items.Sunflower_Seed) < seeds_min:
        trade(Items.Sunflower_Seed, seeds_max)
    if num_items(Items.Cactus_Seed) < seeds_min:
        trade(Items.Cactus_Seed, seeds_max)
    if num_items(Items.Egg) < seeds_min:
        trade(Items.Egg, seeds_max)





