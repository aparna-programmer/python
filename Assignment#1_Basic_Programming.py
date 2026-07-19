
#1. WAP to print "Hello Python" on the screen.

print("Hello Python")

#2
name = input("Please enter your name: ")
print("Welcome ",name)

#3
num = int(input("Enter a numnber: "))
print("You entered : ",num)

#4
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Your first number is: ",num1)
print("Your second number is: ",num2)

#5
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"My name is {name} and my age is {age}")

#6
num = int(input("Enter a number: "))
square = num * num
print(f"The square of {num} is {square}")

#7
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
sum = num1 + num2
print(f"The sum of {num1} and {num2} = {sum}")

#8
num1 = int(input("Enter first number: "))
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

#9
num = int(input("Enter a number: "))
print("The number you entered is :",num)

#10
num = int(input("Enter a number: "))
double = num *2
print(f"The double of {num} is {double}")


#11
num = float(input('Enter a float value: '))
print("You entered: ",num)

#12
num1 = float(input("Enter first float number: "))
num2 = float(input("Enter second float number: "))
print(f"Sum of {num1} and {num2} is {num1 + num2}")

#13
num = float(input("Enter a floating point value: "))
print(f"Half of {num} = ",1/2 * num)

#14
length = float(input("Enter the length of the rectangle: "))
breadth = float(input("Enter the breadth of the rectangle: "))
area = length * breadth
print(f"Area of the rectangle = {area}sq.units")

#15
radius = float(input("Enter the radius: "))
pi = 3.14
area = 3.14 * (radius ** 2)
print(f"Area of the circle = {area}sq.units")

#16
num1 = int(input("Enter an integer: "))
num2 = float(input("Enter a float: "))
print(f"Your integer number is {num1} and your floating point number is {num2}")

#17
total = int(input("Enter total marks: "))
no_of_subs = int(input("Enter number of subjects: "))
avg = total/no_of_subs
print("The average marks = ",avg)

#18
price = float(input("Enter the price: "))
quantity = int(input("Enter the quantity:"))
tot_cost = price * quantity
print("Total cost = ",tot_cost)

#19
num1 = int(input("Enter first integer: "))
num2 = float(input("Enter second float: "))
print(f"The sum of {num1} and {num2} = {num1 + num2}")

#20
sal = float(input("Enter your salary: "))
bonus = int(input("Enter the bonus: "))
print(f"Final salary = {sal + bonus}")


