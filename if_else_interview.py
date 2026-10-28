
#F. INTERVIEW-LEVEL PYTHON LOGIC QUESTIONS

#51. Write a Python program to calculate income tax using slabs.

print("\n51. Base Income Tax using slabs:\n")

std_ded = 75000
limit = slab_inc = 400000
rate = 5
rebate = 60000
slab1_tax = slab2_tax = slab3_tax = slab4_tax = slab5_tax = slab6_tax = slab7_tax = 0
taxfree_inc = 1200000
Base_Tax = 0

GTI = float(input("Enter Gross Total Income(GTI): Rs."))

if GTI < 0:
    print("Invalid input. GTI cannot be negative")
    
else:
    
    tax_inc = GTI - std_ded

    if tax_inc > taxfree_inc:
        
        tax_inc -= limit

        #Slab2
        if tax_inc > 0:
            
            if tax_inc < limit:
                slab_inc = tax_inc
                 
            slab2_tax = rate/100 * slab_inc
           
            #Prepare for next slab
            rate = rate + 5
            tax_inc -= limit

        #Slab3
            if tax_inc > 0:
                
                if tax_inc < limit:
                    slab_inc = tax_inc
                    
               
                slab3_tax = rate/100 * slab_inc
                
                #Prepare for next slab
                rate = rate + 5
                tax_inc -= limit
                
        #Slab4
                if tax_inc > 0:
                           
                    if tax_inc < limit:
                        slab_inc = tax_inc
                        
                   
                    slab4_tax = rate/100 * slab_inc
                   
                    #Prepare for next slab
                    rate = rate + 5
                    tax_inc -= limit
                            
        #Slab5
                    if tax_inc > 0:
                                   
                        if tax_inc < limit:
                            slab_inc = tax_inc
                            
                        slab5_tax = rate/100 * slab_inc
                       
                        #Prepare for next slab
                        rate = rate + 5
                        tax_inc -= limit

        #Slab6
                    if tax_inc > 0:
                               
                        if tax_inc < limit:
                            slab_inc = tax_inc
                            
                        slab6_tax = rate/100 * slab_inc
                       
                        #Prepare for next slab
                        rate = rate + 5
                        tax_inc -= limit

        #Slab7
                        if tax_inc > 0:
                                       
                            #Only for last slot
                            slab_inc = tax_inc
                              
                            slab7_tax = rate/100 * slab_inc
                         
        #Calculating Base Tax:
                            
        Slab_Total_Tax = slab1_tax + slab2_tax + slab3_tax + slab4_tax + slab5_tax + slab6_tax + slab7_tax
        
        #Marginal Relief
        if (GTI - std_ded) < 1280000:
             
            excess = (GTI - std_ded) - 1200000
            
            if excess < Slab_Total_Tax:
                Base_Tax = excess
            else:
                Base_Tax = Slab_Total_Tax
        else:
            Base_Tax = Slab_Total_Tax 
    
    print(f"Base Tax as per New Tax Regime for GTI Rs.{GTI} = Rs.{Base_Tax}")

    
#52. Create an ATM withdrawal program with balance checks.

print("\n52. ATM withdrawal program with balance checks:\n")

balance = 15000.0
print(f"Your current balance = Rs.{balance}")
amount = float(input("Enter amount for withdrawal: Rs."))

if amount <= 0:
    print("Amount should be greater than 0")
elif amount > balance:
    print("Insufficient Balance")
else:
    balance -= amount
    print("Withdrawal Successful\nYour balance is: Rs.",balance)
    

#53. Check promotion eligibility using experience and performance
    
print("\n53. Promotion eligibility using experience and performance:\n")

exp = int(input("Enter your years of experience: "))

if exp < 0:
    print("Invalid input. Experience cannot be negative")
    
else:
     
    if exp >= 3:
        rating = input("Enter your performance rating - Excellent, Good or Poor: ")
        if rating == "Excellent" or rating == "excellent":
            print("You are eligible for promotion")
        else:
            print("Not eligible for promotion. Your performance should be Excellent")
    else:
        print("Insufficient Experience. Not eligible for promotion.")


#54. Implement a grading system using nested if–else.
    
print("\n54. Grading system using nested if–else:\n")

per = int(input("Enter your percentage - 0 to 100: "))
if 0 <= per <= 100:
    if per >= 90:
        print("Grade A")
    else:
        if per >= 75:
            print("Grade B")
        else:
            if per >= 50:
                print("Grade C")
            else:
                print("Fail")
else:
    print("Invalid input")


#55. Validate strong password using multiple conditions.
    
print("\n55. Validating strong Password using multiple conditions:\n")

password = input("Enter password: ")

upper_case = False
lower_case = False
digits = False

for char in password:
    if 'A' <= char <= 'Z':
         upper_case = True
    if 'a' <= char <= 'z':
        lower_case = True
    if '0' <= char <= '9':
        digits = True

if len(password) >= 8 and  upper_case == True and lower_case == True and digits == True:
    print("Strong password:")
else:
    print("Password NOT strong enough:")


#56. Calculate delivery charges based on location and order amount.
    
print("\n56. Delivery charges based on location and order amount:\n")

location = input("Enter your location - Local/Other: ")
order_amount = int(input("Enter your order amount: Rs."))

if order_amount <= 0:
    print("Invalid input. Order amount should be positive")
    
else:
    if location == "local" or location == "Local":
        if order_amount >= 400:
            del_charge = 0
        else:
            del_charge = 40
    else:
        
        if order_amount >= 1000:
            del_charge = 0
        else:
            del_charge = 80
            
    print("The delivery charges are: Rs.",del_charge)


#57. Determine online exam qualification.

print("\n57. Online Exam Qualification:\n")

atten_per = int(input("Enter your attendance percentage (0 to 100): "))

if 0 <= atten_per <= 100:
    fees_paid = input("Are all the fees paid? - y or n: ")

    if atten_per >= 75 and (fees_paid == 'y' or fees_paid == 'Y'):
        print("Qualified for online Exam")
    else:
        print("NOT Qualified for online Exam")
else:
    print("Invalid input")

     
#58. Create movie ticket pricing logic based on age & show time.
    
print("\n58. Movie ticket pricing:\n")

age = int(input("Please enter your age: "))
show_time = int(input("Enter show time(0 - 23): "))

if 0 < age < 106 and 0 <= show_time <= 23:

    if age <= 12:
        price = 150
    else:
        if show_time < 17:
            price = 200
        else:
            price = 300
            
    print(f"Movie ticket costs Rs.{price}")
else:
    print("Invalid input")


#59. Determine bank account type based on balance.

print("\n59. Bank Account Type:\n")
balance = float(input("Enter yuor savings account balance: Rs."))

if balance < 0:
    print("Invalid Balance. Balance cannot be negative")
elif balance >= 100000:
    print("Premium Account")
elif balance >= 10000:
    print("Regular Account")
else:
    print("Basic Account")


#60. Create a menu-driven program using if–elif–else.
    
print("\n60. Menu-driven program using if–elif–else:\n")
print("1. Check Balance")
print("2. Deposit money")
print("3. Withdraw money")

choice = int(input("\nEnter your choice: "))

if not(choice == 1 or choice == 2 or choice == 3):
    print("Invalid input")
else:

    balance =20500.0

    if choice == 1:
          print("\nThe balance in your account is: Rs.",balance)
    elif choice == 2:
        amount = float(input("\nEnter the amount to be deposited: Rs."))
        if amount <= 0:
             print("The amount should be greater than 0")
        else:
            balance += amount
            print("The balance in your account is: Rs.",balance)
    elif choice == 3:
        amount = float(input("\nEnter the amount to be withdrawn: Rs."))
        if amount <= 0:
             print("The amount should be greater than 0")
        elif amount > balance:
            print("Insufficient Balance")
        else:
            balance -= amount
            print("Withdraw successful.\nThe balance in your account is: Rs.",balance)
    else:
        print("Invalid Input")
    



