# Python Day 2 - AM - Lists and Loops

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Lists
# * Ordered, Indexed, Mutable, Allow Duplicates

languages = ["HTML", "CSS", "JavaScript", "Python"]

print(languages)

# ! Remember our index begins at 0
print(languages[1])

# ! Negative Indexing
# * The idea of counting backwards from the end of the list

# * Passing -1 as your index will always return the last item of the list
print(languages[-1])

# * With negative indexing we can access any item we just count backwards from -1
print(languages[-4])

# ! Updating / Changing the List Items
# * We can ammend items in a list by referencing the items index

languages[3] = "SQL"
print(languages)

# ! List Methods#
# RESOURCE: https://www.programiz.com/python-programming/methods/list
# * Built-in functionality that allows us to manipulate our list data in various ways

# ! Remove an Item
# * 'remove()' - Recieves an argument containing the value of item you wish to remove

languages.remove("SQL")
print(languages)

# * If we try to remove an item that does not exist we get an error
# languages.remove("SQL")

# ! Add / Append an Item
# * 'append()' - Add the value passed as an argument to the end of the list

languages.append("SQL")
print(languages)

# ! Number of items in a list
# * 'len()' - pass an argument to it and it will return the length of the data passed

print(len(languages))

# ! Loops - For Loop - List
# * Loop over our 'languages' list and print each item

for i in languages:
    print(i)

# * 'i' in this example is just a reference and can be replaced with anything

for lang in languages:
    print(lang)

# ! For Loop - String

string = "Example"
for i in string:
    print(i)

# * Remember 'i' is just self defined reference
for letters in string:
    print(letters)

# ! For Loop - Range
# * 'range()' - Allows us to define how many iterations we would like

for i in range(5):
    print(i)

# * The count starts from 0 and will run however many times we define in our range
# * To include 1 rather that 0 we can add 1 to our counter 'i'

for i in range(10):
    print(i+1)

# ! While Loop
# * Will run until a condition is met meaning we need to mindful of avoiding infinite loops

# * Basic Example:

num = 1
while num <= 5:
    print(num)
    num += 1

# ! While Loop with 'break'
# * A 'break' statement when encountered ends our loop whether the condition is true or not
# * Our example will ask a user for input and will only stop asking when the user enters "stop"

while True:
    user_input = input("I will keep asking for input until you tell me to \"STOP\": ")

    if user_input.lower() == "stop":
        print(user_input)
        print("No problem, I will stop.")
        break

# ! STUDENT TASKS ! 
"""

Python - Day 2 (AM) - Tasks:

1: Create your own examples of the following For Loops to familiarize yourself with the syntax:

- For Loop (List): Write a for loop that prints each item in a list
- For Loop (String): Write a for loop that prints each character in a string
- For Loop with Range: Write a for loop that prints numbers 1 to 10 using the range function

2: Create your own examples of the following While Loops to familiarize yourself with the syntax and the 'break' and 'continue' keywords:

- Basic While Loop: Write a while loop that prints numbers from 1 to 10.
- While Loop with Break: Implement a 'break' statement in a while loop that prints numbers from 1 to 10 and stops when it reaches 5.
- While Loop with Continue: Research the 'continue' statement and implement it in a while loop that prints numbers from 1 to 10, but skips printing the number 5.

https://www.programiz.com/python-programming/break-continue

3: Research list methods and experiment with them, putting together some example implementations:

https://www.programiz.com/python-programming/methods/list


Stretch Task: 

Guess the Number: Store a number between 1 and 10 in a variable. Write a while loop that asks the user to input a guess, the game should continue until the user inputs a correct guess.

"""















# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")