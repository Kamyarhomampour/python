format_output = "\033[47m\033[30m"
format_reset = "\033[0m"
# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")


questions=(
    "What is the capital of France?",
    "Which element has the chemical symbol O?",
    "What is the largest planet in our solar system?",
    "Who wrote the play Romeo and Juliet?", 
    "What is the main ingredient in traditional Japanese miso soup?")

options=(
    ("A: Berlin", "B: Madrid", "C: Paris", "D: Rome"),
    ("A: Gold", "B: Oxygen", "C: Silver", "D: Iron"),
    ("A: Earth", "B: Mars", "C: Jupiter", "D: Saturn"),
    ("A: William Shakespeare", "B: Charles Dickens", "C: Mark Twain", "D: Jane Austen"),
    ("A: Tofu", "B: Miso paste", "C: Seaweed", "D: Fish"))

answers = ("C", "B", "C", "A", "B")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("--------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess=input("Please enter your guess: ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else :
        print("WRONG")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1

print("--------------------------------")
print(f"You got {score} out of {len(questions)} correct.")






























print(f"{format_output}---END---{format_reset}")