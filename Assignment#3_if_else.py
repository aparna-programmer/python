
                                                                               #Assignment: 3

#A. Python IF (Single Condition)


#1. Write a Python program to check if a number is positive.

print("\n1. Check if a number is positive:\n")
num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive")

    
#2. Print "Eligible to vote" if age is 18 or above.

print("\n2. Check Eligibility to vote:\n")
age = int(input("Enter your age: "))
if 0 < age <=105:
    if age >= 18:
        print("You are eligible to vote")


#3. Check if a number is divisible by 7.
    
print("\n3. Check Divisibility by 7:\n")    
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is divisible by 7")

    
#4. Print "Pass" if marks are greater than 40.
    
print("\n4. Pass if marks are greater than 40:\n")
marks = int(input("Enter the marks: "))
if marks > 40:
    print(f"You have passed with {marks} marks")


#5. Check if a number is greater than 100.
    
print("\n5. Check if a number is greater than 100:\n")
num = int(input("Enter a number: "))
if num > 100:
    print(f"{num} is greater than 100")


#6. Display a message if temperature exceeds 45°C.
    
print("\n6. Check if temp exceeds 45 degrees:\n")
temp = int(input("Enter the temperature "))
if temp > 45:
    print("Its too hot today")


#7. Check if a string length is more than 8 characters. 
print("\n7. Check if string length is more than 8 characters:\n")
str = input("Enter a string: ")
if len(str) > 8:
    print(f'The string "{str}" has more than 8 characters')


#8. Print "Logged In" if password matches "admin123".
    
print("\n8. Check password match:\n")
str = input("Enter a string: ")
if str == "admin123":
    print("Logged in")


#9. Check if a number is a multiple of 10.  
print("\n9. Check if a number is a multiple of 10:\n")
num = int(input("Enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10")


#10. Print a warning if balance is below minimum limit.
    
print("\n10. Check if balance is below minimum limit:\n")
min_limit = 1000
balance = int(input("Enter the balance: Rs."))
if balance < min_limit:
    print("Balance is less than minimum limit!")

    
#B. Python IF-Else (Two Conditions)


#11. Check whether a number is even or odd.  

print("\n11. Check if a number is even or odd:\n")

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")


#12. Find the largest of two numbers. 
print("\n12. Largest of two numbers:\n")
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
    if num2 > num1:
        print(f"{num2} is greater than {num1}")
    else:
        print(f"{num2} is same as {num1}")

#13. Check whether a person is eligible for driving license.
   
print("\n13. Check if a person is eligible for driving license:\n")
age = int(input("Enter your age: "))
if not(0 < age <= 105):
     print("Invalid input")
else:
    if age >= 18:
        print("Congratulations! You can apply for driving license")
    else:
        print(f"Not eligible to apply now. You can apply after {18 - age} years")


#14. Print "Pass" or "Fail" based on marks. 

print("\n14. Check if Pass or Fail:\n")

marks = int(input("Enter the marks - 0 to 100: "))

if not(0 <= marks <= 100):
     print("Invalid input")
else:
    if marks >= 35:
        print("Congratulations! You have passed")
    else:
        print("Sorry, you have failed")


#15. Check whether a number is positive or negative
    
print("\n15. Check if a number is positive or negative:\n")
num = int(input("Enter a number: "))
if num == 0:
    print(f"{num} is neither positive nor negative")
else:
    if num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")


#16. Check whether a character is an vowel or consonant.
    
print("\n16. Check whether a character is an vowel or consonant:\n")

char = input("Enter an English character: ")

if len(char) != 1 or char not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print("Please enter 1 English character")
else:
    if char in {'a','e','i','o','u','A','E','I','O','U'}:
        print(f"'{char}' is an vowel")
    else:
        print(f"'{char}' is a consonant")


#17. Check if a year is leap or not. 

print("\n17. Check if a year is leap or not:\n")

year = int(input("Enter a year (1 or later): "))

if year < 1:
    print("Invalid input")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

#18. Print "Valid Password" or "Invalid Password".
    
print("\n18. Print 'Valid Password' and 'Invalid Password':\n")
password = input("Enter the password: ")
if password == "admin123":
    print("Valid Password")
else:
    print("Invalid Password")


#19. Determine whether salary is taxable or not.
    
print("\n19. Check if salary is taxable or not:\n")
salary = float(input("Enter your salary: Rs."))

if salary < 0:
    print("Invalid input. Salary cannot be negative")
else:
    if salary <= 1275000:
        print(f"Rs.{salary} is not taxable")
    else:
        print(f"Rs.{salary} is taxable")


#20. Check whether a number is greater than 50 or not.
    
print("\n20. Check if a number is greater than 50 or not:\n")
num = int(input("Enter a number: "))
if num > 50:
    print(f"{num} is greater than 50")
else:
    if num < 50:
        print(f"{num} is less than 50")
    else:
       print(f"{num} = 50")


#C. Python NESTED IF-ELSE

#21. Find the largest of three numbers
    
print("\n21. Largest of three numbers:\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print(f"{num1} is the largest")
else:
    if num2 >= num1 and num2 >= num3:
        print(f"{num2} is the largest")
    else:
        print(f"{num3} is the largest")


#22.Check if a number is positive, negative or zero
        
print("\n22. Check if a number is positive, negative or zero:\n")

num = int(input("Enter a number: "))

if num == 0:
    print(f"{num} is zero")
else:
    if num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")


#23. Assign grades:
#● A → marks ≥ 90 
#● B → marks ≥ 75 
#● C → marks ≥ 60 
#● Fail → below 60

print("\n23. Assigning grades:\n A → marks ≥ 90, B → marks ≥ 75, C → marks ≥ 60, Fail → below 60 :\n")

marks = int(input("Enter the marks - 0 to 100: "))

if not(0 <= marks <= 100):
    print("Invalid input. ")
else:
    if marks >= 90:
        print(f"Grade A for {marks} marks")
    else:
        if marks >= 75:
           print(f"Grade B for {marks} marks")
        else:
            if marks >= 60:
                print(f"Grade C for {marks} marks")
            else:
                print(f"Failed with {marks} marks")


#24.  Check whether a triangle is equilateral, isosceles, or scalene. 

print("\n24. Check if a triangle is equilateral, isosceles or scalene:\n")

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

if not(side1 > 0 and side2 > 0 and side3 > 0):
    print("Invalid input. ")
else:
    if side1 == side2 == side3:
        print("It is an EQUILATERAL TRIANGLE")
    else:
        if side1 == side2 or side2 == side3 or side1 == side3:
            print("It is an ISOSCELES TRIANGLE")
        else:
            print("It is a SCALENE TRIANGLE")


#25. Check whether a character is uppercase, lowercase, digit, or special character.
        
print("\n25. Check if a character is uppercase, lowercase, digit or special character:\n")

char = input("Enter a character: ")

if len(char) != 1:
    print("Invalid input. Character length must be 1")
else:
    if char.isupper():
        print(f"'{char}' is an uppercase character")
    else:
        if char.islower():
            print(f"'{char}' is a lowercase character")
        else:
            if char.isdigit():
                 print(f"'{char}' is a digit")
            else:
                 print(f"'{char}' is a special character")


#26. Calculate electricity bill using slab-wise rates
             
print("\n26. Electricity bill using slab-wise rates:\n")

units = int(input("Enter the electricity units consumed: "))

if units < 0:
    print("Invalid input. Units cannot be negative")
else:
    bill = 0

    if units <= 100:
        bill = units * 1.5
    else:
        if units <= 200:
            bill = 100 * 1.5 + (units - 100) * 2.5
        else:
            if units <= 300:
                bill = 100 * 1.5 + 100 * 2.5 + (units - 200) * 4
            else:
                bill = 100 * 1.5 + 100 * 2.5 + 100 *4 + (units - 300) * 6
                
    print(f"Bill = {bill} Rupees")


#27. Validate login using username and password

print("\n27. Validating login using username and password:\n")

username = input("Enter Username: ")
password = input("Enter Password: ")

if username == 'aparna' and password == 'admin123':
    print("Valid Username and Password")
else:
    if username != 'aparna' and password == 'admin123':
        print("Invalid Username")
    else:
        if username == 'aparna' and password != 'admin123':
            print("Invalid Password")
        else:
            print("Invalid Username and Password")


#28. Check student result using marks of 3 subjects
            
print("\n28. Student result using marks of 3 subjects:\n")

sub1 = float(input("Enter subject1 marks: "))
sub2 = float(input("Enter subject2 marks: "))
sub3 = float(input("Enter subject3 marks: "))

print()

if sub1 >= 40:
    if sub2 >= 40:
        if sub3 >= 40:
             total = sub1 + sub2 +sub3
             per = total/3
             print(f"Pass with {per}%")
        else:
             print ("Failed in subject3")
    else:
        if sub3 >= 40:
                print("Failed in subject2")
        else:
                print ("Failed in subject2 and subject3")
else:
    if sub2 >=40:
        if sub3 >= 40:
            print("Failed in subject1")
        else:
            print("Failed in subject1 and subject3")
    else:
        if sub3 >= 40:
            print ("Failed in subject1 and subject2")
        else:
            print ("Failed in subject1 and subject2 and subject3")

            
#29. Find the second largest number among three numbers
                
print("\n29. Second largest number among three numbers:\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
       print("All three are equal. There is no second largest")
else:
    if num1 < num3 and (num1>=num2 or  num2 == num3) or (num1>=num3 and  num1<num2):
        second_largest=num1
    else:
        if  (num2>=num3 and num2<num1) or  ((num2 > num1 or num1==num3) and num2<num3):
            second_largest=num2
        else:
            second_largest=num3
    print("The second largest number is :",second_largest)
                
       
#29. Find the second largest number among three numbers
            
print("\n29. Second largest number among three numbers:\n")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
    print("All three are equal. There is no second largest")

else:
    if num1 >= num2 and num1 >= num3:
       max = num1
    else:
        if num2 >= num1 and num2 >= num3:
            max = num2
        else:
            max = num3
    
    if num1 <= num2 and num1 <= num3:
       min = num1
    else:
        if num2 <= num1 and num2 <= num3:
            min = num2
        else:
            min = num3
    
    if num1 == num2 and max == num1 or num1 == num3 and max == num1 or num2 == num3 and max == num2:
        second_largest = min
    else:
              
        sum = num1 + num2 + num3
        second_largest = sum - max -min
        
    print("The second largest number is :",second_largest)
    

#30. Check loan eligibility using age, salary, and credit score
    
print("\n30. Loan eligibility using age, salary, and credit score:\n")

Min_age = 21
Max_age = 65
Min_sal = 15000
Min_cre_score = 750

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: Rs."))
cre_score = float(input("Enter your credit score: "))

if not(0 < age < 106 and 0 <= salary < 500000000 and 0 <= cre_score <= 1000):
    print("Invalid input")
else:
    if not (Min_age <= age <= Max_age):
        print(f"Not eligible for loan. Age must be between {Min_age} and {Max_age}")
    elif salary < Min_sal:
        print(f"Not eligible for loan. Salary must be greater tham {Min_sal}")
    elif cre_score < Min_cre_score:
        print(f"Not eligible for loan. Credit score must be greater than {Min_cre_score}")
    else: 
        print("Congratulations! You are eligible for loan")


#C. Python ELIF (Multiple Conditions)


#31. Print day name using day number(1-7)
    
print("\n31. Displaying Day name using Day number:\n")

day = int(input("Enter day number(1-7): "))

if not (1 <= day <= 7):
    print("Incorrect day number. Enter only between 1 and 7: ")
elif day == 1:
    print("It is Monday")
elif day == 2:
    print("It is Tuesday")
elif day == 3:
    print("It is Wednesday")
elif day == 4:
    print("It is Thursday")
elif day == 5:
    print("It is Friday")
elif day == 6:
    print("It is Saturday")
else:
    print("It is Sunday")


#32. Print month name using month number
    
print("\n32. Displaying Month name using Month number:\n")

month = int(input("Enter month number(1-12): "))

if not (1 <= month <= 12):
    print("Incorrect month number. Enter only between 1 and 12: ")
elif month == 1:
    print("It is January")
elif month == 2:
    print("It is February")
elif month == 3:
    print("It is March")
elif month == 4:
    print("It is April")
elif month == 5:
    print("It is May")
elif month == 6:
    print("It is June")
elif month == 7:
    print("It is July")
elif month == 8:
    print("It is August")
elif month == 9:
    print("It is September")
elif month == 10:
    print("It is October")
elif month == 11:
    print("It is November")
else:
    print("It is December")


#33. Display grade based on percentage
    
print("\n33. Displaying grade based on percentage:\n")

per = float(input("Enter percentage: "))
if per >= 90:
    print("A Grade")
elif per >= 75:
    print("B Grade")
elif per >= 60:
    print("C Grade")
elif per >= 45:
    print("D Grade")
elif per >= 35:
    print("Pass")
else:
    print("Fail")



#34. Display bonus percentage based on experience years

print("\n34. Displaying bonus percentage based on experience years:\n")

years = float(input("Enter experience years : "))
if not(0 <=years <= 60):
    print("Invalid input.")
else:
    salary = float(input("Enter your salary: Rs."))

    if salary < 0:
        print("Invalid input. Salary cannot be negative")
    else:
        if years > 5:
            bonus = 0.05 * salary
        elif 3 <= years <= 5:
            bonus = 0.02 *salary
        else:
            bonus = 0

        total_sal = bonus + salary
        print("Bonus = Rs.",bonus)
        print("Total salary = Rs.",total_sal)


#35. Identify traffic signal meaning

print("\n35. Identify traffic signal meaning:\n")

colour = input("Enter the traffic signal colour (Red, Yellow or Green): ")
colour = colour.lower()

if colour == 'green':
    print("\nGO! The signal is green")
elif colour == 'yellow':
    print("\nREADY! Prepare to stop. The signal is yellow")
elif colour == 'red':
    print("\nSTOP! The signal is red")
else:
    print("\nWrong signal entered")


#36.Categorize temperature as Cold/Warm/Hot
    
print("\n36. Categorize temperature as Cold/Warm/Hot:\n")

temp =int(input("Enter the temperature: "))

if temp < 18:
    print("It is COLD!")
elif 18 <= temp >= 32:
    print("It is WARM")
else :
    print("It is HOT!")


#37.Categorize employee based on salary range
    
print("\n37. Categorize employee based on salary range:\n")

salary = float(input("Enter your salary: Rs."))

if salary < 0:
        print("Invalid input. Salary cannot be negative")
else:
    if salary < 20000:
        print("Low income")
    elif 20000 <= salary <= 50000:
        print("Middle income")
    elif 50000 < salary <= 100000:
        print("High income")
    else:
        print("Very high income")


#38. Print discount percentage based on purchase amount
    
print("\n38. Discount percentage based on purchase amount:\n")

purchase_amount = float(input("Enter your purchase amount: Rs."))

if purchase_amount < 0:
    print("Invalid input. Purchase amount cannot be negative")
else:

    if purchase_amount > 10000:
        discount = 20
    elif 5000 <= purchase_amount <= 10000:
        discount = 15
    elif 2000 <= purchase_amount < 5000:
        discount = 10
    else:
        discount = 5
        
    final_amount = purchase_amount - discount * purchase_amount / 100

    print(f"Discount for Rs.{purchase_amount} is {discount}%")
    print(f"Final amount = Rs.{final_amount}")


#39. Ientify number type: single-digit/ double-digit/ multi-digit

print("\n39. Ientify number type: single-digit/ double-digit/ multi-digit:\n")

num = int(input("Enter a number: "))

if -10 < num < 10:
    print(f"{num} is single digit")
elif -99 <= num <= -10 or 10 <= num <= 99:
    print(f"{num} is double digit")
else:
    print(f"{num} is multi-digit")


#40. Assign performance rating: poor/Average /Good/ Excellent
    
print("\n40. Performance rating: poor/Average /Good/ Excellent:\n")

score = int(input("Enter your Score (0 - 100): "))

if score < 0 or score > 100:
    print("Invalid score. Enter a value between 0 and 100")
else:
    if score < 50:
        rating = 'Poor'
    elif score < 75:
        rating = 'Average'
    elif score < 85:
        rating = 'Good'
    else:
        rating = 'Excellent'

    print(f"Performance rating for the {score} is {rating}")


#E. Python COMPLEX CONDITIONS (AND/OR/NOT)


#41. Check whether a number is divisible by 5 and 11

print("\n41. Divisibility by 5 and 11:\n")

num = int(input("Enter a number: "))

if num % 5 == 0 and num % 11 == 0:
    print(f"{num} is divisible by both 5 and 11")
else:
    print(f"{num} is NOT divisible by 5 and 11")


#42. Check if a person is eligible for loan:
     # age>=21
     # salary >= 25000
     # credit score >= 700
     
print("\n42. Eligibility for loan:\n")

age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
cred_score = int(input("Enter your credit score: "))

if not(0 < age < 106 and 0 <= salary < 500000000 and 0 <= cred_score <= 1000):
        print("Invalid input")
else:
        if age >= 21 and salary >= 25000 and cred_score >= 700:
            print("Congratulations! You are eligible for loan")
        else:
            print("Sorry. Not eligible for loan")


#43. Validate login using username AND password.
            
print("\n43. Validating login using username AND password:\n")

correct_username = "admin"
correct_password = 123456

u_username = input("Enter username: ")
u_password = int(input("Enter password(int): "))

if u_username == correct_username and u_password == correct_password:
        print("Login Successful")
else:
        print("Incorrect Username or Password!")


#44. Check student pass condition: 
#● All subjects ≥ 40 
#● Average ≥ 50

print("\n44. Student pass condition:\n")

sub1 = int(input('Enter subject 1 marks: '))
sub2 = int(input('Enter subject 2 marks: '))
sub3 = int(input('Enter subject 3 marks: '))

if not(0 <= sub1 <= 100 and 0 <= sub2 <= 100 and 0 <= sub3 <= 100):
        print("Invalid marks. Marks should be between 0 and 100")
else:
    avg = (sub1 + sub2 + sub3)/3

    if sub1 >= 40 and sub2 >= 40 and sub3 >= 40 and avg >= 50:
            print("Congratulations! Student passed\nAverage =",avg)
    else:
            print("Student Failed")

#45. Check if a number lies between 10 and 100.
            
print("\n45. Check if a number lies between 10 and 100:\n")

num = float(input("Enter any number: "))

if 10 < num < 100:
        print(f"{num} lies between 10 and 100")
else:
         print(f"{num} does NOT lie between 10 and 100")


#46. Check exam eligibility: 
#● attendance ≥ 75% OR 
#● medical certificate available
         
print("\n46. Eligibility for Exam:\n")

attend_per = int(input("Enter your attendance percentage: "))

if not(0 <= attend_per <= 100):
    print("Invalid input")
else:
    med_cer = 'n'

    if attend_per < 75:
            med_cer = input("Do you have a medical certificate? Type 'y' for 'Yes' or 'n' for 'No': ")
            
    if attend_per >= 75 or med_cer == 'y':
            print("You are ELIGIBLE to take exam")
    else:
            print("You are NOT ELIGIBLE to take exam")


#47. Validate a date using conditions.
        
print("\n47. Validation of date:\n")

year = int(input("Enter a year between 1 and 9999: "))
month = int(input("Enter the month: "))
day = int(input("Enter the day: "))

if not(1 <= year <= 9999 and 1 <= month <= 12 and 1 <= day <= 31):
     print("Invalid input")
else:

    valid = False

    if 0 < year <= 9999 and 1 <= month <= 12:
            if month == 4 or month == 6 or month == 9 or month == 11:
                    valid = 1 <= day <= 30
            elif month == 2:
                    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                            valid = 1 <= day <= 29
                    else:
                            valid = 1 <= day <= 28
            else:
                    valid = 1 <= day <= 31

    if valid:
            print(f"{day}/{month}/{year} is a valid date")
    else:
            print(f"{day}/{month}/{year} is an invalid date")
           

#48. Check whether an email format is valid.

print("\n48. Email Format Validation:\n")

email = input("Enter an email id: ")

if '@' in email and '.' in email:
        if ' ' in email:
                print(f'The Email "{email}" is Invalid. Spaces are not allowed')
        else:
                print(f'The Email "{email}" is Valid')
else:
        print(f"""The Email "{email}" is Invalid. Either '@' or '.' is missing""")


#49. Determine insurance eligibility using age, health status, and income.

print("\n49. Eligibility for Insurance:\n")

age = int(input("Enter your age: "))
health_score = int(input("Enter your health score between 1 and 100: "))
salary = float(input("Enter your salary: Rs."))

if not(0 < age <= 105 and 0 < health_score <= 100 and salary >= 0):
        print("Invalid input. ")
else:
    if age >= 18 and health_score >= 60 and salary >=25000:
            print("Congratulations! You are eligible for health insurance")
    else:
            print("Sorry! You are NOT eligible for health insurance")


#50. Check leap year using complete leap year logic.
        
print("\n50. Leap year:\n")

year = int(input("Enter a year between 1 and 9999: "))

if 1 <= year <= 9999:
        if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
                print(f"{year} is a Leap Year")
        else:
                print(f"{year} is NOT a Leap Year")

else:
        print("Invalid input. Year should be between 1 and 9999")



