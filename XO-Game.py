import tkinter as tk
from tkinter import font
import random

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
        return "Player"  # If any condition is True, player wins

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
        return "Computer"  # If any condition is True, computer wins

# Restart Button
def restartGame():
    global grid, userCount, compCount, lastPlayer, userScore, computerScore, gameOver

    grid = [[0 for _ in range(3)] for _ in range(3)]
    userCount, compCount = 0, 0
    lastPlayer = ""
    userScore, computerScore = 0, 0
    gameOver = False
    userScoreLabel.config(text=f"Player: {userScore}")
    computerScoreLabel.config(text=f"Computer: {computerScore}")
    statusLabel.config(text="")

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text="", state=tk.NORMAL, bg='SystemButtonFace')  # Reset background color
    print("Game restarted.")

# Button Creation
def createButtonClick(row, col):
    def onButtonClick():
        onButtonClickWithParams(row, col)
    return onButtonClick

def onButtonClickWithParams(row, col):
    global grid, userCount, compCount, lastPlayer, userScore, computerScore, gameOver

    #User's turn to choose their place
    if (lastPlayer == "Computer" and not gameOver or lastPlayer == ""):
        if grid[row][col] == 0:
            buttons[row][col].config(text="X", font=customFont, bg='aqua')
            grid[row][col] = 1
            userCount += 1
            lastPlayer = "Player"

            if userCount >= 3 and checkWinner(grid) == "Player":
                userScore += 1
                userScoreLabel.config(text=f"Player: {userScore}")
                statusLabel.config(text=f"Congrats You Won!", font=customFont)
                gameOver = True
                
            if userCount + compCount == 9 and not gameOver:
                gameOver = True
                statusLabel.config(text="Tie! No Winner.", font=customFont)
                for button_row in buttons:
                    for button in button_row:
                        button.config(bg='red')
                
        #Computer's turn to choose its turn
        if (lastPlayer == "Player" and not gameOver ):
            while True:
                row = random.randint(0, 2)
                col = random.randint(0, 2)
                if grid[row][col] == 0:
                    buttons[row][col].config(text="O", font=customFont, bg='yellow')
                    grid[row][col] = 2
                    compCount += 1
                    lastPlayer = "Computer"

                    if compCount >= 3 and checkWinner(grid) == "Computer":
                        computerScore += 1
                        computerScoreLabel.config(text=f"Computer: {computerScore}")
                        statusLabel.config(text=f"Computer Won!", font=customFont)
                        gameOver = True
                        if (gameOver == True): #exit the function to prevent infinity
                            return

                    if userCount + compCount == 9 and not gameOver: # that indicates that a user and computer marked the entire grid without winning
                        gameOver = True
                        statusLabel.config(text="Tie! No Winner.", font=customFont)
                        for button_row in buttons:
                            for button in button_row:
                                button.config(bg='red')
                    break

#Frame
root = tk.Tk()
root.title("Tic Tac Toe")
customFont = font.Font(family="Helvetica", size=9, weight="bold")


grid = [[0 for _ in range(3)] for _ in range(3)]
buttons = [[None for _ in range(3)] for _ in range(3)]
userCount, compCount = 0, 0
lastPlayer = ""
userScore, computerScore = 0, 0
gameOver = False

#restart Button 
restartButton = tk.Button(root, text="Restart", command=restartGame, pady=10, padx=10, font=customFont)
restartButton.grid(row=4, column=0, columnspan=3)

#User label
userScoreLabel = tk.Label(root, text=f"Player: {userScore}")
userScoreLabel.grid(row=2, column=0)
userScoreLabel.config(font=customFont)

#Computer label
computerScoreLabel = tk.Label(root, text=f"Computer: {computerScore}")
computerScoreLabel.grid(row=2, column=2, pady=10)
computerScoreLabel.config(font=customFont)

#Status label
statusLabel = tk.Label(root, text="")
statusLabel.grid(row=3, column=0, columnspan=3)

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text=" ", width=10, height=5)
        buttons[i][j].config(command=createButtonClick(i, j))
        buttons[i][j].grid(row=i+6, column=j)

root.mainloop()
