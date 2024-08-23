from navigate import *

def harvest_item():

    if get_entity_type() == Entities.Pumpkin:
        harvest()
    else:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if get_pos_y() == get_world_size() - 1:
                    move(North)
                    move_to(i, j)

                else:
                    move_to(i, j)
                if can_harvest():
                    harvest()   

# sunflowers = {}
# petals = 0


def harvest_sunflowers(sunflowers):
    # Define max petals block from dictionary
    
    while True:
        trade(Items.Sunflower_Seed, 1)
        max_petals = 0
        for i in sunflowers:
            petals = sunflowers[i]
            if petals > max_petals:
                max_petals = petals
                x, y = i
        move_to(x, y)
        while not can_harvest():
            use_item(Items.Fertilizer)
        harvest()
        plant(Entities.Sunflower)
        petals = measure()
        sunflowers[(x, y)] = petals
        # move_to(0, 0)


        # If dictionary is empty, break
def safe_move(direction):
    if move(direction):
        return True
    else:
        return False


def sort_cactus():
    n = get_world_size()
    move_to(0, 0)

    for x in range(n):
        for i in range(n):        
            for j in range(0, n - i - 1):
                ## TODO: Check if there's a cactus to the North
                if measure() > measure(North):
                    swap(North)
                    safe_move(North)
                else:
                    safe_move(North)
        safe_move(East)

    for x in range(n):
        for i in range(n):        
            for j in range(0, n - i - 1):
                if measure() > measure(East):
                    swap(East)
                    safe_move(East)
                else:
                    safe_move(East)
        safe_move(North)        

def harvest_cactus():
    if get_entity_type() == Entities.Cactus and can_harvest():
        harvest()
    else:
        for i in range(get_world_size()):
            for j in range(get_world_size()):
                if get_pos_y() == get_world_size() - 1:
                    move(North)
                    move_to(i, j)

                else:
                    move_to(i, j)
                if can_harvest():
                    harvest()

def measure_dinosaurs():
    entity = measure()

    # Measure adjacent dinosaurs
    north = measure(North)
    east = measure(East)
    south = measure(South)
    west = measure(West)

    # Sum the adjacent dinosaurs
    sum = 0
    if north == entity:
        sum += 1
    if east == entity:
        sum += 1
    if south == entity:
        sum += 1
    if west == entity:
        sum += 1

    return sum

def harvest_dinosaurs():
    move_to(1,1)
    # Measure type of dinosaur below the drone
    for i in range(get_world_size()):
        for j in range(get_world_size()):

            if measure_dinosaurs() >= 4:
                harvest()
                use_item(Items.Egg)

            if get_pos_y() == get_world_size() - 1:
                move(North)
            
            move_to(i, j)
    

    
    
