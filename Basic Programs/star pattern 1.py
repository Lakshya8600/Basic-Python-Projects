inp = int(input("enter the number of rows\n"))
i = 0
j = 0
while j < inp:
    while i <= j:
        print("*", end="")
        i = i + 1
    j = j + 1
    print("")
    i = 0