from navigate import * 
from inventory import *
from test import *
from planting import *
from harvesting import *
from mazesolver import *

# Define inventory min-max values



## Reset everything before running
clear()
# manage_inventory()
move_to(0, 0)


## Define the item to plant
item = "Grass"

if item == "Carrots":
    item = Entities.Carrots
    seed = Items.Carrot_Seed
elif item == "Pumpkins":
    item = Entities.Pumpkin
    seed = Items.Pumpkin_Seed
elif item == "Grass":
    item = Entities.Grass
elif item == "Tree":
    item = Entities.Tree
elif item == "Bush":
    item = Entities.Bush
elif item == "Sunflowers":
    item = Entities.Sunflower
    seed = Items.Sunflower_Seed

# while True:
#     manage_inventory()
#     run_maze_solver()

trade(Items.Egg, 50)
trade(Items.Cactus_Seed, 50)

while True:
    manage_inventory()
    # # set_farm_size(6)
    plant_dinosaurs()
    harvest_dinosaurs()
    # plant_cactus()
    # sort_cactus()
    # harvest_cactus()
    # # run_maze_solver()
    # # plant_sunflowers()
    # # plant_item(item)
    # # plant_turbo_trees()
    # # plant_turbo_pumpkins()
    # # polyculture()
    # # harvest_item()
    # quick_print(get_op_count())
