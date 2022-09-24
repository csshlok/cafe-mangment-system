from tkinter import Image
import mysql.connector
mydb = mysql.connector.connect(host='localhost', user='root', password='Ggn@0124', database='project')
import datetime
import csv
from PIL import image

###CODE START###
########MENU#########
val = [
(1, 'Banana Pancake', 'Pancakes', 200),
(2, 'Oatmeal Pancake with Cinnamon Apples', 'Pancakes', 250), (3, 'Blueberry Lemon Ricotta Pancake', 'Pancakes', 300),
(4, 'Original Classic Pancake', 'Pancakes', 200),
(5, 'Chocolate Chip Pancake', 'Pancakes', 250),
(6, 'Cinnamon Roll Pancake', 'Pancakes', 200),
(7, 'Strawberry Buttermilk Pancake', 'Pancakes', 275),
(8, 'Oreo Pancake', 'Pancakes', 250),
(9, 'Red Velvet Pancake','Pancakes',300),
(10,'Key Lime Pancake','Pancakes',300),
(11,'Cookies & Cream Waffle','Waffles',350), (12,'Cinnamon Roll Waffle','Waffles',350),
(13,'Rocky Road Waffle','Waffles',350),
(14,'Black Forest Cherry Waffle','Waffles',350), (15,'Vanilla Berry Waffle','Waffles',300),
(16,'Oreo Waffle','Waffles',350),
(17,'Strawberry Waffle','Waffles',300),
(18,'Chocolate Chip Waffle','Waffles',300), (19,'Blueberry Waffle','Waffles',300),
(20,'Original Classic Waffle','Waffles',275),
(21,'Green Bean Sandwich','Sandwiches',200), (22,'Pickle Veggi Sandwich','Sandwiches',200),
(23,'Loaded Scrambled Egg Sandwich','Sandwiches',220),
(24,'Smoked Tofu Sandwich','Sandwiches',250),
(25,'Grilled Cheese Sandwich','Sandwiches',175),
(26,'Lettuce & Corn Sandwich','Sandwiches',150),
(27,'Grilled Paneer Sandwich','Sandwiches',175),
(28,'Plant Based Italian Sandwich','Sandwiches',250),
(29,'GrilledBroccoliandMozerellaCheeseSandwich','Sandwiches',250),
(30,'Classic Indian Style Sandwich','Sandwiches',200),
(31,'Banana Milkshake','Milkshakes & Coolant Drinks',150),
(32,'Strawberry Milkshake','Milkshakes & Coolant Drinks',150),
(33,'Oreo Milkshake','Milkshakes & Coolant Drinks',150),
(34,'Vanilla Mint Milkshake','Milkshakes & Coolant Drinks',150),
(35,'Rasberry Milshake','Milkshakes & Coolant Drinks',150),
(36,'Lime Soda','Milkshakes & Coolant Drinks',100),
(37,'Cranberry Spritzer','Milkshakes & Coolant Drinks',175),
(38,'Rasberry Fizz','Milkshakes & Coolant Drinks',200),
(39,'Sparkling Water','Milkshakes & Coolant Drinks',100),
(40,'Italian Sweet Soda','Milkshakes & Coolant Drinks',150),
(41,'Choco Chip Cookie','Bakery',30),
(42,'Raisin Cookie','Bakery',30),
(43,'Glazed Doughnut','Bakery',50),
(44,'Cinnamon Doughnut','Bakery',50),
(45,'Custard Filled Doughnut', 'Bakery',60),
(46,'Classic Original Croissant','Bakery',70),
(47,'Melted Chocolate Croissant','Bakery',75),
(48,'Jam Filled Croissant','Bakery',75),
(49,'Cottage Cheese Puff Pastry','Bakery',70),
(50,'Caramelised Green Apple Puff Pastry','Bakery',80), (51,'French Fries','Sides',50),
(52,'Hash Brown','Sides',50),
(53,'Potato Puff','Sides',50),
(54,'Glazed Strawberry','Sides',50), (55,'Classic Side Salad','Sides',75), (56,'Coleslaw','Sides', 75), 
(57,'Garlic Bread','Sides',50), (58,'Chargrilled Veggies','Sides',75), 
(59,'Cheese Sticks','Sides',50), (60,'Hummus Bagel','Sides',100) ]



################### FUNCTIONS/ MAIN CODE STARTS HERE #############

#member verification
#status: untested
def memberverify():
    global memid
    memid = int(input("Enter Member ID"))
    print("You entered ", memid)
    try:
        cursor = mydb.cursor()
        sql = '''select * from membershipdetails where membershipid=''' + str(memid)+";"
        cursor.execute(sql)
        r=cursor.fetchone()
        print("Your details are:" , r)
        global cust_name
        global cust_no
        cust_name = r[1]
        cust_no = r[3]
        global memberconfirm
        memberconfirm = 1
    except Exception as e:
        print(e)
 
#register a member
#status: untested
def registerprocess():
    try:
        mycursor = mydb.cursor()
        f1=input("membershipid")
        f2=input("name")
        f3=input("dob in yyyy-mm-dd format")
        f4=input("phone number")
        sql = '''INSERT INTO membershipdetails VALUES (%s, %s, %s, %s)'''
        l = (f1,f2,f3,f4)
        mycursor.execute(sql,l)
        mydb.commit()
    except Exception as e:
        print(e)

#adding a dish
#status: untested
 
def adddish():
    print("Adding a Dish")
    im = Image.open(r"#status: will add soon")
    im.show()
    try:
        mycursor = mydb.cursor()
        v1=input("Enter DishID")
        v2=input("Enter Qty")
        sql = '''INSERT INTO billtest VALUES (%s, %s)'''
        l = (v1,v2)
        mycursor.execute(sql,l)
        mydb.commit()
        print("Added")
    except Exception as e:
        print(e)

#modify the quantity of a dish
#status: untested
 
def modifyqty():
    print("Modify Quantity")
    try:
        mycursor = mydb.cursor()
        sql = '''select b.dishid, qty, dishname, price from billtest b, menu m where m.dishid=b.dishid;'''
        mycursor.execute(sql)
        print("Here is your current order")
        r=mycursor.fetchall()
        t=0
        print(r)
        while t < len(r):
            print("DishID",r[t][0])
            print("Name",r[t][2])
            print("QTY",r[t][1])
            t=t+1
            mydb.commit()
    except Exception as e:
            print(e)
    modifydishid = int(input("Enter Dish ID"))
    modifyqty = int(input("Enter New Qty"))
    try:
        mycursor = mydb.cursor()
        sql = '''Update billtest set qty=’”+ str(modifyqty) +”’ where dishid='''+ str(modifydishid) +";"
        #to test by print(sql)
        mycursor.execute(sql)
        print("Record Updated")
        mydb.commit()
    except Exception as e:
        print(e)

#delete the billing of a dish
#status: untested
 
def deletedish():
    print("Delete Dish")
    try:
        mycursor = mydb.cursor()
        sql = '''select b.dishid, qty, dishname, price from billtest b, menu m where m.dishid=b.dishid;'''
        mycursor.execute(sql)
        print("Here is your current order")
        r=mycursor.fetchall()
        t=0
        print(r)
        while t < len(r):
            print("DishID",r[t][0])
            print("Name",r[t][2])
            print("QTY",r[t][1])
            t=t+1
            mydb.commit()
    except Exception as e:
        print(e)
    try:
        mycursor = mydb.cursor()
        del1=input("Enter dishid to be deleted")
        sql = '''delete from billtest where dishid=''' + str(del1) + ";"
        mycursor.execute(sql)
        mydb.commit()
        print("Dish Deleted")
    except Exception as e:
        print(e)
 
#printing the bill
#status: untested
 
def printing():
    ############### F I L E N A M E ###################
    print("Processing bill")
    datetime_object = datetime.datetime.now() 
    print(datetime_object)
    filename = str(datetime_object)+".csv" 
    filenametxt = str(datetime_object)+".txt" 
    print(filename)
    ###########GET FINAL BILL + CSV###############
    f=open(filename, mode="a")
    mywriter = csv.writer(f, delimiter = ",")
    try:
        cursor = mydb.cursor()
        sql = '''select * from menu m, billtest b where m.dishid=b.dishid;''' 
        cursor.execute(sql)
        r=cursor.fetchall() 
        print(r)
        global sumy
        sumy = 0
        i=0
        while i < len(r):
            a = r[i][3]*r[i][5]
            print("total of" + r[i][1] + str(a)) 
            sumy = sumy + a
            i=i+1
            dishname = r[i-1][1]
            dishqty = r[i-1][5]
            dishprice = r[i-1][3]
            dishtotal = dishprice*dishqty
            mywriter.writerow([dishname,dishqty,dishprice,dishtotal])
            print("total is" ,sumy) 
            f.close()
########### L O Y A L T Y ###############
if memberconfirm == 1: global pdeduct
pdeduct = 0 global inrdeduct inrdeduct = 0
try:
cursor = mydb.cursor()
sql = “select points from loyaltypoints where membershipid =”+str(memid)+”;”
StockInDesign: The LAB of InDesign Templates

14
cursor.execute(sql)
r=cursor.fetchall()
print(“Available points “, r[0][0], “which evaluate
to INR “, r[0][0]*0.4)
puse = input(“do you want to use your points for
this transaction y/n”)
if puse == “y”:
while pdeduct <= r[0][0]:
points to be deducted”))
pdeduct = int(input(“Enter the no. of
inrdeduct = pdeduct*0.4
print(pdeduct, “points are being deducted”,
inrdeduct, “INR reduced”) try:
mycursor = mydb.cursor()
sql = “update loyaltypoints set points
= points-” +str(pdeduct)+ “ where membershipid=”+str(memid)+”;” #print(sql)
mycursor.execute(sql) print(“Record Updated”) mydb.commit()
except Exception as e: print(e)
break except Exception as e:
print(e)

