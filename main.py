"""
Rock paper scissors
"""
from random import randint
import cgi

choices = ["Rock", "Paper", "Scissors"]
computerChoice = choices[randint(0,2)]

GameEnd = False

while GameEnd == False:
    playerChoice = input ("Choose Rock, Paper or Scissors:")
    if playerChoice == computerChoice:
        print ("Play again it was a tie")
    elif playerChoice == "Rock":
        if computerChoice == "Paper":
            print ("You Lose, Computer Choose: " + computerChoice)
            GameEnd = True
        else:
            print ("You Win, Computer Choose: " + computerChoice)
            GameEnd = True
    elif playerChoice == "Scissors":
        if computerChoice == "Rock":
            print ("You Lose, Computer Choose: " + computerChoice)
            GameEnd = True
        else:
            print ("You Win, Computer Choose: " + computerChoice)
            GameEnd = True
    elif playerChoice == "Paper":
        if computerChoice == "Scissors":
            print ("You Lose, Computer Choose: " + computerChoice)
            GameEnd = True
        else:
            print ("You Win, Computer Choose: " + computerChoice)
            GameEnd = True
    else:
        print ("invalid input")
