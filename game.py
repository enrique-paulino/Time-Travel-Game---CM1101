import changemap, map_one, map_two
import story_counters
import sys,time,random
import puzzle
from player import *
from gameparser import *
from mapvisual import printmap
from os import system,name

current_room = changemap.return_current_map().rooms["Entrance"]

def clear_chat():
    # Clears the chat
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def break_story():
    cont = input("\nEnter anything to continue\n> ")
    clear_chat()

def print_room_items(room):
    # Prints room items
    if len(room["items"]) != 0:
        print("There is " + list_of_items(room["items"]) + " here.")
        print("")
        return
    else:
        return

def print_room(room):
    # Prints the rooms name as well as its description
    print()
    print(room["name"].upper())
    print()
    # Display room description
    print(room["description"])
    print()
    print_room_items(room)

def exit_leads_to(exits, direction):
    # Returns the name of the exit in the specified direction
    return changemap.return_current_map().rooms[exits[direction]]["name"]

def print_exit(direction, leads_to):
    # Prints the exit available in the direction specified along with the room it leads to
    print("GO " + direction.upper() + " to " + leads_to + ".")

def list_of_items(items):
    # Creates a list of items based on the parameter sent

    itemsList = []

    for i in range(len(items)):
        itemsList.append(items[i]["name"])
    return (', '.join(itemsList))

def print_inventory_items(items):
    # Prints all of the users items
    if (len(inventory)) != 0:
        print("You have " + list_of_items(items) + ".")
        print("")
    else:
        return

def print_menu(exits, room_items, inv_items):
    # Prints the menu along with some styling to seperate inventory commands and movement commands
    divider=("+"+"-"*80+"+")
    print(divider)
    for direction in exits:
        put=str("Go "+direction.upper()+" to "+ exit_leads_to(exits,direction))
        addon=79-len(put)
        if addon<0:
            addon=0
        print("! "+put+" "*addon+"!")
    print(divider)
    for i in range (len(room_items)):
        put=str("TAKE "+(room_items[i]["id"]).upper()+" to take "+ room_items[i]["name"] + ".")
        addon=79-len(put)
        if addon<0:
            addon=0
        print("! "+put+" "*addon+"!")
    print(divider)
    for j in range (len(inv_items)):
        put=("DROP "+ (inv_items[j]["id"]).upper()+ " to drop "+ inv_items[j]["name"] + ".")
        addon=79-len(put)
        if addon<0:
            addon=0
        print("! "+put+" "*addon+"!")
        if inv_items[j]["id"] == "device" or inv_items[j]["id"] == "shovel":
            put=("USE "+ (inv_items[j]["id"]).upper()+ " to use "+ inv_items[j]["name"] + ".")
            addon=79-len(put)
            if addon<0:
                addon=0
            print("! "+put+" "*addon+"!")
    print(divider)


    print("What do you want to do?")

def execute_go(direction):
    # Sends the player into a different room based on their input of what direction they wanted to move
    # if there was no room in that direction it sends them back to their current room
    global current_room

    if direction in (current_room["exits"]):
        next_room = current_room["exits"][direction]
        current_room = changemap.return_current_map().rooms[next_room]
        clear_chat()
    else:
        print("You cannot go there.")
        break_story()
        current_room = current_room

def execute_take(item_id):
    # Removes item from the rooms inventory and puts it into the players one
    global current_room

    for i in current_room["items"]:
        if item_id == i["id"]:
            current_room["items"].remove(i)
            inventory.append(i)
            clear_chat()
            if item_id == "sapling" or item_id == "youngtree" or item_id == "seeds":
                print("You can plant this by 'drop'ing it in suitable soil.")
            return
    else:
        print("You cannot take that.")
        break_story()
        return

def execute_drop(item_id):
    # Drops item from inventory and adds it to the rooms items
    global current_room

    for i in inventory:
        if item_id == i["id"]:
            inventory.remove(i)
            current_room["items"].append(i)
            clear_chat()
            return

    else:
        print("You cannot drop that.")
        break_story()
        return

def execute_use(item_id):
    # Checks the item_id then does what the item is supposed to do, not a lot of items are interactable so this was a simple way of doing this
    if item_id == "device" and item_device in inventory:
        global current_room

        room_currently_in = current_room["id"]
        changemap.change_current_map()
        current_room = changemap.return_current_map().rooms[room_currently_in]
        story_counters.used_device = True
        print("You feel odd... time does not feel the same as it felt a moment ago...")
        break_story()

    elif item_id == "shovel" and story_counters.can_use_shovel == True:
        clear_chat()
        slow_type(story_counters.final_text)
        break_story()
        exit()

def execute_command(command):
    # This function splits the users input into separate words, the first is to decide which command will be executed, the second is sent as a
    # paramater for the commands function
    if 0 == len(command):
        break_story()
        return

    if command[0] == "go":
        if len(command) > 1:
            execute_go(command[1])
        else:
            print("Go where?")
            break_story()

    elif command[0] == "take":
        if len(command) > 1:
            execute_take(command[1])
        else:
            print("Take what?")
            break_story()

    elif command[0] == "drop":
        if len(command) > 1:
            execute_drop(command[1])
        else:
            print("Drop what?")
            break_story()

    elif command[0] == "use":
        if len(command) > 1:
            execute_use(command[1])
        else:
            print("Use what?")
            break_story()

    else:
        print("This makes no sense.")
        break_story()

def menu(exits, room_items, inv_items):
    print_menu(exits, room_items, inv_items)

    # Takes user input and normalises it and then returns it allowing for the player to type a larger range of responses
    user_input = input("> ")

    normalised_user_input = normalise_input(user_input)

    return normalised_user_input

def storyline():
    global current_room
    global puppy_name
    if story_counters.used_device == False and current_room == changemap.return_current_map().rooms["Computer Lab"]:
        slow_type(story_counters.entering_lab_without_device)
        current_room = changemap.return_current_map().rooms["Corridor"]
        break_story()

    elif story_counters.used_device == True and current_room == changemap.return_current_map().rooms["Computer Lab"] and story_counters.entering_lab_counter == 0:
        slow_type(story_counters.entering_lab_with_device)
        story_counters.entering_lab_counter += 1
        break_story()

    elif story_counters.entered_future_greenhouse == False and current_room == map_two.rooms["Green House"]:
        slow_type(story_counters.first_time_f_greenhouse)
        story_counters.entered_future_greenhouse = True
        break_story()

    elif story_counters.entered_feeding_ground == False and current_room == map_two.rooms["Dead end"]:
        slow_type(story_counters.feeding_ground_1)
        puppy_name = input("What would you like to name this puppy?\n> ")
        slow_type(story_counters.feeding_ground(puppy_name))
        story_counters.entered_feeding_ground = True
        inventory.append(item_puppy)
        changemap.change_current_map()
        current_room = map_one.rooms["Conference Room"]
        break_story()

    elif item_puppy in inventory and current_room == map_two.rooms["Dead end"]:
        slow_type(story_counters.danger(puppy_name))
        current_room = changemap.return_current_map().rooms["Conference Room"]
        break_story()

    elif current_room == map_one.rooms["Storage Room"] and item_puppy in inventory and story_counters.first_storage == False:
        slow_type(story_counters.storage_room(puppy_name))
        story_counters.first_storage = True
        inventory.remove(item_puppy)
        map_one.rooms["Storage Room"]["items"].append(item_puppy)
        map_one.rooms["Storage Room"]["description"] = "You see your puppy peacefully sleeping in the corner."
        break_story()

    elif current_room == map_two.rooms["Dead end"] and item_puppy not in inventory and story_counters.grown_puppy_enter == False:
        slow_type(story_counters.grown_puppy_feed(puppy_name))
        story_counters.grown_puppy_enter = True
        break_story()

    elif current_room == map_two.rooms["Green House"] and item_sapling in map_one.rooms["Green House"]["items"] and story_counters.sapling_planted == False:
        map_one.rooms["Green House"]["items"].remove(item_sapling)
        map_two.rooms["Green House"]["items"].append(item_youngtree)
        slow_type(story_counters.small_tree_pick_up)
        story_counters.sapling_planted = True
        break_story()

    elif current_room == map_two.rooms["Green House"] and item_youngtree in map_one.rooms["Green House"]["items"] and story_counters.tree_dropped == False:
        slow_type(story_counters.tree_return)
        break_story()

    elif current_room == map_one.rooms["Computer Lab"] and item_armingkey in inventory and story_counters.puzzle_completed == False:
        slow_type("You put the key into the empty lock...")
        slow_type("The computer starts making weird noises... a task presents itself...")
        puzzle.maingame()
        map_one.rooms["Computer Lab"]["description"] = story_counters.new_lab_desc
        map_two.rooms["Green House"]["description"] = story_counters.new_greenhouse_desc
        story_counters.tree_dropped = True
        story_counters.puzzle_completed = True
        inventory.remove(item_armingkey)
        break_story()

    elif story_counters.puzzle_completed == True and item_youngtree in map_one.rooms["Green House"]["items"]:
        map_one.rooms["Green House"]["items"].remove(item_youngtree)

    elif current_room == map_two.rooms["Green House"] and item_seeds in map_one.rooms["Green House"]["items"] and story_counters.puzzle_completed == True:
        map_two.rooms["Green House"]["description"] = story_counters.planted_seeds_desc
        story_counters.can_use_shovel = True


def main():

    while True: # After every command is done, this part of the code will print the menu along with the new options available to the player
        storyline()

        printmap(current_room["id"], False)
        print_room(current_room)
        print_inventory_items(inventory)

        # Show the menu with possible actions and ask the player
        command = menu(current_room["exits"], current_room["items"], inventory)

        # Execute the player's command
        execute_command(command)


# reference adapted from:
# https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing Mar 6 '13 at 4:02
# This code will simulate what it would look like if a real person was typing out the storyline.
def slow_type(text):
    typing_speed = 250
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(random.random()*10.0/typing_speed)
    print('')
# End reference ---------------------------------------------------------------------------------

if story_counters.intro == True:
    if __name__ == "__main__":
        main() # Will run the program
else:
    slow_type(story_counters.intro_text) # Will print the intro to the story
    story_counters.intro = True
    break_story()
    main()
