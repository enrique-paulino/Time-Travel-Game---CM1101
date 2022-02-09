from items import *

# P  stands for present whilst F stands for future

room_entranceP = {
    "name": "Entrance",

    "id": "Entrance",

    "description":
    """You are in a rectangular room with a shut iron door to your west and an opening to the east.""",

    "exits": {"east": "Corridor"},

    "items": []
}

room_corridorP = {
    "name": "Corridor",

    "id": "Corridor",

    "description":
    """You are in the facility corridor, You notice a small jasmine plant in the corner aswell as an exit in each compass direction except for east.""",

    "exits":  {"north": "Computer Lab", "south": "???", "west": "Entrance"},

    "items": []
}

room_labP = {
    "name": "Computer Lab",

    "id": "Computer Lab",

    "description":
    """As you walk in you notice a wall of computers and monitors as well as one massive monitor in the center of the north wall.
This technology looks more high tech than anything you've ever seen. On the massive monitor it says
'Radiation shielding over greenhouse inactive, arming key missing'""",

    "exits": {"south": "Corridor"},

    "items": []
}

room_deviceP = {
    "name": "???",

    "id": "???",

    "description":
    """You are standing in a spherical room with several gold and silver rings surrounding the center.
In the very center you notice a strange small device placed on a metal pedestal.""",

    "exits": {"north": "Corridor"},

    "items": [item_device]
}

room_conferenceP = {
    "name": "Conference Room",

    "id": "Conference Room",

    "description":
    """You cannot tell if this room is part of the facility or not, it looks like a completely normal conference room.
You notice a water bottle and a water fountain along one of the walls aswell as an exit to the north, east and south.""",

    "exits": {"north": "Green House", "east": "Dead end", "south": "Storage Room"},

    "items": [item_water]
}

room_gardenP = {
    "name": "Green House",

    "id": "Green House",

    "description":
    """You are standing in an empty green house with nothing but grass when it comes to flora. You notice a pile of fertilizer bags in the corner of the room.
The only way out is back the way you came to the south.""",

    "exits": {"south": "Conference Room"},

    "items": [item_fertilizer]
}

room_storageP = {
    "name": "Storage Room",

    "id": "Storage Room",

    "description":
    """You see shelves filled with dry dog food along all the walls aswell as water containers that go over the water fountain.
This would be enough for a dog to live off for years. You notice the storage room key is still in the lock.""",

    "exits": {"north": "Conference Room"},

    "items": []
}

room_dead_endP = {
    "name": "Dead end",

    "id": "Dead end",

    "description":
    """You're in a small corridor that leads to a locked door on the east side. It seems like its locked from the other side.
You notice a first aid kit on the wall""",

    "exits": {"west": "Conference Room"},

    "items": []
}

room_endgameP = {
    "name": "Square Room",

    "id": "Endgame Room",

    "description":
    """You're in a square room with various items laying around. A few look useful""",

    "exits": {},

    "items": [item_seeds, item_shovel, item_armingkey]
}

rooms = {
    "Entrance": room_entranceP,
    "Corridor": room_corridorP,
    "Computer Lab": room_labP,
    "???": room_deviceP,
    "Conference Room": room_conferenceP,
    "Green House": room_gardenP,
    "Storage Room": room_storageP,
    "Dead end": room_dead_endP,
    "Endgame Room": room_endgameP
    }
