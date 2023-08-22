class classOne:     

   def classOneMethod(self):
      print ('Calling class one method')

class classTwo(classOne):
   
   def classTwoMethod(self):
      print ('Calling class two method')

class classThree(classTwo):
   
   def classThreeMethod(self):
      print ('Calling class three method')

class classFour(classThree):
   
   def classFourMethod(self):
      print ('Calling class four method')

class Master(classFour):
   pass

c = Master()          
c.classOneMethod()      
c.classTwoMethod()     
c.classThreeMethod()   
c.classFourMethod()     
