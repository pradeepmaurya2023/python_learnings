# Question 1. Write a program using functions to find greatest of three numbers.

# def greatest_num(a,b,c):
#     if(a > b and a>c):
#         return a
#     elif(b > a and b>c):
#         return b
#     else:
#         return c
    
# print(greatest_num(3,4,9))


# Question 2. Write a python program using function to convert Celsius to Fahrenheit.

# def celcius_to_fahrenheit(n):
#     fahren = (n*(9/5)) + 32
#     return fahren

# print(f"5°C is Equals to {celcius_to_fahrenheit(5)}°F")

# Question 3. How do you prevent a python print() function to print a new line at the end.
# print("Hello No new line at the end",end="")



# Question 4. Write a recursive function to calculate the sum of first n natural numbers.

# def sum_of_natural(n):
#     if(n == 1):
#         return 1
#     else:
#         return n+sum_of_natural(n-1)

# print(sum_of_natural(5))

# Question 5. Write a python function to print first n lines of the following pattern:
#  ***
#  ** - for n = 3
#  *

# def pattern(n):
#     if(n == 0):
#         return 
#     else:
#         print("*"*n)
#         return pattern(n-1)

# pattern(10)


# Question 6. Write a python function which converts inches to cms.

# def in_to_cem(n):
#     cem = n*2.54
#     return cem

# print(f"1 inches is Equals to {in_to_cem(1)}cm")

# Question 7. Write a python function to remove a given word from a list and strip it at the same time.

# lst = ["Rohan", "Shubham","Harry","an"]

# def rem(l,word):
#     n = []

#     for item in l:
#         if not(item == word):
#             if word in item:
#                 item = item.strip(word)
#             n.append(item)
        
#     return n

# print(rem(lst, "an"))
# Question 8. Write a python function to print multiplication table of a given number.

def multiplication_table(n):
    for i in range(1,11):
        print(f"{n} x {i} = {n*i}")

multiplication_table(10)

