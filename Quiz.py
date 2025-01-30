print("Welcome to the quiz game!")


score = 0


user_input = input("Would you like to play? ")
if user_input.lower() == "no":
    print("See ya!")
    quit()
else:
    print("Lessgo")


answer = input("What is the full form of MSI? ")
if answer.lower() != "micro star international":
    print("Wrong!")
else:
    print("DING DING DING")
    score += 1 
    
answer = input("How many port numbers do a computer have?: ")
if answer.lower() == "65,535":
    print("DING DING DING!!")
    score += 1
else:
    print("Wrong!!")
    
answer = input("What is the full form of IP?: ")
if answer.lower() == "internet protocol":
    print("DING DING DING!!")
    score += 1
else:
    print("Wrong!!")
    
    
answer = input("Which country has the highest gdp in the world?: ")
if answer.lower() == "usa":
    print("DING DING DING")
    score += 1
else:
    print("Wrong!!")
    
    
answer = input("Full form of CPU? ")
if answer.lower() == "central processing unit":
    print("DING DING DING!!")
    score += 1
else:
    print("Wrong!!")
    
    
    
answer = input("What is the nickname given to the SR-71: ")
if answer.lower() == "blackbird":
    print("DING DING DING!!")
    score += 1
else:
    print("Wrong!!")
    
    
print("You have scored: ", score)
print("You have scored: " + str((score/6) * 100) + "%")

    
