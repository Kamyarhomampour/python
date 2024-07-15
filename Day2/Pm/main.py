# Python Day 2 - PM - Functions and Modules

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Functions
# * Functions are resusable blocks of code that can be called throughout our file

# * Basic greeting function:

# ! Defining a Function

def greeting():
    print("Hello World")

# ! Calling a Function

greeting()

# ! Parameters and Arguments

# ! Parameter(s) - Defined with the function, placeholder for data passed to the function
# ! Argument(s) - Passed to the function when calling it, fulfilling the parameter(s)

# * 'greet_by_name' example:

def greet_by_name(name):
    print(f"Hello {name}")

# * Try to call our function without an argument:

# greet_by_name()

# * To supply an argument to our function we pass the value inside of the brackets when calling it

greet_by_name("Dave")

# * Example with multiple parameters

def add(a,b):
    print(a + b)

# * Calling a function with multiple arguments

add(2,8)

# ! Default Arguments
# * We can use default arguments as fallbacks in case arguments are not supplied
# * To define default arguments treat the pararmeters like variables and assign a value
# * The default will only be used if no argument is supplied

def greet_user(message = "Hello", name = "User"):
    print(f"{message} {name}")

# * If we pass just one argument it fulfills the first parameter automatically

greet_user("Good Afternoon")

greet_user("Dave")

# * If we wish to supply a value to a specific parameter we would need to reference it and pass a value

greet_user(name = "Dave")

# ! *args - Starguments
# * DISCLAIMER - Starguments is just a teaching tool and not an official name 
# * offically referred to as '*args'

# * Starguments allows us to pass an unknown number of arguments to a function 

def add_numbers(*nums):
    print(sum(nums))

add_numbers(2,3,4,10,11,100,1000)

# ! Return Statement
# * All previous examples have been priting a value
# * 'return' allows us to work with the result of a function

def multiply(a,b):
    return a * b

# * TO see the output of a function using return we would need to call it inside 'print()'

print(multiply(5,5))

# * We can store the result of a function ina variable to be used at a later stage

one_hundred = multiply(10,10)
print(one_hundred)

# ! Modules
# * Modules are imported into our files in order to access functionality from them
# * Built-In Example: Random

# * Import a module:

import random

# * Import a module under an alias
# * Think of it as renaming a module for ease of reference

# import random as r

# * random.random() - Generates a float between 0-1
random_float = random.random()
print(random_float)

# * random.randint() - Generate a random integer between a range
# * randint(a,b) - a is the start of the range and b is the end
random_num = random.randint(1,1000)
print(random_num)


# ! STUDENT TASKS ! 
"""

Python - Day 2 (PM) - Tasks:

1: Write functions that meet the following criteria in order to familiarize yourself with how they work:

- A function that uses input to obtain a user's name and returns a string greeting them by their name.
- A function with parameters of 'name' and 'age' that returns a string containing the 'name' and 'age' supplied to it as arguments. Set a default argument of 'unknown' for 'age'.
- A function that uses input to obtain a users name and age and checks whether or not the user is over the age of 18. If the user is over the age of 18, return a string containing their name advising that their sign-up has been successful. If a user is under the age of 18, return a string containing their name and age advising that they are unable to register due to their age.

2: Create your own custom module containing the functions from Task 1:

- Create a file named 'my_functions.py'.
- Import your file as a module into a 'main.py' file.
- Use all 3 of the created functions from the module in your 'main.py' file.

https://www.programiz.com/python-programming/modules

3: Familiarise yourself with Scope in Python:

https://www.programiz.com/python-programming/global-local-nonlocal-variables


Stretch Task: 

Guess the Number V2: Write a function called 'guess_the_number' that starts the game when called. 

Use the random module to generate a random number between 1 and 100. Each turn the user should guess a number, feedback to the user whether their guess is too high, too low or correct. The game should continue until the user guesses the correct number. 

Additional Challenges:

https://www.hackinscience.org/exercises/

https://www.practicepython.org/

"""

import practice
print(practice.username)








# Formatted Message - Signify end of Output
print(f"{format_output}---END---{format_reset}")







































