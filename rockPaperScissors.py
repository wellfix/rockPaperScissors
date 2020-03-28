import random

print("Rock, Paper, Scissors Game ")
player = input("Please choose: \"Rock\", \"Paper\" or \"Scissors\" \n").lower()
ai = random.choice(['rock', 'paper', 'scissors'])

if player == ai:
    print("It's a tie!")
elif (player == 'rock' and ai == 'scissors') \
        or (player == 'paper' and ai == 'rock') \
        or (player == 'scissors' and ai == 'paper'):
    print("You've beaten "+ ai.capitalize() + " with " + player.capitalize() +"!")
elif (ai == 'rock' and player == 'scissors') \
        or (ai == 'paper' and player == 'rock') \
        or (ai == 'scissors' and player == 'paper'):
    print("Your "+ player.capitalize() + " has been beaten by " + ai.capitalize() +"!")
else:
    print("You haven't chosen: \"Rock\", \"Paper\" or \"Scissors\"!")