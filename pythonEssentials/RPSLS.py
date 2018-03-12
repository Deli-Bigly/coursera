
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

import random

humanScore      = 0
computerScore   = 0

def nameToNumber(name):
        if name == "rock":
                number = 0
                return number
        elif name == "Spock":
                number = 1
                return number
        elif name == "paper":
                number = 2
                return number
        elif name == "lizard":
                number = 3
                return number
        elif name == "scissors":
                number = 4
                return number
        else:
                print ("This was an invalid input, \n Valid inputs: 'rock' 'Spock' 'paper' 'lizard' 'scissors'")

def numberToName(number):
        if number == 0:
                name = "rock"
                return name
        elif number == 1:
                name = "Spock"
                return name
        elif number == 2:
                name = "paper"
                return name
        elif number == 3:
                name = "lizard"
                return name
        elif number == 4:
                name = "scissors"
                return name
        else:
                print ("This was an invalid input, \n Valid inputs: '0' '1' '2' '3' '4'")


def RPSLS(playersChoiceString):

        #print a new line between each game
        print()

        #Display the players choice
        print("Human has selected: ", playersChoiceString)

        #determine players number
        playersChoiceInt = nameToNumber(playersChoiceString)

        #Choose what the computer will select
        computersChoiceInt = random.randint(0,4)

        #convert the computers number choice to the string
        computersChoiceString = numberToName(computersChoiceInt)
        print("Computer chooses: ", computersChoiceString)

        #determine the difference of comp and human mod 5
        difference = (computersChoiceInt - playersChoiceInt) % 5

        #determine winner
        if difference == 0:
                print("The game has ended in a tie!")
        elif (difference == 1) or (difference == 2): 
                print("Computer Wins!")
                global computerScore
                computerScore = computerScore + 1
        else: 
                print("Human Wins!")
                global humanScore
                humanScore = humanScore + 1

        print("Human Score: ", humanScore, "Computer Score: ", computerScore)




RPSLS("Spock")
RPSLS("scissors")
RPSLS("paper")
RPSLS("rock")
RPSLS("lizard")