# Python Day 1 - PM - Conditional Statements

# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"

# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")

# ! Operators

# ! We have 4 main types of operator to consider:
# * Mathematical Operators - (+, -, *, / etc...)
# * Assignement Opertators - (=, +=, -= etc...)
# * Comparison Operators - (==, !=, >, <, >=, <=)
# * Logical Operators - (and, or, not, |)

# TODO: Full List of Operators:
# https://www.programiz.com/python-programming/operators

# ! If Statement
# * If a condition evaluates to true we will run the the code in our if block

num = 99
if num > 100:
    print(f"{num} is greater than 100!")

# * No (parentheses) around our condition
# * Colon ':' after our condition
# * Body of statement is indented rather than wrapped in {curly's}

# ! If Else Statement:
num = 50
if num > 100:
    print(f"{num} is greater than 100!")
else:
    print(f"{num} is less than 100!")

# ! Remember indentation - 'else' should be on the same level as 'if'
# * Colon ':' after our 'else'
# * Followed by our indented 'else' block

# ! If Elif Else Statement:
# * Working with an 'else if' block in Python has one main difference to note
# * Rather than adding an 'else if' block the syntax is 'elif' to reduce characters

num = 70
if num > 1000:
    print(f"{num} is greater than 1000!")
elif num > 100:
    print(f"{num} is bewtween 100 and 1000!")
elif num > 50:
    print(f"{num} is bewtween 50 and 100!")
else:
    print(f"{num} is less than 50!")

# ! Remember indentation - 'elif' should be on the same level as 'if' and 'else'
# * Colon ':' after our 'elif' condition
# * Followed by our indented 'elif' block

# ! Match Statement
# * Equivalent to a Switch in JS
# * Useful for complex comparisons or checking against multiple condition

# * Example: A match statement to check the day of the week and return a message to console

day = "Sunday"
match day:
    case "Monday":
        print("Start of the work week!")
    case "Friday":
        print("Almost the weekend!")
    case "Saturday" | "Sunday":
        print("It's the weekend!")
    case _:
        print("Just another weekday!")

# ! Remember indentation 
# * We use Match rather than Switch
# * We also don't need any 'break' keyword
# ! NOTE: The default case is represented by '_'

# ! STUDENT TASKS ! 
"""

Python - Day 1 (PM) - Tasks:

1: Create your own examples of the following Condtional Statements to famliarise yourself with the syntax:

- If Statement
- If/Else Statement
- If/Elif/Else Statement
- Match Statement

2: Research the 'and' and 'or' operators in Python and put together some example implementations using multiple conditions.

3: Research and create a 'Nested If Statement' to check whether a number is 'positive' or 'negative' and print the result to the console, the statement should also account for the possibility of the number being '0'.

4: Utilise 'input()' to obtain a students test-score (0-100), using a conditional statement assign the the student with the appropraite grade and print the result the conosle:

- 90-100: "A"
- 80-89: "B"
- 70-79: "C"
- 60-69: "D"
- 00-59: "F"

Stretch Task: 

If you manage to complete all of the relevant tasks, feel free to experiment with further implementations or do some pre-reading on Lists and Loops in Python ahead of tomorrow's session.


"""




# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")