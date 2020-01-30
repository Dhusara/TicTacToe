# Beginner game TicTacToe on Python
# Made by Sergei Demianenko

# --- Global variables ---

# Game board
board = ["-", "-", "-",
         "-", "-", "-", 
         "-", "-", "-"]

# If game is still going
gameStillGoing = True

# Who won? Or tie?
winner = None

# Whos turn
currentPlayer = "X"

# --- Functions ---

# Display the game board to the screen
def displayBoard():
    print("\n")
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])
    print("\n")

# Play a game
def playGame():

    # Display your board
    displayBoard()

    # While the game is still going
    while gameStillGoing:

        # Hangle a single turn
        handleTurn(currentPlayer)
        
        # Check if game is over
        checkIfGameIsOver()

        # Flip to other player
        flipPlayer()

    # The game has ended
    if winner == "X" or winner == "O":
        print(winner + " won.")
    elif winner == None:
        print("Tie.")


# Handle a single turn
def handleTurn(player):

    print(player + "'s turn.")

    position = input("Choose your position from 1 to 9: ")

    valid = False
    while not valid:

        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Choose position from 1 to 9: ")

        position = int(position) - 1

        if board[position] == "-":
            valid = True
        else:
            print("You cant go there. Go again.")

    board[position] = player
    displayBoard()

def checkIfGameIsOver():
    checkIfWin()
    checkIfTie()

def checkIfWin():

    # Global variable
    global winner

    # Check rows
    rowWinner = checkRows()

    # Check columns
    columnWinner = checkColumns()

    # Check diagonals
    diagonalWinner = checkDiagonals()

    if rowWinner:
        winner = rowWinner
    elif columnWinner:
        winner = columnWinner
    elif diagonalWinner:
        winner = diagonalWinner
    else:
        winner = None

    return

# Check rows 
def checkRows():
    # Set up global variable
    global gameStillGoing

    # Check if any row has the same value or nothing
    rowOne = board[0] == board[1] == board[2] != "-"
    rowTwo = board[3] == board[4] == board[5] != "-"
    rowThree = board[6] == board[7] == board[8] != "-"

    # If
    if rowOne or rowTwo or rowThree:
        gameStillGoing = False

    # Return the winner (X or O)
    if rowOne:
        return board[0]
    elif rowTwo:
        return board[3]
    elif rowThree:
        return board[6]
    return

# Check columns
def checkColumns():
     # Set up global variable
    global gameStillGoing

    # Check if any column has the same value or nothing
    columnOne = board[0] == board[3] == board[6] != "-"
    columnTwo = board[1] == board[4] == board[7] != "-"
    columnThree = board[2] == board[5] == board[8] != "-"

    # If
    if columnOne or columnTwo or columnThree:
        gameStillGoing = False

    # Return the winner (X or O)
    if columnOne:
        return board[0]
    elif columnTwo:
        return board[1]
    elif columnThree:
        return board[2]
    return

# Check diagonals
def checkDiagonals():
     # Set up global variable
    global gameStillGoing

    # Check if any diagonal has the same value or nothing
    diagonalOne = board[0] == board[4] == board[8] != "-"
    diagonalTwo = board[6] == board[4] == board[2] != "-"

    # If
    if diagonalOne or diagonalTwo:
        gameStillGoing = False

    # Return the winner (X or O)
    if diagonalOne:
        return board[0]
    elif diagonalTwo:
        return board[6]
    return

def checkIfTie():
    # Global variable
    global gameStillGoing
    # Tie logic
    if "-" not in board:
        gameStillGoing = False
    return

def flipPlayer():
    # Global variable
    global currentPlayer

    # If current player was X change it to O
    if currentPlayer == "X":
        currentPlayer = "O"
        # If current player was O change it to X 
    elif currentPlayer == "O":
        currentPlayer = "X"
    return

playGame()