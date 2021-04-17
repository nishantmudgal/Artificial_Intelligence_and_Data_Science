'''
Tic-Tac-Toe Game:

This is the implementation of tic-tac-toe game. Here user can play against the computer.
Computer plays according to implementation of solving Tic-tac-toe using Magic Square.
User gets first chance and then the game continues.

-Nishant Mudgal
'''

import random

board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
magicSquare = [8, 3, 4, 1, 5, 9, 6, 7, 2]
remainingNum = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playerIndex = []
computerIndex = []

def displayBoard():
    print("Board:")
    print(board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('---------')
    print(board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('---------')
    print(board[6] + ' | ' + board[7] + ' | ' + board[8])
    print()

def checkWinner():
    for i in range(3):
        if (board[i*3] == board[i*3+1] == board[i*3+2] == 'X') or (board[i] == board[i+3] == board[i+6] == 'X'):
            return True
            
    if (board[0] == board[4] == board[8] == 'X') or (board[2] == board[4] == board[6] == 'X'):
        return True
        
    return False
    
def winningPosition(currentPlayer):
    if currentPlayer == 'Player':
        index = playerIndex
    else:
        index = computerIndex
        
    for i in index:
        for j in index:
            if i == j:
                continue

            winPos = 15 - (magicSquare[i-1] + magicSquare[j-1])

            if winPos in magicSquare:
                winIndex = magicSquare.index(winPos)
            else:
                continue

            if (winIndex+1) in remainingNum:
                return (winIndex+1)
                
    return -1
    
    
def playTicTacToe():
    
    playerTurn = True
    turnsCount = 0
    playerWon = ''
    
    while playerWon == '' and turnsCount < 9:
        
        if playerTurn:
            userTurn = int(input("Enter your turn : "))
            while userTurn not in remainingNum:
                userTurn = int(input("Enter valid input : "))
                
            board[userTurn - 1] = 'X'
            playerIndex.append(userTurn)
            remainingNum.remove(userTurn)
            playerTurn = False
            
            if checkWinner():
                playerWon = "Player"
            
        else:
            if turnsCount < 3:
                computerTurn = random.choice(remainingNum)
                
            else:
                computerTurn = winningPosition('Computer')
                if computerTurn == -1:
                    computerTurn = winningPosition('Player')
                    if computerTurn == -1:
                        computerTurn = random.choice(remainingNum)
                else:
                    playerWon = "Computer"
            
            print("Computer Enters : " + str(computerTurn))
            board[computerTurn - 1] = 'O'
            computerIndex.append(computerTurn)
            remainingNum.remove(computerTurn)
            playerTurn = True
            
        displayBoard()
        turnsCount = turnsCount + 1
    
    if playerWon == "Computer":
        print("Computer Won!!!")
    elif playerWon == 'Player':
        print("Congratulations!! You Won...")
    else:
        print("Match Draw")


playTicTacToe()
