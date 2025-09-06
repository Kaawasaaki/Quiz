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

answer = input("What is the full form of HTTP")
if answer.lower() == "hyper text transfer protocol":
    score += 1
    print("DING DING DING!")
else:
    print("Wrong!!")

answer = input("Which of these is compiled into bytecode: Python or C++")
if answer.lower() == "python":
    print("DING DING DING")
    score += 1
else:
    print("Bruh Read a Book")


answer = input("what data type is used to store integers in C/C++ :")
if answer.lower() == "int":
    print("DING DING DING")
    score += 1
else:
    print("Bruh Read a Book")

answer = input("whos the president of the United States?: ")
if answer.lower() == "donald trump"
    score +=  1
    print("DING DING DING")
else:
print("Read a book bruh")

answer = input("Whats the capital of china?")
if answer.lower() = "beijing"
    print("DING DING DING!!")
    score += 1
else:
    print("Read a book bruh")

answer = input("Which is better : cheese popcorn or caramel popcorn")
if answer.lower() = "cheese popcorn"
    print("DING DING DING!!")
    score += 1
else:
    print("You just have bad taste lol")

answer = input("Who won the 2022 world cup: ")
if answer.lower() = "argentina"
    score += 1
    print("DINGDINGDING")
else:
    print("read a book bruh")

answer = input("what is the name of the java interpreter ")
if answer.lower() = "jvm"
    print("DINGDINGDING")
    score += 1
else:
    print("read a book bruh")

answer = input("Who was the leader of nazi Germany?")
if answer.lower = "adolf hitler":
    print("DING DING DING")
    score += 1
else:
    print("Wrong!!")

answer = input("What is Tail of an aerplane called?")
if answer.lower() = "vertical stabilizer"
    score += 1
else:
    print("wrong!!")

answer = input("Full form of GAN")
if answer.lower() == "generative adviseral network":
    print("Corrext")
    score += 1

answer = input("Fastest Interceptor aircraft?")
if answer.lower() == 'mig-25 foxbat':
    print("DING DING DING")
    score += 1
else:
    print("Read a book")

answer = input("what is the tail of aeroplanes called?")
if answer.lower() == 'vertical stabilizer':
    print("DING DING DING")
    score += 1
else:
    print("Read a book")


print("You have scored: ", score)
print("You have scored: " + str((score/18) * 100) + "%")

    
