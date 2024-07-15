# Formatting Variables
format_output = "\033[47m\033[30m"
format_reset = "\033[0m"
# Formatted Message - Signify Start of Output
print(f"{format_output}---START---{format_reset}")
x=15
if 20>x:
    print(" x is less than 20 ")
num=99
if 100>num:
    print (f"{num} is smaller than 100")
else:
    print (f"{num} is bigger than 100")  
# Age=18
age=int(input("How old are you?"))
if age<18:
    print("you are a Teenager")
elif age>=18:
    print("you are older than a teenager")  
elif age> 25 :
    print("you are an adult")
elif age > 35:
    print ("you are a middle age")  
grade= 55
match grade: 
    case 40 :
        print("you have just passed")
    case _ if grade<40:
        print(" you have failed") 
    case _ if grade>50 and grade<60:
        print("You have got 2:2")
    case _ if grade>60 and grade<70:
        print("You have got 2:1")
    case _ if grade>70:
        print("you have got first honour, congrats")    



































# Formatted Message - Signify End of Output
print(f"{format_output}---END---{format_reset}")