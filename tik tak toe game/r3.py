
global a
a = 3

def b():
    # global a
    a = 10
    print(a)

def c():
    # global a
    a = 20
    print(a)
    


b()   
print(a)
c()
print(a)