import rpsModule

rpsModule.getUserInput()
rpsModule.getComputerChoice()
rpsModule.playRPS()

playAgain = input("Play again? (Enter y/n) : ")
while playAgain == "y":
	rpsModule.getUserInput()
	rpsModule.getComputerChoice()
	rpsModule.playRPS()