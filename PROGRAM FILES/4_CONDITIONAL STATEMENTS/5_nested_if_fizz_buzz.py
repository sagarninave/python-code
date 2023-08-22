for i in range(1,51):
    if (i%3==0 and i%5==0):
        print(i, "is fizz buzz")
    else:
        if(i%3==0 ):
            print(i, "is fizz")
        else:
            if(i%5==0):
                print(i, "is buzz")
            else:
                print(i)
