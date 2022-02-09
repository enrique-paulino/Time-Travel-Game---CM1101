rods = {
    "l": [2],
    "m": [3],
    "r": [4,1]}

allowed = ["l","m","r"]

def print_rods(rods):
    print("l = ", rods["l"])
    print("m = ", rods["m"])
    print("r = ", rods["r"])


def input_check(user_input,allowed):
    test = user_input.lower()
    count = 0
    if len(test) == 2:
        for i in range(3):
            if allowed[i] in test:
                count+=1
        if count == 2:
            return True
        else:
            print("Not valid input, try again")
            return False
    else:
        print("Not valid input, try again")
        return False

def endcheck(rods):
    if len(rods["l"]) == 4 or len(rods["m"]) == 4 or len(rods["r"]) == 4:
        return False
    else:
        return True

def hhelp():
    print("Complete a full tower to look like this: ")
    print("[4,3,2,1]")
    print("And then you can proceed!")
    print()
    print("Typing 'lm' will move the number from the left to the middle")
    print("but only if the number at 'l' is smaller than the number at 'm'")

def hmove(user_input):
    global rods
    new = list(user_input)
    start = new[0]

    if not rods[start]:
        print("Doesn't fit! Try again")
        return None

    end = new[1]
    copy = rods[start][-1]

    if not rods[end]:
        rods[start].remove(copy)
        rods[end].append(copy)
    elif copy < rods[end][-1]:
        rods[start].remove(copy)
        rods[end].append(copy)
    else:
        print("Doesn't fit! Try again")
        return None

def maingame():
    hhelp()
    print_rods(rods)
    end = True
    while end:
        user_input = input("> ")
        while not input_check(user_input,allowed):
            user_input = input("> ")
        hmove(user_input)
        print_rods(rods)
        end = endcheck(rods)
    print("Well done! You've gained access!")
    return None


#lm,rm,rl,mr,ml,rl,mr,lr,lm,rm,rl,mr,ml,rl
