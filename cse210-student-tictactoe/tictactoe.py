# Author: Levi Jones
# Date: 9/20/21
# Assignment: CSE210 Tic-Tac-Toe

def printBoard(board):
    print('\n')
    for i, line in enumerate(board):
        for j, space in enumerate(line):
            print(space, end='')
            if (j < len(line) - 1):
                print('|', end='')
        if (i < len(board) - 1):
            print('\n-+-+-')
    print('\n')

def checkForWin(board):
    for i, line in enumerate(board):
        # Check rows
        if all(space == line[0] for space in line):
            return True
        # Check columns
        if all(line[i] == board[0][i] for line in board):
            return True
    
    # Check diagnals
    if (board[0][0] == board[1][1] == board [2][2]
    or board[0][2] == board[1][1] == board[2][0]):
        return True 
    
    return False

def checkForTie(board):
    for line in board:
        for space in line:
            if space.isnumeric():
                return False
    return True

# Find the row and column of the location
def findTarget(board, index):
    ret = None
    if (0 < index < 10):
        target = [int((index - 1) / 3), (index % 3) - 1]
        # Check if the target space is already filled
        if board[target[0]][target[1]].isnumeric():
            ret = target 
    
    return ret

def main():
    curPlayer = ''
    board = [
        ['1', '2', '3'],
        ['4', '5', '6'],
        ['7', '8', '9']
    ]

    # Main game loop
    while not (checkForWin(board)):
        location = None
        target = None

        if checkForTie(board):
            curPlayer = None
            break

        if curPlayer == 'X':
            curPlayer = 'O'
        else:
            curPlayer = 'X'

        printBoard(board)
        print(f'{curPlayer}\'s turn!')

        while True:
            try:
                location = int(input('Enter a number (1-9): '))
                target = findTarget(board, location)
                if target is None:
                    raise ValueError('Invalid input')
                else:
                    break
            except ValueError:
                print('Invalid number!')

        board[target[0]][target[1]] = curPlayer

    printBoard(board)

    if (curPlayer):
        print(f'{curPlayer}s win! Good game!')
    else:
        print('It\'s a tie!')

    if (input('Do you want to play again? ')[0].lower() == 'y'):
        main()

if __name__ == '__main__':
    main()