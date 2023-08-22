class classOne:     
   a=4

   def classOneMethod(self):
      print(self.a, "in class one")
      print ('Calling class one method')

class classTwo(classOne):
   
   def classTwoMethod(self):
      print(self.a,"in class 2")
      print ('Calling class two method')

class classThree(classOne):
   
   def classThreeMethod(self):
      print(self.a, "in class three")
      print ('Calling class three method')

class classFour(classTwo, classThree):
   
   def classFourMethod(self):
      print(self.a, "in class four")
      print ('Calling class four method')

c = classFour()          
c.classOneMethod()      
c.classTwoMethod()     
c.classThreeMethod()   
c.classFourMethod()     
