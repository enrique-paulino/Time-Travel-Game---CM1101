import changemap

#checks map state and prints correct map
def printmap(room, isdooropen):
    whatmap = changemap.return_current_map()
    if whatmap == changemap.map_one:
        printPmap(room, isdooropen)
    else:
        printFmap(room)
        gonetofuture()

#a list acting as a counter
counter = []

#a function that adds an item to the 'counter' list everytime its called
def gonetofuture():
    counter.append("")

#prints your location in the future room
def printFmap(room):
    frm = {               #frm stands for future room markers
        "a" : " ",        #all the markers on the maptest
        "A" : " ",        #there are 9 rooms and each "You are here" icon
        "b" : " ",        #requires 2 markers
        "B" : " ",
        "c" : " ",
        "C" : " ",
        "d" : " ",
        "D" : " ",
        "e" : " ",
        "E" : " ",
        "f" : " ",
        "F" : " ",
        "g" : " ",
        "G" : " ",
        "h" : " ",
        "H" : " ",
        "i" : " ",
        "I" : " ",
        }
#changes the frm values of the room you're in to those of the icon parts
    if room == "Entrance":
        frm["a"] = "o"
        frm["A"] = "╵"

    elif room == "Computer Lab":
        frm["b"] = "o"
        frm["B"] = "╵"

    elif room == "Corridor":
        frm["c"] = "o"
        frm["C"] = "╵"

    elif room == "???":
        frm["d"] = "o"
        frm["D"] = "╵"

    elif room == "Green House":
        frm["e"] = "o"
        frm["E"] = "╵"

    elif room == "Conference Room":
        frm["f"] = "o"
        frm["F"] = "╵"

    elif room == "Storage Room":
        frm["g"] = "o"
        frm["G"] = "╵"

    elif room == "Dead end":
        frm["h"] = "o"
        frm["H"] = "╵"

    elif room == "Endgame Room":
        frm["i"] = "o"
        frm["I"] = "╵"

#prints the future map
    print("                              ┌───────────┐")
    print("              ┌─────┐         │     "+frm["e"]+"     │"+" "*27+"Future")
    print("              │  "+frm["b"]+"  │         │     "+frm["E"]+"     │")
    print("              │  "+frm["B"]+"  │         └────┐ ┌────┘")
    print("              └──┐ ┌┘   ┌──────────┘ └──────────┐                 ┌─────────┐")
    print(" ┌───────────┐  ┌┘ └┐   │                       │  ┌───────────┐  │         │")
    print(" │     "+frm["a"]+"     └──┘ "+frm["c"]+" └───┘           "+frm["f"]+"           └──┘     "+frm["h"]+"     └──┘    "+frm["i"]+"    │")
    print(" │     "+frm["A"]+"     ┌──┐ "+frm["C"]+" ┌───┐           "+frm["F"]+"           ┌──┐     "+frm["H"]+"     ┌──┐    "+frm["I"]+"    │")
    print(" └───────────┘  └┐ ┌┘   │                       │  └───────────┘  │         │")
    print("               ┌─┘ └─┐  └───────────────────────┘                 └─────────┘")
    print("             ┌─┘     └─┐         ┌─────┐")
    print("            ┌┘    "+frm["d"]+"    └┐        │  "+frm["g"]+"  │")
    print("            └┐    "+frm["D"]+"    ┌┘        │  "+frm["G"]+"  │")
    print("             └─┐     ┌─┘         └─────┘")
    print("               └─┐_┌─┘")


#prints your location in the present room
def printPmap(room, isdooropen):
    prm = {               #prm stands for present room markers
        "a" : " ",        #all the markers on the maptest
        "A" : " ",        #there are 9 rooms and each "You are here" icon
        "b" : " ",        #requires 2 markers
        "B" : " ",
        "c" : " ",        #prm also inclusde the dooropen icons to show if
        "C" : " ",        #the door is open or closed on the map
        "d" : " ",
        "D" : " ",
        "e" : " ",
        "E" : " ",
        "f" : " ",
        "F" : " ",
        "g" : " ",
        "G" : " ",
        "h" : " ",
        "H" : " ",
        "i" : " ",
        "I" : " ",
        "j" : "┬",
        "J" : "┴",
        }
#changes the prm values of the room you're in to those of the icon parts
    if room == "Entrance":
        prm["a"] = "o"
        prm["A"] = "╵"

    elif room == "Computer Lab":
        prm["b"] = "o"
        prm["B"] = "╵"

    elif room == "Corridor":
        prm["c"] = "o"
        prm["C"] = "╵"

    elif room == "???":
        prm["d"] = "o"
        prm["D"] = "╵"

    elif room == "Green House":
        prm["e"] = "o"
        prm["E"] = "╵"

    elif room == "Conference Room":
        prm["f"] = "o"
        prm["F"] = "╵"

    elif room == "Storage Room":
        prm["g"] = "o"
        prm["G"] = "╵"

    elif room == "Dead end":
        prm["h"] = "o"
        prm["H"] = "╵"

    elif room == "Endgame Room":
        prm["i"] = "o"
        prm["I"] = "╵"

#if the door between room 8 and 9 has been unlocked the map visual will change
    if isdooropen == True:
        prm["j"] = "─"
        prm["J"] = "─"

#the lines that comprise the hidden part of the present map
    lx = {
        "l1" : "",
        "l2" : "",
        "l3" : "",
        "l4" : "",
        "l5" : "",
        "l6" : "",
        "l7" : "",
        "l8" : "",
        "l9" : "",
        "l10" : "",
        "l11" : "",
        "l12" : "",
        "l13" : "",
        "l14" : "",
    }

#adds the rest of the map if the future map has been printed
    if len(counter) >0:
        lx["l1"] =  "                              ┌───────────┐"
        lx["l2"] =  "         │     "+prm["e"]+"     │"+" "*26+"Present"
        lx["l3"] =  "         │     "+prm["E"]+"     │"
        lx["l4"] =  "         └────┐ ┌────┘"
        lx["l5"] =  "   ┌──────────┘ └──────────┐                 ┌─────────┐"
        lx["l6"] =  "   │                       │  ┌───────────┐  │         │"
        lx["l7"] =  "   │           "+prm["f"]+"           └──┘     "+prm["h"]+"     └─"+prm["j"]+"┘    "+prm["i"]+"    │"
        lx["l8"] =  "   │           "+prm["F"]+"           ┌──┐     "+prm["H"]+"     ┌─"+prm["J"]+"┐    "+prm["I"]+"    │"
        lx["l9"] =  "   │                       │  └───────────┘  │         │"
        lx["l10"] = "  └──────────┐ ┌──────────┘                 └─────────┘"
        lx["l11"] = "         ┌─┘ └─┐"
        lx["l12"] = "        │  "+prm["g"]+"  │"
        lx["l13"] = "        │  "+prm["G"]+"  │"
        lx["l14"] = "         └─────┘"

#prints the present map
    print(""+lx["l1"])
    print("              ┌─────┐"+lx["l2"])
    print("              │  "+prm["b"]+"  │"+lx["l3"])
    print("              │  "+prm["B"]+"  │"+lx["l4"])
    print("              └──┐ ┌┘"+lx["l5"])
    print(" ┌───────────┐  ┌┘ └┐"+lx["l6"])
    print(" │     "+prm["a"]+"     └──┘ "+prm["c"]+" │"+lx["l7"])
    print(" │     "+prm["A"]+"     ┌──┐ "+prm["C"]+" │"+lx["l8"])
    print(" └───────────┘  └┐ ┌┘"+lx["l9"])
    print("               ┌─┘ └─┐"+lx["l10"])
    print("             ┌─┘     └─┐"+lx["l11"])
    print("            ┌┘    "+prm["d"]+"    └┐"+lx["l12"])
    print("            └┐    "+prm["D"]+"    ┌┘"+lx["l13"])
    print("             └─┐     ┌─┘"+lx["l14"])
    print("               └─┐_┌─┘")
