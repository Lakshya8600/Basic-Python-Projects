inp1 = input("enter your number\n")
inp2 = input("enter your number\n")
#if we will entered the input as a string the compiler will test the statement
#if it is false it will move on to the except statement and go on

try:
    print(int(inp1)+int(inp2))

except Exception as e:
    print(e)

print("you are outside the statement")
