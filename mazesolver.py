from movement import *
from planting import watering


## Drone facing directions
def turn_left(direction):
    if direction == North:
        return West
    elif direction == West:
        return South
    elif direction == South:
        return East
    elif direction == East:
        return North

def turn_right(direction):
    if direction == North:
        return East
    elif direction == East:
        return South
    elif direction == South:
        return West
    elif direction == West:
        return North



def summon_maze():
    while get_entity_type() != Entities.Hedge:
        watering()
        plant(Entities.Bush)
        use_item(Items.Fertilizer)
    
    if get_entity_type() == Entities.Hedge:
        return True
    else:
        return False


def harvest_treasure():
    if get_entity_type() == Entities.Treasure:
        harvest()
        return True


def solve(direction):
    if summon_maze():
        while get_entity_type() != Entities.Treasure:
            direction = turn_left(direction)
            if not move(direction):
                direction = turn_right(direction)
            if not move(direction):
                direction = turn_right(direction)
            else:
                direction = turn_left(direction)
                if not move(direction):
                    direction = turn_right(direction)
            


        harvest_treasure()

        


def run_maze_solver():
    direction = North

    solve(direction)
