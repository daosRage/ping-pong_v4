import pygame

class Board(pygame.Rect):
    def __init__(self, x, y, width, height, color, speed, name= "player"):
        super().__init__(x, y, width, height)
        self.COLOR = color
        self.SPEED = speed
        self.NAME = name
        self.SCORE = 0
        self.MOVE = {"UP": False, "DOWN": False}

    def move(self, window):
        if self.MOVE["UP"] and self.y > 0:
            self.y -= self.SPEED
        elif self.MOVE["DOWN"] and self.y + self.height < 500:
            self.y += self.SPEED
        pygame.draw.rect(window, self.COLOR, self)