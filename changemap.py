import map_one, map_two
import player

list_of_maps = [map_one,map_two]
num = 1

def change_current_map():
    if player.map_state == True:
        player.map_state = False
    else:
        player.map_state = True
    return

def return_current_map():
        if player.map_state == True:
            return list_of_maps[0]
        else:
            return list_of_maps[1]
