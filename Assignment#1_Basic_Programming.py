                                                                    #Assignment: 1
#Basic Input & Print Questions

#1. WAP to print "Hello Python" on the screen.
print("\nHello Python")

#2. Take a name as input and print Welcome <name> 
name = input("\nPlease enter your name: ")
print(f'Welcome "{name}"')

#3. Take a number as input and print it.
num = int(input("\nEnter a numnber: "))
print("You entered:",num)

#4. Take two numbers as input and print both numbers on separate lines. 
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))

print("Your first number is:",num1)
print("Your second number is:",num2)

#5. Take a name and age as input and print: 
name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

print(f"My name is '{name}' and my age is {age} years")


#Integer (int) Based Questions

#6. Take an integer as input and print its square. 
num = int(input("\nEnter a number: "))
square = num * num
print(f"The square of {num} is {square}")

#7. Take two integers as input and print their sum. 
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} = {sum}")

#8. Take two integers and print: 
#o Addition 
#o Subtraction 
#o Multiplication 
num1 = int(input("\nEnter first number: "))
num2 = int(input("Enter second number: "))
#Addition
sum = num1 + num2
#Subtraction
diff = num1 - num2
#Multiplication 
prod = num1 * num2

print(f"The sum of {num1} and {num2} = {sum}")
print(f"The difference of {num1} and {num2} = {diff}")
print(f"The product of {num1} and {num2} = {prod}")

#9. Take a number and print: 
#The number entered is <number> 
num = int(input("\nEnter a number: "))
print("The number you entered is:",num)

#10. Take an integer and print its double.
num = int(input("\nEnter a number: "))
double = num * 2
print(f"The double of {num} is {double}")


#Float (float) Based Questions

#11. Take a float value as input and print it. 
num = float(input('\nEnter a float value: '))
print("You entered:",num)

#12. Take two float numbers and print their sum. 
num1 = float(input("\nEnter first float number: "))
num2 = float(input("Enter second float number: "))
print(f"Sum of {num1} and {num2} is {num1 + num2}")

#13. Take a float number and print its half value. 
num = float(input("\nEnter a floating point value: "))
print(f"Half of {num} =",1/2 * num)

#14. Take length and width (float) as input and print the area of a rectangle.  (length*width) 
length = float(input("\nEnter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
print(f"Area of the rectangle = {area}sq.units")

#15. Take radius as float input and print the area of a circle 
#(Use π = 3.14) 
radius = float(input("\nEnter the radius: "))
pi = 3.14
area = 3.14 * (radius ** 2)
print(f"Area of the circle = {area}sq.units")


#Mixed int & float Questions

#16. Take one integer and one float as input and print both. 
num1 = int(input("\nEnter an integer: "))
num2 = float(input("Enter a float: "))
print(f"Your integer number is {num1} and your floating point number is {num2}")

#17. Take total marks (int) and number of subjects (int) and print the average as float. 
total = int(input("\nEnter total marks: "))
no_of_subs = int(input("Enter number of subjects: "))
avg = total/no_of_subs
print("The average marks =",avg)

#18. Take price (float) and quantity (int) and print the total cost. 
price = float(input("\nEnter the price: "))
quantity = int(input("Enter the quantity:"))
tot_cost = price * quantity
print("Total cost =",tot_cost)

#19. Take two numbers (one int, one float) and print their sum. 
num1 = int(input("\nEnter first integer: "))
num2 = float(input("Enter second float: "))
print(f"The sum of {num1} and {num2} = {num1 + num2}")

#20. Take salary (float) and bonus (int) and print the final salary.
sal = float(input("\nEnter your salary: "))
bonus = int(input("Enter the bonus: "))
print(f"Final salary = {sal + bonus}")



