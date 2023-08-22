class student:
    def __init__(self,n,r,s,y):
        self.name = n
        self.rollno = r
        self.sem = s
        self.year = y
        
    def disp(self):
        print("The student",self.name,"has roll no",self.rollno,"and studies in semester",self.sem,"year",self.year)
  
s1=student("pinka",17,4,2)      
s1.disp()

s2=student("pranita",16,4,2)
s2.disp()
s2.marks=100
print("student marks:",s2.marks)
#print("student marks:",s1.marks)

