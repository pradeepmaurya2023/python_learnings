# Question 1 - Write a program to find the greatest of four numbers entered by the user.
# nums = []
# for i in range(4):
#     num = int(input("Enter a num : "))
#     nums.append(num)
# print(max(nums))

# Question 2 - Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

# nums = []
# for i in range(3):
#     num = int(input("Enter a num : "))
#     nums.append(num)
# average = sum(nums)/3
# if (average >= 40 and nums[0] >=33 and nums[1] >=33 and nums[2] >=33):
#     print("Congrats Bro, You are Passed!!!!!!!!!!!!!")
# else:
#     print("Sorry Bro, Try again next year")

# Question 3 - A spam comment is defined as a text containing following keywords: “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program to detect these spams.

# spam1 = "Make a lot of money" 
# spam2 = "buy now"
# spam3 = "subscribe this"
# spam4 = "click this"

# user_input = input("Enter Your Comment : ")

# if spam1 in user_input or spam2 in user_input or spam3 in user_input or spam4 in user_input:
#     print("It is a spam comment")

# else:
#     print("Thanks for Your Feedback")

# Question 4 - Write a program to find whether a given username contains less than 10 characters or not.

# user_input = input("Enter Your Username : ")

# if(len(user_input)<10):
#     print("Your username has less than 10 characters")

# else:
#     print("Username is available")

# Question 5 - Write a program which finds out whether a given name is present in a list or not.
# names = ["Pradeep","kanchan","Varsha","Tushar","Yug"]
# user_input = input("Enter Your Username : ")

# if user_input in names:
#     print("Your username is present in list")

# else:
#     print("Username is unavailable")


# Question 6 - Write a program to calculate the grade of a student from his marks from the following scheme:
# 90 – 100 => Ex
# 80 – 90 => A
# 70 – 80 => B
# 60 – 70 =>C
# 50 – 60 => D
# <50 => F
# marks = int(input("Enter Your marks : "))
# if marks in range(90,101):
#     print("You got Excellent Grade")
# elif marks in range(80,90):
#     print("You got A Grade")
# elif marks in range(70,80):
#     print("You got B Grade")
# elif marks in range(60,70):
#     print("You got C Grade")
# elif marks in range(50,60):
#     print("You got D Grade")
# elif marks < 50:
#     print("You got F Grade")
    

# Question 7 - Write a program to find out whether a given post is talking about “Harry” or not.
# post = "Harry bhai is awesome!!!"

# if "Harry" in post:
#     print("This post is talking about Harry bhai")
# else:
#     print("This post is not talking about Harry bhai")