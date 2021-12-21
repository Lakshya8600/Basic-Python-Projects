import random
playerpoint = 0
i = 0
compoint = 0
print("press \ns for snake\nw for water \ng for gun")
item = ["snake","water","gun"]
while i < 10:
    com = random.choice(item)
    player = input("enter your character\n")
    print("\n")
    print(f"computer's character {com}")
    if player == "s":
        print("your character is snake")
    elif player == "w":
        print("your character is water")
    elif player == "g":
        print("your character is gun")


    if com == "snake":
        if player == "s":
            print("tie")
            playerpoint = playerpoint + 1
            compoint = compoint + 1

        elif player == "w":
            print("computer's point")
            compoint = compoint + 1

        elif player == "g":
            print("players turn")
            playerpoint = playerpoint + 1

    elif com == "water":
        if player == "w":
            print("tie")
            playerpoint = playerpoint + 1
            compoint = compoint + 1

        elif player == "g":
            print("computer's point")
            compoint = compoint + 1

        elif player == "s":
            print("players turn")
            playerpoint = playerpoint + 1

    elif com == "gun":
        if player == "g":
            print("tie")
            playerpoint = playerpoint + 1
            compoint = compoint + 1

        elif player == "s":
            print("computer's point")
            compoint = compoint + 1

        elif player == "w":
            print("players turn")
            playerpoint = playerpoint + 1
    i = i + 1

print(f"computer's point - {compoint}")
print(f"player's point - {playerpoint}")

if compoint > playerpoint:
    print("computer won")

elif playerpoint > compoint:
    print("player won")