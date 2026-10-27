'''#A. Python IF (Single Condition)
#1. If a number is positive

num = int(input("Enter a number: "))
if num > 0:
    print(f"{num} is positive")
    
#2. Eligible to vote

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote")

#3. Divisible by 7
    
num = int(input("Enter a number: "))
if num % 7 == 0:
    print(f"{num} is divisible by 7")
    
#4. Pass if marks are greater than 40

marks = int(input("Enter the marks: "))
if marks > 40:
    print(f"You have passed with {marks} marks")

#5. If a number is greater than 100

num = int(input("Enter a number: "))
if num > 100:
    print(f"{num} is greater than 100")

#6. If temp exceeds 45 degrees

temp = int(input("Enter the temperature "))
if temp > 45:
    print("Its too hot today")

#7. If string length is more than 8 characters

str = input("Enter a string: ")
if len(str) > 8:
    print(f"The string {str} has more than 8 characters")

#8. Check password match

str = input("Enter a string: ")
if str == "admin123":
    print("Logged in")

#9. If a number is a multiple of 10

num = int(input("Enter a number: "))
if num % 10 == 0:
    print(f"{num} is a multiple of 10")

#10. If balance is below minimum limit

min_limit = 1000
balance = int(input("Enter the balance: "))
if balance < min_limit:
    print("Balance is less than minimum limit!")
    
#B. Python IF-Else (Two Conditions)
    
#11. If a number is even or odd

num = int(input("Enter a number: "))
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

#12. Find largest of two numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 > num2:
    print(f"{num1} is greater than {num2}")
else:
   print(f"{num2} is greater than {num1}")

#13. If a person is eligible for driving license

age = int(input("Enter your age: "))
if age >= 18:
    print("Congratulations! You can apply for driving license")
else:
    print(f"Not eligible to apply now. You can apply after {18 - age} years")

#14. Pass or Fail

marks = int(input("Enter the marks: "))
if marks >= 35:
    print("Congratulations! You have passed")
else:
    print("Sorry, you have failed")

#15. If a number is positive or negative

num = int(input("Enter a number: "))
if num == 0:
    print(f"{num} is neither positive nor negative")
if num > 0:
    print(f"{num} is positive")
else:
    print(f"{num} is negative")

#16. Check whether a chasracter is a vowel or consonant
    
char = input("Enter a character: ")
if char in {'a','e','i','o','u','A','E','I','O','U'}:
    print(f"{char} is an vowel")
else:
    print(f"{char} is a consonant")

#17. If an year is leap or not

year = int(input("Enter an year: "))
if year % 4 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#18. Print "Valid Password" and "Invalid Password"

password = input("Enter the password ")
if password == "admin123":
    print("Valid Password")
else:
    print("Invalid Password")

#19. If salary is taxable or not

salary = float(input("Enter your salary: "))
if salary <= 1275000:
    print(f"{salary} is not taxable")
else:
    print(f"{salary} is taxable")

#20. If a number is greater than 50 or not

num = int(input("Enter a number: "))
if num > 50:
    print(f"{num} is greater than 50")
else:
    print(f"{num} is not greater than 50")

#C. Python NESTED IF-ELSE

#21. Find the largest of three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
if num1 > num2 and num1 > num3:
    print(f"{num1} is greater than {num2} and {num3}")
else:
    if num2 > num1 and num2 > num3:
        print(f"{num2} is greater than {num1} and {num3}")
    else:
        print(f"{num3} is greater than {num1} and {num2}")

#22.Check if a number is positive, negative or zero

num = int(input("Enter a number: "))
if num == 0:
    print(f"{num} is zero")
else:
    if num > 0:
        print(f"{num} is positive")
    else:
        print(f"{num} is negative")

#23. Assign grades:

marks = int(input("Enter the marks: "))
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

#24. A triangle is equilateral, isosceles or scalene

side1 = int(input("Enter the first side: "))
side2 = int(input("Enter the second side: "))
side3 = int(input("Enter the third side: "))

if side1 == side2 == side3:
    print("It is an EQUILATERAL TRIANGLE")
else:
    if side1 == side2 or side2 == side3 or side1 == side3:
        print("It is an ISOSCELES TRIANGLE")
    else:
        print("It is a SCALENE TRIANGLE")

#25.A character is uppercase, lowercase, digit or special character

char = input("Enter a character: ")
if char.isupper():
    print(f"{char} is an uppercase character")
else:
    if char.islower():
        print(f"{char} is a lowercase character")
    else:
        if char.isdigit():
             print(f"{char} is a digit")
    
        else:
             print(f"{char} is a special character")


#26. Calculate electricity bill using slab-wise rates

units = int(input("Enter the electricity units consumed: "))
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

username = input("Enter Username: ")
password = input("Enter Password:")

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

sub1 = float(input("Enter subject1 marks:"))
sub2 = float(input("Enter subject2 marks:"))
sub3 = float(input("Enter subject3 marks:"))

if sub1 >= 40:
    if sub2 >= 40:
        if sub3 >= 40:
            total = sub1 + sub2 +sub3
            per = total/3
            print(f"Pass with {per}%")
        else:
            print("Failed in subject3")
    else:
        print("Failed in subject2")
else:
    print("Failed in subject1")

if sub1 >= 40 and sub2 >= 40 and sub3 >= 40:
     total = sub1 + sub2 +sub3
     per = total/3
     print(f"Pass with {per}%")

else:
    if sub1 >=40:
        if sub2 >= 40:
            print ("Failed in subject3")
        else:
            if sub3 >= 40:
                print("Failed in subject2")
            else:
                print ("Failed in subject2 and subject3")
    else:
        if sub2 >=40 and sub3 >=40:
            print("Failed in subject1")
        else:
            if sub2 < 40 and sub3 >= 40:
                print ("Failed in subject1 and subject2")
            else:
               if sub2 >=40 and sub3 < 40:
                   print("Failed in subject1 and subject 3")
               else:
                    print ("Failed in subject1 and subject2 and subject3")

                    

#29. Find the second largest number among three numbers

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num1 == num2 == num3:
    print("All three are equal. There is no second largest")
else:
    if (num1 < num2 and num1 >= num3) or (num1 < num3 and num1 >= num2) or (num2 == num3 and num1 < num2):
        print(f"{num1} is the second largest number")
    else:
        if (num2 < num1 and num2 >= num3) or (num2 < num3 and num2 >= num1) or (num1 == num3 and num2 < num1):
            print(f"{num2} is the second largest number")
        else:
            print(f"{num3} is the second largest number")
       
#29. Find the second largest number among three numbers

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
    print("max=",max)
    if num1 <= num2 and num1 <= num3:
       min = num1
    else:
        if num2 <= num1 and num2 <= num3:
            min = num2
        else:
            min = num3
    print("min=",min)
    if num1 == num2 and max == num1 or num1 == num3 and max == num1 or num2 == num3 and max == num2:
        second_largest = min
    else:
              
        sum = num1 + num2 + num3
        second_largest = sum - max -min
    print("The second largest number is : ",second_largest)

#30. Check loan eligibility using age, salary, and credit score

Min_age = 21
Max_age = 65
Min_sal = 15000
Min_cre_score = 750
Loan_approved = 1
age = int(input("Enter your age: "))
salary = float(input("Enter your salary: "))
cre_score = float(input("Enter your credit score: "))

if not (Min_age <= age <= Max_age):
    Loan_approved = 0
    print(f"Age must be between {Min_age} and {Max_age}")
if salary < Min_sal:
    Loan_approved = 0
    print(f"Salary must be greater tham {Min_sal}")
if cre_score < Min_cre_score:
    Loan_approved = 0
    print(f"Credit score must be greater than {Min_cre_score}")
if Loan_approved:
    print("Congratulations! You are eligible for loan")

'''
#C. Python ELIF (Multiple Conditions)

#31. Print day name using day number(1-7)

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
elif day == 7:
    print("It is Sunday")

#32. Print month name using month number

month = int(input("Enter month number(1-12): "))
if not (1 <= day <= 12):
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
elif month == 12:
    print("It is December")

#33. Display grade based on percentage

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

years = float(input("Enter experience years: "))
salary=float(input("Enter your salary: "))

if years > 5:
    bonus = 0.05 * salary
elif 3 <= years <= 5:
    bonus = 0.02 *salary
else:
    bonus = 0

total_sal = bonus + salary
print("Bonus = ",bonus)
print("Total salary = ",total_sal)

#35. Identify traffic signal meaning

colour =input("Enter the traffic signal colour (Red, Yellow or Green): ")
lower(colour)
if colour == 'green':
    print("GO! The signal is green")
elif colour == 'yellow':
    print("READY! Prepare to stop. The signal is yellow")
elif colour == 'red':
    print("STOP! The signal is red")
else:
    print("Wrong signal entered")

 #36.Categorize temperature as Cold/Warm/Hot

temp =int(input("Enter the temperature: "))

if temp < 18:
    print("It is COLD!")
elif 18 <= temp >= 32:
    print("It is WARM")
else :
    print("It is HOT!")

 #37.Categorize employee based on salary range

    salary = float(input("Enter your salary: "))

    if salary < 20000:
        print("Low income")
    elif 20000 <= salary <= 50000:
        print("Middle income")
    elif 50000 < salary <= 100000:
        print("High income")
    else:
        print("Very high income")

     #38.Print discount percentage based on purchase amount

    purchase_amount = float(input("Enter your purchase amount: "))

    if purchase_amount > 10000:
        discount = 20
    elif 5000 <= purchase_amount <= 10000:
        discount = 15
    elif 2000 <= purchase_amount < 5000:
        discount = 10
    else:
        discount = 5
    final_amount = purchase_amount - discount * purchase_amount / 100
    print(f"Discount for {purchase_amount} is {discount}%")
    print("Final amount = ",final_amount)

    #39.Ientify number type: single-digit/ double-digit/ multi-digit

    num = int(input("Enter a number: "))
    if -10 < num < 10:
        print(f"{num} is single digit")
    elif -99 <= num <= -10 or 10 <= num <= 99:
        print(f"{num} is double digit")
    else:
        print(f"{num} is multi-digit")

    #40. Assign performance rating: poor/Average /Good/ Excellent

    score = int(input("Enter the score between 0 to 100: "))
    if score < 0 or score > 100:
        print("Invalid score. Enter a value between 0 and 100")
    elif score < 50:
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

    num = int(input("Enter a number: "))
    if num % 5 == 0 and num % 11 == 0:
        print(f"{num} is divisible by both 5 and 11")

    #42. Check if a person is eligible for loan:
        # age>=21
        # salary >= 25000
        # credit score >= 700
    num = int(input("Enter a number: "))
    if num % 5 == 0 and num % 11 == 0:
        print(f"{num} is divisible by both 5 and 11")


    

