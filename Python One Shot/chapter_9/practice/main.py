# Question 1. -  Write a program to read the text from a given file ‘poems.txt’ and find out whether it contains the word ‘twinkle’.

# file1 = open("poems.txt","r")
# data = file1.read()

# if "Twinkle" in data:
#     print("File containes Twinkle Word")
# else:
#     print("File doesnt containe twinkle word")

# file1.close()
# Question 2. -  The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or contains the previous Hi-score. You need to write a program to update the Hi score whenever the game() function breaks the Hi-score.

# import random
# import math

# def game():
#     return random.random()*100

# score = math.floor(game())

# with open("Hi-score.txt","r") as hiscore:
#     previous_score = hiscore.readline()
#     if previous_score != '':
#         previous_score = int(previous_score)
#         print(previous_score)
#     else:
#         previous_score = 0

# if previous_score < score:
#     with open("Hi-score.txt","w") as hiscore:
#             hiscore.write(f"{score}")
#             print("Made changes in Hi-Score.txt")
# else:
#     print("No changes in Hi-Score.txt", score)



# Question 3. -  Write a program to generate multiplication tables from 2 to 20 and write it to the different files. Place these files in a folder for a 13 – year old.

# def generateTable(n):
#     table = ""
#     for i in range(1,11):
#         table += f"{n} x {i} = {n*i}\n"

#     with open(f"tables/table_{n}.pdf","w") as file:
#         file.write(table)


# for i in range(2,21):
#     generateTable(i)


# Question 4. -  A file contains a word “Donkey” multiple times. You need to write a program which replace this word with ##### by updating the same file. 

# word = "Donkey"

# with open("file.txt","r") as f:
#     content = f.read()
#     contentNew = content.replace(word,"#####")

# with open("file.txt","w") as f:
#     f.write(contentNew)


# Question 5. -  Repeat program 4 for a list of such words to be censored.


# words = ["Donkey","bad", "ganda"]

# with open("file.txt","r") as f:
#     content = f.read()

# for word in words:
#     content = content.replace(word,"#"*len(word))

# with open("file.txt","w") as f:
#     f.write(content)

# Question 6. -  Write a program to mine a log file and find out whether it contains ‘python’.


# Question 7. -  Write a program to find out the line number where python is present from ques 6.


# Question 8. -  Write a program to make a copy of a text file “this. txt”


# Question 9. -  Write a program to find out whether a file is identical & matches the content of another file.


# Question 10 - . Write a program to wipe out the content of a file using python.


# Question 11 - . Write a python program to rename a file to “renamed_by_ python.txt.
