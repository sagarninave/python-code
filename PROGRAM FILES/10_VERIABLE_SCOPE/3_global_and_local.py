x = "global"

def foo():
    global x
    y = "local"
    x = x * 2
    print(x)
    print(y)
    
foo()




x = 5

def foo():
    x = 10
    print("local x:", x)

foo()
print("global x:", x)
