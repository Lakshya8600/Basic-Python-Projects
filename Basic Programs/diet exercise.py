input1 = input("enter your name\n")
if input1 == "lakshya":
    input11 = input("enter your plan\n")
    if input11 == "exercise":
        f1 = open("lkexe.txt","rt")
        a = f1.read()
        print(a)
        f1.close()

    elif input11 == "diet":
        f2 = open("lkdiet.txt","rt")
        a = f2.read()
        print(a)
        f2.close()

elif input1 == "yash":
    input11 = input("enter your plan\n")
    if input11 == "exercise":
        f3 = open("ykexe.txt","rt")
        a = f3.read()
        print(a)
        f3.close()

    elif input11 == "diet":
        f4 = open("ykdiet")
        a = f4.read()
        print(a)
        f4.close()
