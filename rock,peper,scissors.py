import random as rd

choices = ["rock", "peper", "scissors"]
player = input("enter your choice: ")
computer = rd.choice(choices)
#print("computer : ", computer)
while player not in choices :
    print("you should choise frome \"rock, peper, scissors\"")
    player = input("enter your choice: ")
print("computer: ", computer)
if player == computer :
    print("draw")
elif player == choices[0] and computer == choices[1] :
    print("you lose")
elif player == choices[1] and computer == choices[2] :
    print("you lose")
elif player == choices[2] and computer == choices[0] :
    print("you lose")
else :
    print("you win :)")

