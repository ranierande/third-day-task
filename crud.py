import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="Rani@8377",database="Fruit_Shop")
mycursor = mydb.cursor()
print("Do you want to perform whcih operations: 1=create, 2=read, 3=update, 4=delete")
choice=int(input('choose your option='))
if choice == 1:
    
    mycursor.execute("create table fruits2(fruit_name VARCHAR(255), fruit_price INT)")
    try:
        mycursor.execute("insert into fruits2 values('mango',80),('apple',89),('cherry',90),('grapes',50)")  
        mydb.commit() 
        print('Record inserted successfully...')   
    except:
        mydb.rollback() 
    mydb.close()  
      
elif choice == 2:
    try:
        mycursor.execute("select * from fruits2")  
        result=mycursor.fetchall()   
        for i in result:
            fruit_name=i[0]  
            fruit_price=i[1]  
            print(fruit_name,fruit_price)  
    except:
        print('Error:Unable to fetch data.')  
    mydb.close()
    for row in mycursor:
        print('row = %r' % (row,))

elif choice == 3:
    try:
        mycursor.execute("update fruits2 SET fruit_price=110 WHERE fruit_name='apple'")
        mydb.commit() 
        print('Record updated successfully...')   
    except:   
      mydb.rollback()  
    mydb.close()
elif choice == 4:
    try:
        mycursor.execute("delete FROM fruits2 WHERE fruit_name='apple'") 
        mydb.commit()   
        print('Record deteted successfully...')  
    except:
        mydb.rollback
    mydb.close()
else:
    print("you are not select right options please try again")
    
 
    

