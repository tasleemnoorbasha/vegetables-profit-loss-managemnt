import mysql.connector as db
con=db.connect(user='root',password='Tasleem@123',\
               host='localhost',database='tasleem')
cur=con.cursor()
total_sells=0
total_cost=0
print("ice cream shop open")
while True:
    print('\n new customer')
    customerbill=0
    while True:
        
        items=input("enter icecream name:")
        
        cur.execute("select*from items where name=%s"),(items,))
        result=cur.fetchone()
        if result:
            cid,cname,cquantity,sellingprice,costprice=result

            qty=int(input("how many cups you want:"))
            if qty<=quantity:
                amount=qty*sellingprice
                cost=qty*costprice
                new_qty=quantity-qty


                cur.execute(
                    '''update items set quantity=%s where cid=%s''',
                        (new_qty,cid))
                    
                
                db.commit()

                     
                customer_bill+=amount
                total_sales+=amount
                total_cost+=cost
                    
                print("Added:", amount, "rupees")

            else:
                print("Out of stock")

        else:
            print("Item not available")

        more = input("More items? (yes/no): ")
        if more == "no":
            break

    print("Customer Bill:", customer_bill)

    next_customer = input("Next customer? (yes/no): ")
    if next_customer == "no":
        break

print("\n---- SHOP CLOSED ----")

# Show remaining stock (shopkeeper view)
print("\nRemaining Stock:")
cursor.execute("SELECT name, quantity FROM items")
for row in cursor.fetchall():
    print(row[0], "-", row[1], "cups")

# Owner view
profit = total_sales - total_cost

print("\n---- OWNER VIEW ----")
print("Total Sales:", total_sales)
print("Total Cost:", total_cost)

if profit > 0:
    print("Profit:", profit)
else:
    print("Loss:", profit)

db.close()
                    












cur.close()

con.close()
