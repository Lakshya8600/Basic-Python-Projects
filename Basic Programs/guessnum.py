guesses = 1


while guesses <= 5:
    num = int(input("enter the number\n"))
    if num == 15:
        print("you won")
        break

    elif num > 15:
        print("number is greater")

    elif num < 15:
        print("number is smaller")

    guesses = guesses + 1
