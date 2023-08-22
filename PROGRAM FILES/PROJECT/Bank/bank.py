import sqlite3
from datetime import datetime,date, time
import random

class bank:
    
    def __init__(self):
        
        self.bal=0
        
    def bankAccount(self):
        
        accountNo=random.randint(1000000000,9999999999)
        print('\nYOUR ACCOUNT NUMBER SUCCESSFULLY GENERATED\n ACCOUNT NUMBER : ',accountNo)
        firstName=str(input('FIRST NAME: '))
        middleName=str(input('MIDDLE NAME: '))
        lastName =str(input('LAST NAME: '))
        address =str(input('ADDRESS: '))
        phoneNo =int(input('MOBILE NUMBER: '))
        email =str(input('EMAIL ADDRESS: '))
        age =int(input('AGE: '))
        nationality =str(input('NATIONALITY: '))
        branch =str(input('NAME OF BRANCH: '))
        accountCreatingDate= date.today()
        accountCreatingTime= datetime.now().strftime("%X")
        
        con=sqlite3.connect('bank.db')
        c=con.cursor()
        data=(accountNo,firstName,middleName,lastName,address,phoneNo,email,age,nationality,branch,accountCreatingDate,accountCreatingTime)
        c.execute('INSERT INTO account VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',data)
        con.commit()
        con.close()

        print('\nYOUR ACCOUNT IS CREATED SUCCESSFULLY!!!')

        

    def bankAccountDetails(self):
        
        accountNo=str(input('ACCOUNT NUMBER : '))

        con=sqlite3.connect('bank.db')
        c=con.cursor()
        accountNoExist=c.execute("SELECT accountNo FROM account WHERE accountNo="+accountNo)

        if accountNoExist is not None:
            
            c.execute("SELECT accountNo, firstName, middleName, lastName, address, phoneNo, email, age, nationality, branch, accountCreatingDate, accountCreatingTime FROM account WHERE accountNo="+accountNo)
            print(c.fetchall())
        else:
            print('YOUR ACCOUNT DOES NOT EXIST!!! ')
            
        con.commit()
        con.close()

        
        
    def depositMoney(self):
        
        accountNo=str(input('ENTER YOUR ACCOUNT NUMBER: '))

        con=sqlite3.connect('bank.db')
        c=con.cursor()
        accountNoExist = c.execute("SELECT accountNo FROM account WHERE accountNo="+accountNo)
        con.commit()
        con.close()

        if accountNoExist is not None:
            
            depositId=random.randint(1000000000,9999999999)
            depositAmount=float(input('AMOUNT FOR DEPOSIT : '))
            depositMode=str(input('MODE OF PAYMENT (cash/cheque) : '))

            if depositMode == "CASH" or depositMode == "cash" or depositMode == "Cash":

                note_1000=str(input('1000 * NUMBER OD NOTES: '))
                note_500=str(input('500 * NUMBER OD NOTES : '))
                note_200=str(input('200 * NUMBER OD NOTES : '))
                note_100=str(input('100 * NUMBER OD NOTES : '))
                note_50=str(input('50 * NUMBER OD NOTES : '))
                note_20=str(input('20 * NUMBER OD NOTES :'))
                note_10=str(input('10 * NUMBER OD NOTES : '))

            elif depositMode == "CHEQUE" or depositMode == "cheque" or depositMode == "Cheque":

                chequeNo=str(input('CHEQUE NUMBER : '))
                chequeIssuerName=str(input('CHEQUE ISSUER NAME : '))
                bankOfChequeIssuer=str(input('BANK OF CHEQUE ISSUER : '))
                dateOfIssue=str(input('DATE OF CHEQUE ISSUED : '))

            else:

                print("PLEASE SELECT VALID PAYMENT MODE.")

            depositDate= date.today()
            
            con=sqlite3.connect('bank.db')
            c=con.cursor()

            if depositMode == "CASH" or depositMode == "cash" or depositMode == "Cash":

                depData=(depositId, depositAmount, depositMode, note_1000, note_500, note_200, note_100, note_50, note_20, note_10, depositDate, accountNo)
                c.execute('INSERT INTO deposit(depositId, depositAmount, depositMode, note_1000, note_500, note_200, note_100, note_50, note_20, note_10, depositDate, accountNo) VALUES(?,?,?,?,?,?,?,?,?,?,?,?)',depData)

            elif depositMode == "CHEQUE" or depositMode == "cheque" or depositMode == "Cheque":
                
                depData=(depositId, depositAmount, depositMode, chequeNo, chequeIssuerName, bankOfChequeIssuer, dateOfIssue, depositDate, accountNo)
                c.execute('INSERT INTO deposit(depositId, depositAmount, depositMode, chequeNo, chequeIssuerName, bankOfChequeIssuer, dateOfIssue, depositDate, accountNo) VALUES(?,?,?,?,?,?,?,?,?)',depData)

            con.commit()
            con.close()
            
        else:
            print("BANK ACCOUNT DOES NOT EXISTS")

            

    def withdrawMoney(self):
        accountNo=int(input('ENTER YOUR ACCOUNT NUMBER: '))
        withdrawAmt=float(input('ENTER THE AMOUNT TO WITHDRAW: '))
        if withdrawAmt<=(self.bal):
            print('You had withdrawn {} Rs'.format(withdrawAmt))
            self.bal=self.bal-withdrawAmt
            print('Total amount left is {} Rs'.format(self.bal))
        else:
            print('You don\'t have enough money')
            
        print('IN WHICH FORM?\n CASH  or  CHEQUE')
        witForm=str(input('ENTER YOUR CHOICE: '))
        dateW=date.today()
        con=sqlite3.connect('bank.db')
        c=con.cursor()
        witData=(withdrawAmt,witForm,dateW,accNo)
        c.execute('INSERT INTO withdraw VALUES(?,?,?,?)',witData)
        con.commit()
        con.close()
        


def main():
    b=bank()
    print('\tWELCOME TO\n\t*MI BANK* ')
    
    while 1:
        print('\n')
        print('1. CREATE NEW ACCOUNT')
        print("2. DEPOSIT AMOUNT")
        print("3. WITHDRAW AMOUNT")
        print("4. BANK ACCOUNT DETAILS")
        print("5. EXIT")
        
        choice=int(input('Enter your choice: '))
        
        if choice==1:
            b.bankAccount()
        elif choice==2:
            b.depositMoney()
        elif choice==3:
            b.withdrawMoney()
        elif choice==4:
            b.bankAccountDetails()
        else:
            print('THIS OPTION DOES NOT EXISTS')
        
        z=str(input('DO YOU WANT TO CONTINUE(y/n)?: '))
        
        if z=='y':
            continue
        else: 
            break
        
if __name__=='__main__':
    main()
