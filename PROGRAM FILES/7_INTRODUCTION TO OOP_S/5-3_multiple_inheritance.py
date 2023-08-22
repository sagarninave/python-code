class classOne:     

   def classOneMethod(self):
      print ('Calling class one method')

class classTwo():
   
   def classTwoMethod(self):
      print ('Calling class two method')

class classThree():
   
   def classThreeMethod(self):
      print ('Calling class three method')

class classFour():
   
   def classFourMethod(self):
      print ('Calling class four method')

class Master(classOne, classTwo, classThree, classFour):
   pass

c = Master()          
c.classOneMethod()      
c.classTwoMethod()     
c.classThreeMethod()   
c.classFourMethod()     
