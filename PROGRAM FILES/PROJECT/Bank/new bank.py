class bank:
    def __init__(self):
        self.bal=0
        
    def create(self):
        global name,p
        name=str(input('Enter your name: '))
        str(input('Enter your dob: '))
        str(input('Enter your address: '))  
        str(input('What type of account you want to open\nsavings(s) or current(c): '))
        print('\nYOUR ACCOUNT IS CREATED.')
        
    def balance(self):
        print('Your current balance is: {} Rs'.format(self.bal))
         
    def deposit(self):
        p=int(input('Enter the amount you want to deposit:\n'))
        print('Your {} Rs have been deposited successfully'.format(p))
        self.bal=self.bal+p
        print('Your current balance is {} Rs '.format(self.bal))
          
        
    def withdraw(self):
        m=int(input('Enter the amount you want to withdraw:\n'))
        if m<=(self.bal):
            print('You had withdrawn {} Rs'.format(m))
            self.bal=self.bal-m
            print('Total amount left is {} Rs'.format(self.bal))
        else:
            print('You don\'t have enough money')
                       
def main():
    b=bank()
    
    while 1:
        
        print('\n\tMi BANK:)\n')
        print('1. CREATE NEW ACCOUNT \n2. BALANCE ENQUIRY \n3. CASH DEPOSIT \n4. CASH WITHDRAW \n5. EXIT ')
        a=int(input('Enter your choice: '))
        
        if a==1:
            print('\nYour account number is 8888')
            b.create()
    
        elif a==2:
            b.balance()          
    
        elif a==3:
            b.deposit()          
    
        elif a==4:
            b.withdraw()           
            
        else:
            print("Invalid Option")

        z=str(input('do you want to continue(y/n): '))

        if z=='y':
            continue
        else: 
            print('Thank you!!')
            break
           
            
if __name__=='__main__':
    main()
