#project for fruitshop with list tuples and dictionaries
#define variable
options="yes"
fruit={}
fruit_name=[]
fruit_cost=[]
print("*****FRUIT SHOP SYSTEM*****")
print('')
print('')
print("welcome to fruit shop!!!")
print('')
#bill creation after user buy a fruits

def bill():
    generate_bill="yes"
    while generate_bill in("yes","y","Y","Y","Yes"):
        print("")
        selectItem=input("do you want to create a bill for all items?")
        print("")
        if selectItem in("yes","y","Y","Y","Yes"):
            i=0
            sumtotal=0
            for i in range(len(fruit_name)):
                Item=fruit_name[i]
                Rate=fruit_cost[i]
                print("Item:",Item)
                Qty=int(input("Enter Quantity in kg:"))
                if Qty<=5:
                 Amount=(Rate*Qty)
                 print('')
                 print("Item",'\t\t',"Rate",'\t\t',"Quantity",'\t\t',"Amount")
                 print(Item,'\t\t',Rate,'\t\t',Qty,'\t\t',Amount)
                 print("Total Amount:",Amount,"Rs.")
                 print("")
                 sumtotal=Amount+sumtotal
                 i=i+1
                 print("\t\t\t","----------")
                 print("\t\t\t","Tatal price of all Items:",sumtotal,"Rs.")
                 print("")
                 break
                else:
                 Amount=(Rate*Qty)
                 print('')
                 print("Item",'\t\t',"Rate",'\t\t',"Quantity",'\t\t',"Amount")
                 print(Item,'\t\t',Rate,'\t\t',Qty,'\t\t',Amount)
                 print("Total Amount:",Amount,"Rs.")
                 print("**congrates you got a discount of 5%**")
                 disc=Amount*0.05
                 print("discount",disc,"Rs")
                 print("total amount is :",Amount-disc,"Rs")
                 sumtotal=(Amount-disc)+sumtotal
                 i=i+1
                 print("\t\t\t","----------")
                 print("\t\t\t","Tatal price of all Items:",sumtotal,"Rs.")
                 print("")
                 break
        elif selectItem in("no","n","N","No"):
             Item=input("Enter item for bill:")
             Rate=fruit.get(Item,'No data found')
             Qty=int(input("Enter Quantity :"))
             print("")
             if Qty<=5:
                 Amount=(Rate*Qty)
                 print('')
                 print("Item",'\t\t',"Rate",'\t\t',"Quantity",'\t\t',"Amount")
                 print(Item,'\t\t',Rate,'\t\t',Qty,'\t\t',Amount)
                 print("Total Amount:",Amount,"Rs.")
                 print("")
                 break
             else:
                 Amount=(Rate*Qty)
                 print('')
                 print("Item",'\t\t',"Rate",'\t\t',"Quantity",'\t\t',"Amount")
                 print(Item,'\t\t',Rate,'\t\t',Qty,'\t\t',Amount)
                 print("Total Amount:",Amount,"Rs.")
                 print("congrates you got a discount of 5%")
                 disc=Amount*0.05
                 print("discount",disc,"Rs")
                 print("your total amount is :",Amount-disc,"Rs")
                 break
        else:
             print("sorry your answer is not valid,please create bill by more options")
             if  Bill_again==input("yes","y","Y","Y","Yes"):
                 generate_bill="yes"
             elif Bill_again in ("no","n","N","No"):
                 break
             else:
                 print("sorry, Your answer is not valid but we drop you at bill creation page")
#Item adding options
while options in ("yes","y","Y","Yes"):
     print("select options:")
     print("1.show Item")
     print("2.Add Item")
     print("3.Exit")
     choice=input("choose a valid option:")
     print("")
     if choice=="1":
         if len(fruit.keys()) == 0:
             print("Nothing to show choose valid option")
             print('')
             continue
             options='yes'
         else:
            print("")
            print("Item",'\t\t\t',"rate")
            print("----------------------------")
            i=0
            for i in range(len(fruit_name)):
                 Item=fruit_name[i]
                 Rate=fruit_cost[i]
                 print("Item",'\t\t\t',"rate")
                 print("")
                 generate_bill=input("do you want to generate bill")
                 print("")
                 if generate_bill in ("yes","y","Y","Yes"):
                     bill()
                 elif generate_bill in ("no","n","N","No"):
                      options="yes"
                 else:
                      print("sorry your answer is not valid")
     elif choice=="2":
         
         Item=input("enter item name(max 14 character:)")
         Rate=int(input("Enter Rate per kg:"))
         fruit[Item]=Rate
         fruit_name.append(Item)
         fruit_cost.append(Rate)
         print("Item added")
         print("")
         generate_bill=input("do you want to generate bill")
         print("")
         if generate_bill in ("yes","y","Y","Yes"):
                bill()
         elif generate_bill in ("no","n","N","No"):
                options="yes"
         else:
                print("sorry your answer is not valid")
     elif choice=="3":
      print("thank you for using this application")
      break
     else:
      print("choose a valid options=Yes")
 
 
    
            
        
             
                
             
             
             
             
                
                
                
    
