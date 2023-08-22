def argument(*args):
    total=0
    for n in args:
        total += n
    print(total)
    
number=[1,2,3,4,5,6,7,8,9,10]    #list of date 
argument(number[0],number[1],number[2],number[3],number[4],number[5],number[6],number[7],number[8],number[9]) #it is long process of unpacking
argument(*number)                #it is unpacked using star symbol

argument(2,435,253,67,23,54)
argument(200,400,600,800,1000)
argument(2345,4342,7654,2354,8985,7344)


def findAvg(*othernums):
    A=(sum(othernums))/(len(othernums))
    print('Average is:',A)
findAvg(10,20,30,40)
