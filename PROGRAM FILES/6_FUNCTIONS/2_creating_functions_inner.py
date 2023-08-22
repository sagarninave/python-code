def function1(): # outer function  
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()

function1()



def function1(): # outer function  
    print ("Hello from outer function")
    def function2(): # inner function
        print ("Hello from inner function")
    function2()



def num1(x):  
   def num2(y):
      return x * y
   return num2
res = num1(10)

print(res(5))



def function1(): # outer function  
    x = 2 # A variable defined within the outer function
    def function2(a): # inner function
       # Let's define a new variable within the inner function
       # rather than changing the value of x of the outer function
        x = 6
        print (a+x)
    print (x) # to display the value of x of the outer function
    function2(3)

function1() 



def outer_function(x):  
    # Hidden from the outer code
    def inner_increment(x):
        return x + 2
    y = inner_increment(x)
    print(x, y)

#inner_increment(5)  
outer_function(5)

#########   Closures and Factory Functions


def function1(name):  
    def function2():
        print('Hello ' + name)
    return function2

func = function1('Nicholas')  
func()


def power_generator(num):

    # Create the inner function
    def power_n(power):
        return num ** power

    return power_n

power_two = power_generator(2)  
power_three = power_generator(3)  
print(power_two(8))  
print(power_three(4)) 
