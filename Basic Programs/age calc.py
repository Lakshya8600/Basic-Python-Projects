age = int(input("enter you age or date of birth\n"))
if age < 100:
   a =  100 - age
   b = 2020 + a
   print("you will be at the age of 100 in the year",b)

elif age > 1900:
    a = age + 100
    print("you will be 100 yrs old in",a)
    yesno = str(input("do you want your age at a particular year\n"))
    if yesno == "yes":
        age2 = int(input("enter year\n"))
        print(age2-age)

    else:
        print("ok")

else:
    print("error: you are lieing")

