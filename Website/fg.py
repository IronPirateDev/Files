import mysql.connector as mc
mycon=mc.connect(host='localhost',user='root',password=dp
sbn,database='shop')
if mycon.is_connected==False:
print('error')
else:
while True:
print('''
1) Add a record
2) Display All Records
3) Display records of a particular manufacturer.
4) Modify the Price of a given P_ID entered by user.
5) Delete a Record of given ProductName
6) Exit.''')
choice=int(input('Enter your choice:'))
mycur = mycon.cursor()
if choice==1:
q=input('Enter IP_ID(2 letter, 2 number code):')
r=input('Enter PRODUCT_NAME:')
s=input('Enter MANUFACTURER:')
t=int(input('Enter PRICE:'))
q1="insert into product values('{}', '{}', '{}',
{})".format(q,r,s,t)
mycur.execute(q1)
mycon.commit()
if choice==2:
mycur.execute('select * from product')
data=mycur.fetchall()
for i in data:
print(i)
if choice==3:
x=input('Enter Manufacturer Name:')
qq=("select * from product where
Manufacturer='{}'").format(x)
mycur.execute(qq)
records = mycur.fetchall()
for record in records:
print(record)
if choice==4:
d=(input('Chose P_ID:'))
e=int(input('Enter New Price:'))
q11="update product SET Price = {} where P_ID=
'{}'".format(e,d)
mycur.execute(q11)
mycon.commit()
if choice==5:
g=input('Enter Product_Name:')
q12="delete from student where
Product_Name='{}'".format(g)
mycur.execute(q12)
mycon.commit()
if choice==6:
print("The Code is Over")
mycon.close()
break