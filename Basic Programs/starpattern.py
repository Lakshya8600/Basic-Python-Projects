input = int(input("enter the number\n"))
int1 = "simple"
if int1 == "simple":
    i = 0
    j = 0
    while i <= input:
        while j < i:
            print("*", end="")
            j = j + 1
        print("")
        i = i + 1
        j = 0

elif int1 == "reverse":
    while i <= input:
        while i < j:
            print("*", end="")
            j = j - 1
        print("")
        i = i - 1
        j = 0


"""
i = 1
inp = 4
j = 1 
*


"""