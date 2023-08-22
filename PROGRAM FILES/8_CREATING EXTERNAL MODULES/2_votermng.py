from datetime import date
from module_Calculateage_for_votermng import cal_age
class Eligibility(Exception):
       pass
class Votermgm(Exception):
    def __init__(self, name,dob, city):
        self.name=name
        self.dob=dob
        self.city=city
    def check(self):
        try:
           if self.age[0]<18:
                raise Eligibility
           else:
                print('Person is Eligible')
                
        except Eligibility:
           print("person is not eligible")
          
      
    def display(self):
        print("    Voter Slip   ")
        print("Name of voter : ",self.name)
        print("date of birth : ",self.dob)
        print("Age  ",self.age[0],'years',self.age[1],'months',self.age[2],'days')
        print("City : ",self.city)
                
v1=Votermgm('Priyanka',date(1995,10,5),'nagpur')
v1.age=cal_age(v1.dob)
v1.display()
v1.check()
print()


