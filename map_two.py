from items import *


#Future rooms start here

room_entranceF = {
    "name": "Worn Entrance",

    "id": "Entrance",

    "description":
    """You are in the same rectangular room as before but the iron door is now covered by debris that fell from the ceiling.""",

    "exits": {"east": "Corridor"},

    "items": []
}

room_corridorF = {
    "name": "Worn Corridor",

    "id": "Corridor",

    "description":
    """You find yourself in the facility corridor, but a lot more worn.
You notice that the previously small jasmine plant in the corner is now wilted and dead.
You also notice that aswell as the exits that were previously there, There is a opening in the east wall
that leads to another room which wasn't there before.""",

    "exits":  {"north": "Computer Lab", "east": "Conference Room", "south": "???", "west": "Entrance"},

    "items": []
}

room_labF = {
    "name": "Computer Lab",

    "id": "Computer Lab",

    "description":
    """As you walk in you notice that the wall of computers and moniters glow no more.""",

    "exits": {"south": "Corridor"},

    "items": []
}

room_deviceF = {
    "name": "Worn device room",

    "id": "???",

    "description":
    """You are standing in the same spherical room but a lot more dusty. You notice that the ceiling has collapsed in some parts of the room.""",

    "exits": {"north": "Corridor"},

    "items": []
}

room_conferenceF = {
    "name": "Worn Conference Room",

    "id": "Conference Room",

    "description":
    """You cannot tell if this room is part of the facility or not, it looks like a abandoned conference room.
You notice an exit to the north and an exit to the east aswell as a pile of rubble where it seems like an other exit should've been to the south.""",

    "exits": {"north": "Green House", "east": "Dead end", "west": "Corridor"},

    "items": []
}

room_gardenF = {
    "name": "Future Green House",

    "id": "Green House",

    "description":
    """You are standing on the floor of the green house, barren soil occasionally interuppted by wilted grass. If this is what flora looks like in a
completely isolated green house you fear what might've happened to all the flora open to the elements. You see that something has rotted in
the corner of the green house, this area is surrounded by more wilted grass than the rest of the room. Maybe there is hope for flora in this
place after all. You see that a small sapling has grown out of the rott.""",

    "exits": {"south": "Conference Room"},

    "items": [item_sapling]
}

room_storageF = {
    "name": "Worn Storage Room",

    "id": "Storage Room",

    "description":
    """You see shelves, previously filled with dog food and containers of water are now destroyed, the entrence to the north where rubble
now stands seems to have broken outwards, as if something huge broke out.""",

    "exits": {},

    "items": []
}

room_feeding_groundF = {
    "name": "Feeding ground",

    "id": "Dead end",

    "description":
    """You realise the ceiling of this room is no more from the sweltering sun light beaming onto your skin. As you take a step forward you
hear the crunch of bones beneath your shoes. Animal bones, unnaturally big, cover the entirety of the floor. You see another exit to the east.""",

    "exits": {"west": "Conference Room", "east": "Endgame Room"},

    "items": []
}

room_endgameF = {
    "name": "Empty square room",

    "id": "Endgame Room",

    "description":
    """You're in an empty square room, ashes cover the floor as if there was a fire in here""",

    "exits": {"west": "Dead end"},

    "items": []
}

rooms = {
    "Entrance": room_entranceF,
    "Corridor": room_corridorF,
    "Computer Lab": room_labF,
    "???": room_deviceF,
    "Conference Room": room_conferenceF,
    "Green House": room_gardenF,
    "Storage Room": room_storageF,
    "Dead end": room_feeding_groundF,
    "Endgame Room": room_endgameF
    }
