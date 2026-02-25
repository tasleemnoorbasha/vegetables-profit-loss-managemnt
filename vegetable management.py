#Project name VEGETABLE SHOP MANAGEMENT the project about the profit and loss
#To develop a project we need a specific criteria that is
                        #planning,analysis,design,develop





veg=["gabage","calyflower","capsicum"]
quantity=[10,5,15]
price=[35,40,60]

while True:
    item=input("what do you want :")
    if item in veg:
        qty=float(input("how many kgs you want :"))
        idx=veg.index(item)
        if qty<=quantity[idx]:
            amount=qty*price[idx]
            quantity[idx]=quantity[idx]-qty
            print("please pay",amount,"rupees")
        else:
            print("out of stock")
    else:
        print(item,"is not available")
    ch=input("do you  want to close the shop(yes/no):")
    if ch=="yes":
                
     print("closing the shop")
     break
        
                 
                 
                
                
                 
                 





            
