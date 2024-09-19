name="Hari"
password="990"
user_name=input("Enter your name:")
passwords=input("Enter your password:")
s='''
     1.credit
     2.debit
     3.money statement
     4.exit
'''
Amount=100000
if name==user_name and password==passwords:
    print(s)
    while True:
        option=int(input("Enter the option:"))
    
        if option==1:
            credit_amount=float(input("Enter the amount:"))
            print("Amount after credit:",Amount+credit_amount)
        elif option==2:
            debit_amount=float(input("Enter the amount:"))
            print("Amount after debit:",Amount-debit_amount)
        elif option==3:
        
            print("Amount:",Amount)  
        elif option==4:
            break              
else:
    print("incorrect")        

