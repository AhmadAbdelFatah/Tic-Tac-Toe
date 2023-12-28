import tkinter as tk
import random2

def checkWinner(gameGrid):
    # Checking for all possible winning combinations for player 1
    if (
        (gameGrid[0][0] == 1 and gameGrid[0][1] == 1 and gameGrid[0][2] == 1) or
        (gameGrid[1][0] == 1 and gameGrid[1][1] == 1 and gameGrid[1][2] == 1) or
        (gameGrid[2][0] == 1 and gameGrid[2][1] == 1 and gameGrid[2][2] == 1) or
        (gameGrid[0][0] == 1 and gameGrid[1][0] == 1 and gameGrid[2][0] == 1) or
        (gameGrid[0][1] == 1 and gameGrid[1][1] == 1 and gameGrid[2][1] == 1) or
        (gameGrid[0][2] == 1 and gameGrid[1][2] == 1 and gameGrid[2][2] == 1) or
        (gameGrid[0][0] == 1 and gameGrid[1][1] == 1 and gameGrid[2][2] == 1) or
        (gameGrid[0][2] == 1 and gameGrid[1][1] == 1 and gameGrid[2][0] == 1)
    ):
        return name  # If any condition is True, player 1 wins

    elif (
        (gameGrid[0][0] == 2 and gameGrid[0][1] == 2 and gameGrid[0][2] == 2) or
        (gameGrid[1][0] == 2 and gameGrid[1][1] == 2 and gameGrid[1][2] == 2) or
        (gameGrid[2][0] == 2 and gameGrid[2][1] == 2 and gameGrid[2][2] == 2) or
        (gameGrid[0][0] == 2 and gameGrid[1][0] == 2 and gameGrid[2][0] == 2) or
        (gameGrid[0][1] == 2 and gameGrid[1][1] == 2 and gameGrid[2][1] == 2) or
        (gameGrid[0][2] == 2 and gameGrid[1][2] == 2 and gameGrid[2][2] == 2) or
        (gameGrid[0][0] == 2 and gameGrid[1][1] == 2 and gameGrid[2][2] == 2) or
        (gameGrid[0][2] == 2 and gameGrid[1][1] == 2 and gameGrid[2][0] == 2)
    ):
        return "computer"


# Gather user information and preferences
name = input("What's your name? ").capitalize()
wannaPlay = input(f"Hi, {name} would you like to play X-O Game? (Enter Yes/No) ").lower()

# Start the game if user wants to play
if wannaPlay != "yes":
    print("That's cool, have a good day!")
else:
    print("That's Nice \n")
    user = input("What would you prefer? 'X' or 'O': ").lower()
    if user == 'x':
        computer = 'o'
    elif user == 'o':
        computer = 'x'

    user, computer = "", ""
    row, column = 3, 3
    grid = [[0 for _ in range(row)] for _ in range(column)]
    U, C = 0, 0  # U -> user's attempt / C -> computer's attempt
    lastPLayer = ""
    userScore, computerScore = 0, 0 
    gameOver = False

    for i in range(row):
        for j in range(column):
            if (lastPLayer == "computer" or lastPLayer == ""):
                while True:
                    Row = int(input(f"{name} Enter your row place: "))
                    Col = int(input(f"{name} Enter your col place: "))

                    if (grid[Row][Col] != 0):
                        print("This place is reserved, Try another one. \n")
                    else:
                        grid[Row][Col] = 1
                        U += 1
                        lastPLayer = "user"
                        break

                if (U >= 3 and checkWinner(grid) == name):
                    userScore += 1
                    print(f"{name}, Congratulation You won! \nYour score: {userScore}\n")
                    gameOver = True
                if (U + C == 9):
                    print("Tie, No Winner!")

            if (lastPLayer == "user" and not gameOver):
                while True:
                    Row = random2.randint(0, row - 1)
                    Col = random2.randint(0, column - 1)

                    if (grid[Row][Col] != 0):
                        print(f"Computer's choice: row: {Row} Column: {Col} This place is reserved, Try another one. \n")
                    else:
                        grid[Row][Col] = 2
                        C += 1
                        lastPLayer = "computer"
                        print(f"Computer's choice: row: {Row} Column: {Col} ")
                        break

                if (C >= 3 and checkWinner(grid) == "computer"):
                    computerScore += 1
                    print(f"Hard luck {name}, the computer won! \nIts score: {computerScore}\n")
                    userScore = 0
                    gameOver = True
                    
                if (U + C == 9):
                    print("Tie, No Winner!")

            if gameOver:
                break

        if gameOver:
            break

    
