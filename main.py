import pygame
import os
import sys
from pygame.constants import MOUSEBUTTONDOWN

board = [['*', '*', '*'],
         ['*', '*', '*'],
         ['*', '*', '*']]
def isempty(row,col):
    if (board[int(row)][int(col)] != "*"):
        return False
    return True

def placeinput(sign,row,col):
    if(isempty(row,col)):
        board[int(row)][int(col)] = sign

def checktie():
    for row in range(3):
        for col in range(3):
            if(board[row][col] == '*'):
                return False
    return True

pygame.init()
WIDTH, HEIGHT, = 750, 750

WIN = pygame.display.set_mode((WIDTH, HEIGHT))  # sets the size of the display
pygame.display.set_caption("Tic Tac Toe")  # sets the name of the window (top left)
WHITE = (255, 255, 255)                    # just the color white in rgb set into a variable
BLACK = (0, 0, 0)
FPS = 69                                   # sets frames per second to 60

X_WIDTH = 200
X_HEIGHT = 200
O_WIDTH = 200
O_HEIGHT = 200

VERT_LINE = pygame.Rect(WIDTH/3 - 25, 0, 50, HEIGHT)
BACKROUND = pygame.image.load(r'C:\Users\Eyal\PycharmProjects\python_chills\Directory\backround.png')
BACKROUND = pygame.transform.scale(BACKROUND, (750, 750))
X_IMAGE = pygame.image.load(r'C:\Users\Eyal\PycharmProjects\python_chills\Directory\x.png')
X_IMAGE = pygame.transform.scale(X_IMAGE, (X_WIDTH, X_HEIGHT))
O_IMAGE = pygame.image.load(r'C:\Users\Eyal\PycharmProjects\python_chills\Directory\o_png\o.png')
O_IMAGE = pygame.transform.scale(O_IMAGE, (O_WIDTH, O_HEIGHT))
pos = []

def draw_backround():
    WIN.fill(WHITE)
    for i in range(2):
        pygame.draw.rect(WIN, BLACK, ((WIDTH/3)*(i+1) - 25, 0, 50, HEIGHT))
    for i in range(2):
        pygame.draw.rect(WIN, BLACK, (0, ((HEIGHT)/3)*(i+1) - 25, WIDTH, 50))
    pygame.display.update()

def drawO(row,col):
    for row in range(3):
        for col in range(3):
            if(board[row][col] == 'o'):
                pygame.draw.circle(WIN, BLACK, (row*250 +125 ,col*250+125), 38, 6)


def main():
    isclicked = False
    turn = 1

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN and isclicked == False:
                isclicked = True
            if event.type == pygame.MOUSEBUTTONUP and isclicked == True:
                isclicked = False
                pos = pygame.mouse.get_pos()
                row = pos[1]
                col = pos[0]
                print(row//250,col//250)
            if board[row//250][col//250] == '*':
                if(turn == 1):
                 board[row//250][col//250] == 'x'
                 turn = 2
            elif(turn == 2):
                board[row // 250][col // 250] == 'o'
                turn = 1
            print(board)









        draw_backround()
    exit()




if __name__ == "__main__":
    main()









