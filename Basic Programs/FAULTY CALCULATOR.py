print("enter the number")
input1 = int(input())

print("enter the number")
input3 = int(input())

print("enter the operator")
input2 = input()

if input1 == 43 and input3 == 53 and input2 == "*":
    print("111")

elif input1==11 and input3 == 86 and input3 == "/":
    print("45")

else:
    if input2 == "*":
        print(input1*input3)
    elif input2 == "/":
        print(input1/input3)
    elif input2 == "+":
        print(input1+input3)
    elif input2 == "-":
        print(input1-input3)