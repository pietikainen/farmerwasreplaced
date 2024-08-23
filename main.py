from movement import * 
from inventory import *
from test import *
from planting import *
from harvesting import *
from mazesolver import *

## Reset playing field before running
clear()
move_to(0, 0)


## TODO: Refine general planting function to include "easy" items
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

## Debug mode: 0 = off, 1 = on
debug = 1


## Main loop
while True:
    manage_inventory()

    if debug == 1:
        set_execution_speed(5)
        set_farm_size(10)

    # plant_dinosaurs()
    # harvest_dinosaurs()
    # plant_cactus()
    # sort_cactus()
    # harvest_cactus()
    # # run_maze_solver()
    # # plant_sunflowers()
    # # plant_item(item)
    # # plant_turbo_trees()
    # # plant_turbo_pumpkins()
    polyculture()
    # # harvest_item()

    ## Debugging
    # quick_print(get_op_count())
