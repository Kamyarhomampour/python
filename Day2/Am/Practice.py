# # ! STUDENT TASKS ! 
# """

# Python - Day 2 (AM) - Tasks:

# 1: Create your own examples of the following For Loops to familiarize yourself with the syntax:

# - For Loop (List): Write a for loop that prints each item in a list
# - For Loop (String): Write a for loop that prints each character in a string
# - For Loop with Range: Write a for loop that prints numbers 1 to 10 using the range function""

classes = ["math","english","coding","Physics"]
for i in classes:
    print(i)
string =  "practice" 
for i in string:
    print(i)
for i in range(10):
    print(i+1)

# 2: Create your own examples of the following While Loops to familiarize yourself with the syntax and the 'break' and 'continue' keywords:

# - Basic While Loop: Write a while loop that prints numbers from 1 to 10.
# - While Loop with Break: Implement a 'break' statement in a while loop that prints numbers from 1 to 10 and stops when it reaches 5.
# - While Loop with Continue: Research the 'continue' statement and implement it in a while loop that prints numbers from 1 to 10, but skips printing the number 5.

# https://www.programiz.com/python-programming/break-continue

num=1
while num<11:
    print(num)
    num+=1
# num=1
# while num<=20: 
#     print(num)
#     if num==7:
#     print("No problem, I will stop.")
#     num+=1
#     break
num = 1

while num <= 10:
    print(num)
    if num == 5:
        print("I will stop")
        break
    num += 1
    
