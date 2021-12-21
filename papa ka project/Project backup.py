import datetime

date = datetime.date.today()

def inputfunc(x):
    print("enter ",x)
    input12 = input()
    f = open("lk.txt","a")
    f.write(str(date))
    f.write("\n")
    f.write(input12)
    f.write("\n")

    print("Enter quantity and rate for Opening Stock of", input12 ,"respectively" )
    input13 = int(input("Quantity - "))
    input23 = int(input("Rate - "))
    amo1 = input13 * input23
    f.write("Opening stock - Quantity - ")
    f.write(str(input13))
    f.write("\n")
    f.write("              - Rate - ")
    f.write(str(input23))
    f.write("\n")
    f.write("              - Amount - ")
    f.write(str(amo1))
    f.write("\n")

    print("Enter quantity and rate for purchase of", input12 ,"respectively" )
    input14 = int(input("Quantity - "))
    input24 = int(input("Rate - "))
    amo2 = input14 * input24
    f.write("purchase - Quantity - ")
    f.write(str(input14))
    f.write("\n")
    f.write("         - Rate - ")
    f.write(str(input24))
    f.write("\n")
    f.write("         - Amount - ")
    f.write(str(amo2))
    f.write("\n")

    print("Enter quantity and rate for sale of", input12 ,"respectively" )
    input15 = int(input("Quantity - "))
    input25 = int(input("Rate - "))
    amo3 = input15 * input25
    f.write("Sale - Quantity - ")
    f.write(str(input15))
    f.write("\n")
    f.write("     - Rate - ")
    f.write(str(input25))
    f.write("\n")
    f.write("      - Amount - ")
    f.write(str(amo3))
    f.write("\n")

    CSA = (amo1 + amo2)- amo3
    CSQ = (input13 + input14) - input15
    CSR = (input23 + input24) - input25
    f.write("Closing Stock - Quantity - " )
    f.write(str(CSQ))
    f.write("\n")
    f.write("              - Rate - ")
    f.write(str(CSR))
    f.write("\n")
    f.write("              - Amount - ")
    f.write(str(CSA))
    f.write("\n")
    f.write("\n")
    print("\n")

    f.close()

if __name__ == "__main__":
    while(1):
        inputfunc("product name")

