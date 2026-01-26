#This is the python code for lab 2 of week 2
#Juela Topi 101087887 COMP2152 

# Define the choices array
choices = ["Rock", "Paper", "Scissors"]

# Get the player input
playerChoice = input("Enter your choice (1=Rock, 2=Paper, 3=Scissors): ")
playerChoice = int(playerChoice)

# Validate the players input
if playerChoice < 1 or playerChoice > 3:
    print("Error: Choice must be between 1 and 3.")

# Get the computers choice 
computerChoice = input("Enter computer's choice (1-3): ")
computerChoice = int(computerChoice)

# Validate the computers input
if computerChoice < 1 or computerChoice > 3:
    print("Error: Choice must be between 1 and 3.")

# Use array indexing (subtract 1 for 0-based index- human numbering - if user enters 1, then we need index 0)
playerChoiceName = choices[playerChoice - 1]
computerChoiceName = choices[computerChoice - 1]

# Print choices
print("You chose:", playerChoiceName)
print("Computer chose:", computerChoiceName)

# Determine the winner
if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == 1 and computerChoice == 3:
    print("Rock beats Scissors - You win!")
elif playerChoice == 2 and computerChoice == 1:
    print("Paper beats Rock - You win!")
elif playerChoice == 3 and computerChoice == 2:
    print("Scissors beats Paper - You win!")
else:
    print("You lose!")

# String comparison
if playerChoiceName != "Rock":
    print("You didn't pick the classic Rock...")