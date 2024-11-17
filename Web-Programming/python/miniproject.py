#import random library which is already build in python 
import random
target = random.randint(1,100)

while True: #we are going to run it regardless of anything 
    userChoice = input("Guess the target or Quit(Q) :") #asked the user to enter the target value
    if(userChoice == "Quit"):
        break
    userChoice = int(userChoice)
    if(userChoice == target):   #if the target value and userchoice is same
        print("Success: Correct Guess!!") 
        break 
    elif(userChoice < target):
        print("Your number was too small. Take a bigger guess...")
    else:
        print("Your number was too big. Take a smaller guess...")

print("-----------------------Game Over------------------")
    


#print(randNum)