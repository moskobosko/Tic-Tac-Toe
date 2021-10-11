# notes:
# find a different function that draw a circle on clicked position

# dad tip:
# add the option to let a player choose backround color

##################################################################################

import pygame

board = [['*', '*', '*'],
         ['*', '*', '*'],
         ['*', '*', '*']]

pygame.init()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (167, 216, 222)
LIGHT_GREEN = (152, 251, 152)
SIZE = (700, 700)
screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Tic Tac Toe")
pos = []
clicked = False



def getinput(sign,row,col):
    if(board[int(row)][int(col)] != "*"):
        print("Please choose a different spot, this one is taken")
    else:
        board[int(row)][int(col)] = sign
    print(board[0])
    print(board[1])
    print(board[2])




def draw_backround():
    screen.fill(LIGHT_BLUE)
    for i in range(2):
        pygame.draw.rect(screen, BLACK, ((SIZE[0]/3)*(i+1) - 7.5, 0, 15, SIZE[1]))
    for i in range(2):
        pygame.draw.rect(screen, BLACK, (0, ((SIZE[1])/3)*(i+1) - 7.5, SIZE[0], 15))
    pygame.display.update()

def draw(cord_list, zero):
    ''' This is what will draw on the screen when the mouse clicks using recursion'''
    pygame.draw.circle(screen, (255-167, 255-216, 255-222), cord_list[zero], 100, 5)
    zero += 1
    if len(cord_list) > zero:
        draw(cord_list, zero)

done = False

clock = pygame.time.Clock()


while not done:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
    draw_backround()
    if pygame.mouse.get_pressed()[0]:
        pos.append(pygame.mouse.get_pos())
        clicked = True

    if clicked == True:
        draw(pos, 0)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
















