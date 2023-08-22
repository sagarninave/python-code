x = "global"

def foo():
    print("x inside :", x)

foo()
print("x outside:", x)

x = "global"

def foo():
    x = x * 2
    print(x)
foo()
