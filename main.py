import pygame
from pong import *

pygame.init()

setting_win = (700, 500)
setting_board = (30, 300)

window = pygame.display.set_mode(setting_win)
pygame.display.set_caption("PONG")

player_left = Board(10,                                             #x
                    setting_win[1] // 2 - setting_board[1] // 2,    #y 
                    setting_board[0],                               #width
                    setting_board[1],                               #height
                    (255,255,255),                                  #color
                    5)                                              #speed
player_right = Board(setting_win[0] - setting_board[0] - 10,        
                     setting_win[1] // 2 - setting_board[1] // 2, 
                     setting_board[0], 
                     setting_board[1], 
                     (255,255,255), 
                     5)

clock = pygame.time.Clock()

game = True
while game:
    window.fill((0,0,0))

    player_left.move(window)
    player_right.move(window)

    pygame.draw.line(window, (255, 255, 255), (setting_win[0] // 2, 0), (setting_win[0]// 2, setting_win[1]), 3)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player_left.MOVE["UP"] = True
            elif event.key == pygame.K_s:
                player_left.MOVE["DOWN"] = True
            if event.key == pygame.K_UP:
                player_right.MOVE["UP"] = True
            elif event.key == pygame.K_DOWN:
                player_right.MOVE["DOWN"] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                player_left.MOVE["UP"] = False
            elif event.key == pygame.K_s:
                player_left.MOVE["DOWN"] = False
            if event.key == pygame.K_UP:
                player_right.MOVE["UP"] = False
            elif event.key == pygame.K_DOWN:
                player_right.MOVE["DOWN"] = False


    clock.tick(60)
    pygame.display.flip()
        
