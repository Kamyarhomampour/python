# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

"""

Python - Day 2 (PM) - Tasks:

1: Write functions that meet the following criteria in order to familiarize yourself with how they work:

- A function that uses input to obtain a user's name and returns a string greeting them by their name.
- A function with parameters of 'name' and 'age' that returns a string containing the 'name' and 'age' supplied to it as arguments. Set a default argument of 'unknown' for 'age'.
- A function that uses input to obtain a users name and age and checks whether or not the user is over the age of 18. If the user is over the age of 18, return a string containing their name advising that their sign-up has been successful. If a user is under the age of 18, return a string containing their name and age advising that they are unable to register due to their age."""
def username():
    greetings=input("Hello,What is yor name?")
    greeting1=f"Hello {greetings}"
    return greeting1
print(username())

def details(name,age="unknown"):
    return f"Hello {name} you are age is {age}"
print(details("kamyyy"))

def username1():
    name = input("Whats your name?")
    age = int(input ("how old are you?"))
    if age>18:
        return(f"you are{age} so you can buy this item")
    else:
        return(f"you are younger than 18 you cant buy this item")
print(username1())

""": Create your own custom module containing the functions from Task 1:

- Create a file named 'my_functions.py'.
- Import your file as a module into a 'main.py' file.
- Use all 3 of the created functions from the module in your 'main.py' file."""


# def check_registration():
#     name = input("Please enter your name: ")
#     age = int(input("Please enter your age: "))
    
#     if age > 18:
#         return f"Hello, {name}! Your sign-up has been successful."
#     else:
#         return f"Hello, {name}. You are {age} years old, and you are unable to register due to your age."

# # Example usage
# print(check_registration())













































# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")