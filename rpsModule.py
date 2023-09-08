import random

def getUserInput():

        #make variable scope global.
	global user

	user = input("Enter choice (rock, paper, scissors): ")


#List possible actions for the computer.
actions = ["rock", "paper", "scissors"]

def getComputerChoice():
	global computer 
	computer = random.choice(actions)

#Driver function for game play. 
def playRPS():
	print(f"\nYou chose {user}, computer chose {computer}.\n ")
	if (user == computer):
		print("You have drawn.\n")
	elif (user == "rock"):
		if (computer == actions[1]):
			print("You lose!")
		else:
			print("you win!")
	elif (user == "scissors"):
		if (computer == actions[0]):
			print("You lose!")
		else:
			print("You win!")




