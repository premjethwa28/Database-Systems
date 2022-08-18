import pandas as pd
import mysql.connector as mysql


con = mysql.connect(host = "acadmysqldb001p.uta.edu",user = "paj1810",password = "DBmysql@123",database = "paj1810")
cur = con.cursor()
cur.execute("select database()")  #provides database name
record = cur.fetchone()  #retrieves next tuple
print("connected", record)

def  bank():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\BANK.csv',delimiter = ',')  #reads the csv file
    data_dump.head()  #Retrieves n no of rows
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO BANK VALUES(%s,%s,%s)"  #Insert query statement
        cur.execute(sql_query,tuple(row)) 
        print("record inserted")
    cur.close()  
    con.commit()
    con.close    

def bank_branch():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\BANK_BRANCH.csv',delimiter = ',')
    data_dump.head()
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO BANK_BRANCH VALUES(%s,%s,%s)"
        cur.execute(sql_query,tuple(row))
        print("record inserted")
    cur.close()
    con.commit()
    con.close 

def account():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\ACCOUNT.csv',delimiter = ',')
    data_dump.head()
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO ACCOUNT VALUES(%s,%s,%s,%s,%s)"
        cur.execute(sql_query,tuple(row))
        print("record inserted")
    cur.close()
    con.commit()
    con.close 

def customer():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\CUSTOMER.csv',delimiter = ',')
    data_dump.head()
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO CUSTOMER VALUES(%s,%s,%s,%s)"
        cur.execute(sql_query,tuple(row))
        print("record inserted")
    cur.close()
    con.commit()
    con.close 

def loan():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\LOAN.csv',delimiter = ',')
    data_dump.head()
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO LOAN VALUES(%s,%s,%s,%s,%s)"
        cur.execute(sql_query,tuple(row))
        print("record inserted")
    cur.close()
    con.commit()
    con.close 

def accountCustomer():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\ACCOUNT_CUSTOMER.csv',delimiter = ',')
    data_dump.head()
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO ACCOUNT_CUSTOMER VALUES(%s,%s)"
        cur.execute(sql_query,tuple(row))
        print("record inserted")
    cur.close()
    con.commit()
    con.close 

def loanCustomer():
    data_dump = pd.read_csv('C:\Users\premj\OneDrive\Desktop\UTA Courses\DB1 - 5330\Project_1_Bank\LOAN_CUSTOMER.csv',delimiter = ',')
    data_dump.head()
    for i,row in data_dump.iterrows():
        sql_query = "INSERT INTO LOAN_CUSTOMER VALUES(%s,%s)"
        cur.execute(sql_query,tuple(row))
        print("record inserted")
    cur.close()
    con.commit()
    con.close 

bank()
bank_branch()
account()
customer()
loan()
accountCustomer()
loanCustomer()

#References
#https://datatofish.com/import-csv-sql-server-python/