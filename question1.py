#Task 1: Code correction
place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    else: action = "cross a river"
    print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")
else: #Task 3
    pass
#Task 2
if place == "cave":
    action = input("light a torch or proceed in the dark?")
    if action == "light a torch":
        print("You can see in the cave!")
    elif action == "proceed in the dark":
        print("You can't anything.")
