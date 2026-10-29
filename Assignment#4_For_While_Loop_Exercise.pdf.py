                                                                    #Assignment#4

#For_While_Loop_Exercise.pdf


#FOR Loop – Programming Questions

    
#1. Write a program to print numbers from 1 to 100.

print("\n1. The numbers from 1 to 100 are:\n")
for i in range(1,101):
    print(i," ",end = '')
    if i % 20 == 0:
        print()

        
#2. Write a program to print all even numbers between 1 and 50.
        
print("\n2. All even numbers between 1 and 50 are:\n")
for i in range(2,51,2):
    print(i,"",end = '')
    if i % 10 == 0:
        print()

        
#3. Write a program to print the sum of first n natural numbers.
        
print("\n3. Sum of first n natural numbers:\n")
n = int(input("Enter n: "))
if n > 0:
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(f"The sum of first {n} natural numbers = {sum}")
else:
    print("The number should be greater than 0")


#4. Write a program to print the multiplication table of a given number.
    
print("\n4. Multiplication table of a given number:\n")
num = int(input("Enter a number: "))

for i in range(1,11):
    print(f"{num} * {i} = {num*i}")


#8. Write a program to print all prime numbers between 1 and 100.
    
print("\n8. Prime numbers between 1 and 100 are:\n")
for num in range(1, 101):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    if count == 2:
        print(num,"",end = '')
    if num % 10 == 0:
        print()


#9. Write a program to calculate the factorial of a number using for loop.
    
print("\n9. Factorial of a number using For Loop:\n")
num = int(input("Enter a non negative integer: "))

if not(num < 0):
    
    fact = 1

    for i in range (1, num + 1):
        fact = fact * i

    print(f"The factorial of {num} is {fact}")
    
else:
    
    print("The number cannot be negative")


#WHILE Loop – Programming Questions
print("\n\n#WHILE Loop – Programming Questions:\n")

    
#11. Write a program to print numbers from 1 to 50 using while loop.
    
print("\n11. Numbers from 1 to 50 using While Loop:\n")

num = 1
while num <= 50:
    print(num," ",end = '')
    if num % 10 == 0:
        print()
    num += 1


#12. Write a program to print all odd numbers between 1 and 50.
    
print("\n12. Odd Numbers from 1 to 50 using While Loop:\n")

num = 1
while num <= 50:
    if num % 2 == 1:
        print(num," ",end = '')
    if num % 10 == 0:
        print()
    num += 1
    
       
#13. Write a program to calculate the sum of digits of a number.

print("\n13. Program to calculate the sum of digits of a number using while loop:\n")

ori_num = num = int(input("Enter an integer: "))

if ori_num < 0:
    num = -num 

sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10

print(f"Sum of all the digits of |{ori_num}| = {sum}")


#14. Write a program to reverse a number using a while loop.

print("\n14. Program to reverse a number using while loop:\n")

ori_num = num = int(input("Enter an integer: "))

sign = 1

if ori_num < 0:
    sign = -1
    num = -num 

rev_num = 0
while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //= 10
    
rev_num = rev_num * sign

print(f"Reverse of {ori_num} = {rev_num}")


#15. Write a program to find the factorial of a number using a while loop.
print("\n15. Factorial of a number using While Loop:\n")

num = int(input("Enter a non-negative integer: "))

if num < 0:
    print("Invalid input")
else:
    i = 1
    fact = 1
    while i <= num:
        fact = fact * i
        i += 1
        
    print(f"Factorial of {num} = {fact}")


#16. Write a program to keep taking input from the user until the user enters 0.
print("\n16. Keep taking input from the user until the user enters 0 - While Loop:\n")

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break


#17. Write a program to find the largest digit in a number.

print("\n17. Largest digit in a number:\n")

ori_num = num = int(input("Enter a number: "))

large_digit = 0

if num < 0:
    num = -num

while num > 0:
    digit = num % 10
    if digit > large_digit:
        large_digit = digit
    num //= 10

print(f"Largest digit in {ori_num} = {large_digit}")


#18. Write a program to check whether a number is a palindrome.

print("\n18. Check whether a number is  palindrome:\n")

ori_num = num = int(input("Enter an integer: "))

if ori_num < 0:
    print(f"{ori_num} is NOT a palindrome")
elif 0 <= ori_num <= 9:
    print(f"{ori_num} is a palindrome")
else:
    rev_num = 0
    while num > 0:
        digit = num % 10
        rev_num = rev_num * 10 + digit
        num //= 10
        
    if ori_num == rev_num:
        print(f"{ori_num} is a palindrome")
    else:
        print(f"{ori_num} is a NOT a palindrome")


#19. Write a program to print the Fibonacci series up to n terms.

print("\n19. Print the Fibonacci series up to n terms:\n")

n_terms = int(input("Enter number of terms (> 0): "))

if n_terms <= 0:
    print("Invalid input")
else:
    pre_prev = 0
    prev = 1
    print(f"{pre_prev} {prev} ",end = '')
    
    count = 3
    while count <= n_terms:
        cur_term = pre_prev + prev
        print(f"{cur_term} ",end = '')
        count += 1
        
        pre_prev = prev
        prev = cur_term
        
    print()
        
#20. Write a program to implement a number guessing game using a while loop.
        
print("\n20. Implemention of a number guessing game:")

game_num =47
end = "enter"
while end != "exit":
       
    user_num = int(input("\nEnter any number between 0 and 100: "))
                   
    if not(0 <= user_num <= 100):
        print("Invalid input")
        continue
    if user_num == game_num:
        print("\nCongratulations Winner. You guessed right!")
        break
    elif game_num - 1 <= user_num <= game_num + 1:
        print("\nClosest")
    elif game_num - 5 <= user_num <= game_num + 5:
        print("\nCloser")
    elif game_num - 15 <= user_num <= game_num + 15:
        print("\nClose")
    elif game_num - 20 <= user_num <= game_num + 20:
        print("\nSlightly close")
    else:
        print("\nFar away")
    end = input('\nType "exit" for exiting the game; Press "enter" to continue: ')

