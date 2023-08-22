import sqlite3
con=sqlite3.connect('bank.db')
c=con.cursor()
# c.execute(
    
#     '''CREATE TABLE account(
#             accountNo NUMERIC PRIMARY KEY UNIQUE NOT NULL,
#             firstName VARCHAR NOT NULL,
#             middleName VARCHAR NOT NULL,
#             lastName VARCHAR NOT NULL,
#             address TEXT NOT NULL,
#             phoneNo VARCHAR NOT NULL,
#             email VARCHAR NOT NULL,
#             age INTEGER NOT NULL,
#             nationality VARCHAR NOT NULL,
#             branch VARCHAR NOT NULL,
#             accountCreatingDate VARCHAR NOT NULL,
#             accountCreatingTime VARCHAR NOT NULL)'''
#     )

c.execute(

    '''CREATE TABLE deposit(
            depositId NUMERIC PRIMARY KEY UNIQUE,
            depositAmount FLOAT(10,2) NOT NULL,
            depositMode VARCHAR NOT NULL,
            chequeNo VARCHAR,
            chequeIssuerName VARCHAR,
            bankOfChequeIssuer VARCHAR,
            dateOfIssue VARCHAR,
            chequeExpiringDate VARCHAR,
            note_1000 VARCHAR,
            note_500 VARCHAR,
            note_200 VARCHAR,
            note_100 VARCHAR,
            note_50 VARCHAR,
            note_20 VARCHAR,
            note_10 VARCHAR,
            depositDate VARCHAR NOT NULL,
            accountNo NUMERIC NOT NULL,
            FOREIGN KEY (accountNo) REFERENCES account (acccountNo))'''
    )
# c.execute(

#     '''CREATE TABLE withdraw(
#             withdrawId NUMERIC PRIMARY KEY UNIQUE NOT NULL,
#             withdrawAmount FLOAT(10,2) NOT NULL,
#             withdrawMode VARCHAR NOT NULL,
#             chequeNo VARCHAR,
#             chequeIssuerName VARCHAR,
#             chequeGivenTo VARCHAR,
#             bankOfChequeIssuer VARCHAR,
#             dateOfIssue VARCHAR,
#             chequeExpiringDate VARCHAR,
#             note_1000 VARCHAR,
#             note_500 VARCHAR,
#             note_200 VARCHAR,
#             note_100 VARCHAR,
#             note_50 VARCHAR,
#             note_20 VARCHAR,
#             note_10 VARCHAR,
#             withdrawDate VARCHAR NOT NULL,
#             withdrawTime VARCHAR NOT NULL,
#             accountNo NUMERIC NOT NULL,
#             FOREIGN KEY (accountNo) REFERENCES account (accountNo))'''
#           )
print("Table created successfully")
con.commit()
con.close()
