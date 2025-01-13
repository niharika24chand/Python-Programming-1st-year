#Guess the number
import random
target=random.randint(1,10)
while True:
    userChoice=int(input("Guess the target: "))
    if(userChoice == target):
        print("Success:Correct Guess!!")
        break
    elif(userChoice > target):
        print("Incorrect: Your guess is to big try to guess a smaller number")
    else:
        print("Incorrect: Your guess is to small try to guess a bigger number")
print("____GAME OVER____")
