from navigate import *
from harvesting import *
from main import harvest_item

def watering():
    while get_water() < 0.99:
        use_item(Items.Water_Tank)

def plant_item(x):

    # Plant
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            
            if get_pos_y() == get_world_size() - 1:
                move(North)
                move_to(i, j)
            else:
                move_to(i, j)

            watering()
            if get_ground_type() == Grounds.Soil:
                plant(x)
            else:
                till()
                plant(x)
            # trade(Items.Carrot_Seed, 1)



def plant_turbo_trees():
    move_to(0, 0)

    # Plant
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_pos_y() == get_world_size() - 1:
                move(North)
                move_to(i, j)

            else:
                move_to(i, j)

            if get_entity_type() == Entities.Grass:
                harvest()
            watering()
            if (i + j) % 2 == 0:
                plant(Entities.Bush)
                use_item(Items.Fertilizer)
            else:
                plant(Entities.Tree)
                use_item(Items.Fertilizer)
    #     do_a_flip()
    # do_a_flip()
                

def plant_turbo_pumpkins():
    move_to(0, 0)

    trade(Items.Fertilizer, (get_world_size() * get_world_size() * 2))
    # Plant
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_pos_y() == get_world_size() - 1:
                move(North)
                move_to(i, j)
            else:
                move_to(i, j)

            if get_ground_type() != Grounds.Soil:
                till()

            watering()          

            while get_entity_type() == None:
                plant(Entities.Pumpkin)
                use_item(Items.Fertilizer)
                watering()
                trade(Items.Pumpkin_Seed, 1)
    
            # do_a_flip()

            # while get_entity_type() == None:
            #     plant(Entities.Pumpkin)
            #     trade(Items.Pumpkin_Seed, 1)
            #     watering()          
            #     use_item(Items.Fertilizer)
            #     break


def move_to_companion():
    while get_companion() != None:
        move_to(get_companion()[1], get_companion()[2])

def polyculture():
    move_to(0, 0)

    # Plant

    plant(Entities.Bush)
    friend = get_companion()
    quick_print("Friend: ", friend)
    quick_print("Friend[0]: ", friend[0])
    quick_print("Friend[1]: ", friend[1])
    quick_print("Friend[2]: ", friend[2])
    move_to(friend[1], friend[2])
    
    while friend != None:          
        till()
        # watering()
        plant(friend[0])
        quick_print("Planted", friend[0], "in", friend[1], friend[2])
        friend = get_companion()
        move_to(friend[1], friend[2])
        if get_pos_x() == friend[1] and get_pos_y() == friend[2]:
            harvest()
            plant(friend[0])


def plant_sunflowers():
    sunflowers = {}
    petals = 0

    move_to(0, 0)

    # Plant
    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_pos_y() == get_world_size() - 1:
                move(North)
                move_to(i, j)
            else:
                move_to(i, j)

            till()
            watering()
            plant(Entities.Sunflower)
            petals = measure()
            sunflowers[(i, j)] = petals

    quick_print("Sunflowers: ", sunflowers)

    harvest_sunflowers(sunflowers)


def plant_cactus():
    move_to(0, 0)

    # Plant

    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_pos_y() == get_world_size() - 1:
                move(North)
                move_to(i, j)
            else:
                move_to(i, j)

            if get_ground_type() != Grounds.Soil:
                till()
            watering()
            plant(Entities.Cactus)
            use_item(Items.Fertilizer)
    
    # sort_cactus()

def plant_dinosaurs():
    move_to(0, 0)

    # Plant

    for i in range(get_world_size()):
        for j in range(get_world_size()):
            if get_pos_y() == get_world_size() - 1:
                move(North)
                move_to(i, j)
            else:
                move_to(i, j)

            use_item(Items.Egg)
    
    # sort_cactus()





