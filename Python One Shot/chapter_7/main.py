# Question 1 - Write a program to print multiplication table of a given number using for loop.

# num = int(input("Enter Number to Print Table : "))
# for i in range(1,11):
#     print(f"{num} x {i} = {num*i}")

# Question 2 - Write a program to greet all the person names stored in a list ‘l’ and which starts with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Good Morning {name}")


# Question 3 - Attempt problem 1 using while loop.

# num = int(input("Enter Number to Print Table : "))
# i = 1
# while (i<=10):
#     print(f"{num} x {i} = {num*i}")
#     i = i+1

# Question 4 - Write a program to find whether a given number is prime or not.

# def is_prime(n):
#     # Check if n is less than 2 (not prime)
#     if n <= 1:
#         return False
#     # Check if n is 2 or 3 (prime)
#     if n <= 3:
#         return True
#     # Check if n is divisible by 2 or 3 (not prime)
#     if n % 2 == 0 or n % 3 == 0:
#         return False
#     # Check for other factors up to the square root of n
#     i = 5
#     while i * i <= n:
#         if n % i == 0 or n % (i + 2) == 0:
#             return False
#         i += 6
#     return True

# # Test the function
# number = int(input("Enter a number to check if it is prime: "))
# if is_prime(number):
#     print(f"{number} is a prime number.")
# else:
#     print(f"{number} is not a prime number.")


# Question 5 - Write a program to find the sum of first n natural numbers using while loop.

# number = int(input("Enter a number to check if it is prime: "))
# sum = 0
# for i in range(0,number+1):
#     sum = sum+i
# print(f"Sum of first {number} numbers are {sum}")

# 6. Write a program to calculate the factorial of a given number using for loop.

# number = int(input("Enter a number to check if it is prime: "))
# n = number
# fact = 1
# while(n >=1):
#     fact = fact*n
#     n -=1

# print(f"Factorial of {number} is {fact}")


# Question 7 - Write a program to print the following star pattern.
#   *
#  ***
# ***** for n = 3

# n = 3
# for i in range(1, n + 1):
#     # Print leading spaces
#     for j in range(n - i):
#         print(" ", end="")
#     # Print stars
#     for k in range(2 * i - 1):
#         print("*", end="")
#     # Move to the next line
#     print()

# Question 8. Write a program to print the following star pattern:
# *
# **
# *** for n = 3

# n=3
# for i in range(1,n+1):
#     for j in range(0,i):
#         print("*",end="")   #to dont create a new line

#     print("")       # to start a new line

# Question 9. Write a program to print the following star pattern.
# * * *
# *   *   for n = 3
# * * * 

n = 3
for i in range(1,n+1):
    if(i==1 or i ==n):
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print()


# Question 10. Write a program to print multiplication table of n using for loops in reversed order.
