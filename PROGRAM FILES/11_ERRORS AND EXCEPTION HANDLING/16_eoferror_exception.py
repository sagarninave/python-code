try:
    x=input()
    if x == "" or x is not None:
        raise EOFError
        print(x)
except EOFError:
    print("enter Content")
