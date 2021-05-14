from random import randint

game_inputs = ['s','w','g']

print("\n\n\t\t\t\t\t------Welcome to the Game------")
print("\t\t\t\t\t        Snake Water Gun        ")
print("\nGame Rules :-")
print("\nFor Snake press - s\nFor Water press - w\nFor Gun press - g")

playerName = input("\nEnter Your Name = ")
attempt = int(input("Enter how many time you want to play = "))
playerScore = 0
computerScore = 0

print("\n\t\t\t\t\t-------let's Start the Game-------")
for i in range(attempt):
    
    print(f"\nAttempt Number - {i+1} ")
    playerInput = input("Enter Your choice [s/w/g]= ")
    computerInput = game_inputs[randint(0,2)]
    
    print("Result - ",end="")
    if playerInput.lower() == computerInput:
        print("Draw")
    elif playerInput.lower() == 's':
        if computerInput == 'w':
            print(f"{playerName} Win")
            playerScore += 1
        else:
            print("Computer Win")
            computerScore += 1
    elif playerInput.lower() == 'w':
        if computerInput == 'g':
            print(f"{playerName} Win")
            playerScore += 1
        else:
            print("Computer Win")
            computerScore += 1
    elif playerInput.lower() == 'g':
        if computerInput == 'w':
            print(f"{playerName} Win")
            playerScore += 1 
        else:
            print("Computer Win")
            computerScore += 1
    
    print(f"{playerName} = {playerScore} and Computer = {computerScore}")

print(f"\nPlayer {playerName} score = {playerScore}")
print(f"Computer score = {computerScore}")
