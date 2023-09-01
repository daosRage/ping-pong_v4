import pygame
from random import uniform

class Board(pygame.Rect):
    def __init__(self, x, y, width, height, color, speed, name= "playerj,hsbg,d"):
        super().__init__(x, y, width, height)
        self.COLOR = color
        self.SPEED = speed
        self.NAME = name
        self.SCORE = 0
        self.MOVE = {"UP": False, "DOWN": False}
        self.FONT = pygame.font.SysFont("Comic Sans MS", 40)

    def move(self, window):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y + self.height < 500:
            self.y += self.SPEED
        pygame.draw.rect(window, self.COLOR, self)

def blit_player_score(window, player_left, player_right, setting_win):
    render_score_left = player_left.FONT.render(str(player_left.SCORE), True, (0, 63, 255))
    render_score_right = player_right.FONT.render(str(player_right.SCORE), True, (0, 63, 255))
    render_name_left = player_left.FONT.render(player_left.NAME, True, (0, 63, 255))
    render_name_right = player_right.FONT.render(player_right.NAME, True, (0, 63, 255))

    window.blit(render_score_left, (setting_win[0] // 2 - 50, 5))
    window.blit(render_score_right, (setting_win[0] // 2 + 20, 5))
    window.blit(render_name_left, (5, 5))
    window.blit(render_name_right, (setting_win[0] - player_right.FONT.size(player_right.NAME)[0] - 5, 5))

class Ball(pygame.Rect):
    def __init__(self, x, y, radius, color, speed):
        super().__init__(x, y, radius * 2, radius * 2)
        self.RADIUS = radius
        self.COLOR = color
        self.SPEED = speed
        self.SPEED_X = self.SPEED
        self.SPEED_Y = 0
        self.COUNT = 0
    
    def move(self, window, player_left, player_right):
        pygame.draw.circle(window, self.COLOR, (self.x + self.RADIUS, self.y + self.RADIUS), self.RADIUS)

        if self.y < 0 or self.y + self.height > 500:
            self.SPEED_Y *= -1
        if self.colliderect(player_left) and self.COUNT > 5:
            self.COUNT = 0
            if player_left.MOVE["UP"]:
                self.SPEED_Y = uniform(self.SPEED // 2, self.SPEED)
                coef = ((self.SPEED_X ** 2 + self.SPEED_Y ** 2) ** 0.5) / self.SPEED
                self.SPEED_X /= coef
                self.SPEED_Y *= -1
            elif player_left.MOVE["DOWN"]:
                self.SPEED_Y = uniform(self.SPEED // 2, self.SPEED)
                coef = ((self.SPEED_X ** 2 + self.SPEED_Y ** 2) ** 0.5) / self.SPEED
                self.SPEED_X /= coef
                
            self.SPEED_X *= -1
        elif self.colliderect(player_right):
            self.COUNT = 0
            if player_right.MOVE["UP"]:
                self.SPEED_Y = uniform(self.SPEED // 2, self.SPEED)
                coef = ((self.SPEED_X ** 2 + self.SPEED_Y ** 2) ** 0.5) / self.SPEED
                self.SPEED_X /= coef
                self.SPEED_Y *= -1
            elif player_right.MOVE["DOWN"]:
                self.SPEED_Y = uniform(self.SPEED // 2, self.SPEED)
                coef = ((self.SPEED_X ** 2 + self.SPEED_Y ** 2) ** 0.5) / self.SPEED
                self.SPEED_X /= coef

            self.SPEED_X *= -1

        self.x += self.SPEED_X
        self.y += self.SPEED_Y
        self.COUNT += 1
        