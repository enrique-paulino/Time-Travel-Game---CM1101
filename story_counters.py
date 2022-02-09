intro = False

intro_text = """Scientist: Alright C2053585, your mission is to explore this abandoned facility and return with intel. Remember, if you come back alive your sentence will be erased. This means you won't be C2053585 anymore, you'll be Kirill Sidorov once again.

The scientist nods at the guard holding onto your restraints and so the guard takes your restraints off, throws you into the facility entrance and closes the iron door.
You see the scientist through a small slit in the iron door.

Scientist: Once you've recovered enough intel we will open the door for you. Oh and just so you know… don't even think about running, the only way out is back through this iron door.

In and out as fast as you can and then you'll once again have the freedom you previously lost, sounds good.

You look around the room you're in
"""
# --------------------------------------------------------------------------------------------------------
used_device= False
entering_lab_counter = 0

entering_lab_without_device = """As you walk in an overwhelming scent of beer and piss hits you, as you stand there stunned you suddenly hear a voice from within the room.

Giant Squatter: Hey hold on a second, there's only one of them. I can take him.

He cracks his knuckles before you hear another voice.

Small Squatter: Hold your horses big guy. If he doesn't leave this place alive they will just send more people in here and then we won't be able to live here anymore.

Then a third voice interrupts.

Useless Squatter: What do you mean send more people?

Small Squatter: Just look at his orange jumpsuit. He must be with those crazy scientists that use convicted criminals as guinea pigs.

He turns to look at you.

Small Squatter: Listen here man, go back to where you came from and tell them theirs nothing interesting here, otherwise my friend over here won't be happy.

The giant squatter pushes you out of the room and back into the corridor.
"""

entering_lab_with_device = """As this room appears around you three squatters get up in shock and run out of the room

Small Squatter: Those crazy scientists must’ve given him special powers! RUN FOR YOUR LIVES!!

You watch them turn the corner in the corridor to run into the room you entered from.

A moment passes and you hear three gunshots followed by complete silence.
"""
# --------------------------------------------------------------------------------------------------------
entered_future_greenhouse = False

first_time_f_greenhouse = """You are stunned to see outside of this greenhouse, through the glass you see city ruins with no sign of living humanity in sight.

...

Wonderfull...

This is something you've dreamt of for years. Complete and utter freedom with no one telling you what to do and no expectations placed upon you.

A post-apocalyptic world.

However, You fear using the device and staying in the present time for too long in case the apocalypse is triggered whilst you're still around.
But you also know that it would be foolish not to prepare yourself for survival in this new world. So you plan to bring things from the past and affect the future so you have something to fall back on when you choose to permanently live in this new world.
you take a deep breath and you look around the room for any clues on where to start.
"""
# --------------------------------------------------------------------------------------------------------
entered_feeding_ground = False

feeding_ground_1 = """You realise the ceiling of this room is no more from the sweltering sun light beaming onto your skin.
As you take a step forward you hear the crunch of bones beneath your shoes.
Animal bones, unnaturally big, cover the entirety of the floor. You notice a small injured puppy unable to move in the centre of the room."""

def feeding_ground(puppy_name):

    return "It's a miracle ",puppy_name," survived this long, the apocalyptic event must've made dogs more resilient somehow.\nYou pick up ",puppy_name," planning to take him to safety but as you do a pack of big feral dogs attack. The biggest one attempts to bite at ",puppy_name," but you put your other arm in the way just in time. Before they attempt to attack a second time you're forced to use the device.\nYou feel odd... time does not feel the same as it felt a moment ago…\nYou grab a first aid kit you see on the wall and use it to patch your arm. You feel weird, this is the first time you've ever cared about any living thing other than yourself. You search for a suitable safe place to leave ",puppy_name," until you've prepared the new world for yourself."

# --------------------------------------------------------------------------------------------------------
def danger(puppy_name):
    return "You do not want to endanger " + puppy_name+ "."


# --------------------------------------------------------------------------------------------------------
first_storage = False

def storage_room(puppy_name):

    text = "You see shelves filled with dry dog food along all the walls as well as water containers that go over the water fountain. This would be enough for a dog to live off for years. You notice the storage room key is still in the lock.\nYou softly place " + puppy_name + " on the floor and you rip open one of the bags of dog food so it spills onto the floor. " + puppy_name + " spends some time eating the food until it's regained its energy. It then happily wags its tail whilst looking up at you. You are not sure what to do in this situation. \nAfter you stand there in confusion for what felt like a minute, " + puppy_name + " walks over to one of the water containers, jumps up and bites a hole into it.\nThe water slowly spills onto the floor and flows into an uneven part of the floor where " + puppy_name + " then drinks it."+ puppy_name + " should be fine here for awhile."

    return text

# --------------------------------------------------------------------------------------------------------

grown_puppy_enter = False
def grown_puppy_feed(puppy_name):
    text = "As you walk in the pack of feral dogs begin to growl. The biggest dog leaps at you in an attempt to attack you again however before it reaches you a dog much bigger shoves it out of the way. This huge dog roars at the pack who then jumps over the wall retreating.\nThe huge dog then turns around and takes a step towards you and then licks your face. It begins to wag its tail intensely whilst carrying a big smile on its face. It's "+puppy_name+".\n"+puppy_name+" then heads towards the conference room."

    return text
# --------------------------------------------------------------------------------------------------------
sapling_planted = False
small_tree_pick_up = "You notice there is now a young tree in the middle of the green house. It looks small enough to pick up"
# --------------------------------------------------------------------------------------------------------
tree_dropped = False
tree_return = "You notice the young tree is now much bigger however it seems to have been poisoned by the radiation."
# --------------------------------------------------------------------------------------------------------
puzzle_completed = False
new_lab_desc = "As you walk in you notice a wall of computers and monitors as well as one massive monitor in the center of the north wall.\nThis technology looks more high tech than anything you've ever seen. On the massive monitor it says:\n'Radiation shielding over greenhouse active'"
# --------------------------------------------------------------------------------------------------------
new_greenhouse_desc = "You are standing on the floor of the green house, This time the grass is luscious and alive.\nYou have succeeded in bringing living flora from the past and keeping it alive. You see a big tree in the centre of the green house.\nThe tree's roots must've uncovered an underground water deposit that have allowed the other flora to flourish, and the radiation shielding must’ve kept the plant life alive through the apocalypse."
planted_seeds_desc = new_greenhouse_desc+"\nYou also notice that potatoes have grown where you planted those seeds. You have successfully introduced human food into the new world.\n\nMaybe you could dig your way down to the water deposit so you have plenty of water..."
# --------------------------------------------------------------------------------------------------------
can_plant_seeds = False
can_use_shovel = False
use_shovel = False
# --------------------------------------------------------------------------------------------------------
final_text = "This is the final step, after you find water you will leave the past behind you and you will be free for the rest of your life.\n*You start digging.*\nThe puppy walks into the green house and lays behind you by your feet.\nNot only have you finally found freedom but you’ve found happiness as well. You come to the realisation that freedom is nothing without someone to share it with.\nYou dig your shovel into the ground one last time, and as you raise the shovel, water starts flowing out.\n\n fin."
