list=[1,2,3,[4,5],['pinka','xyz'],3.5,7.3]
for i in range(0,len(list)):
        if type(list[i])==int or type(list[i])==float or type(list[i])==str:
            print(list[i])
        else:
            for j in range(0,len(list[i])):
                print(list[i][j])
            
