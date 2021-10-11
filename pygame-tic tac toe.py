# Bugs:

# Extra:
# Add the option to let a player choose his sign
# Make a decent board





def turns():
    while(checkwinO() == checktie() == checkwinX() == False):
        Xrow = input("X's turn, please enter a row and a collum: ")
        Xcol = input()
        getinput('X', int(Xrow-1), int(Xcol-1))
        Orow = input("O's turn, please enter a row and a collum: ")
        Ocol = input()
        getinput('O', int(Orow), int(Ocol))



def getinput(sign,row,col):
    if(board[int(row-1)][int(col-1)] != "*"):
        print("Please choose a different spot, this one is taken")
    else:
        board[int(row-1)][int(col-1)] = sign
    printboard()

def checkwinX():
    if board[0][0] == board[1][1] == board[2][2] == 'x':        # check first alahson
        return True
    elif board[2][0] == board[1][1] == board[0][2] == 'x':      # check second alahson
        return True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'x':    # check every row
            return True
        elif board[0][i] == board[1][i] == board[2][i] == 'x':  # check every collum
            return True
    return False

def checkwinO():
    if board[0][0] == board[1][1] == board[2][2] == 'o':        # check first alahson
        return True
    elif board[2][0] == board[1][1] == board[0][2] == 'o':      # check second alahson
        return True
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == 'o':    # check every row
            return True
        elif board[0][i] == board[1][i] == board[2][i] == 'o':  # check every collum
            return True
    return False


#          0    1    2
board = [['*', '*', '*'],  # 0
         ['*', '*', '*'],  # 1
         ['*', '*', '*']]  # 2

def checktie():
    for row in range(3):
        for col in range(3):
            if(board[row][col] == '*'):
                return False
    return True



def printboard():
    print(board[0])
    print(board[1])
    print(board[2])

def game():
    printboard()
    while(checkwinO() == checkwinX() == checktie() == False):
        sign = input("pls enter the sign row and collum")
        row = input()
        col = input()
        getinput(sign, int(row), int(col))
        turns()
    if(checkwinO()):
        print("O won!")
    if(checkwinX()):
        print("X won") 
    if(checktie()):
        print("It's a tie!")
game()











