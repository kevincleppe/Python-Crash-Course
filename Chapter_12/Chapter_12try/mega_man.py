import pygame

class Mega:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()


        self.image = pygame.image.load('/Users/kev/Desktop/python/Python-Crash-Course/Chapter_12/Chapter_12try/mega.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom =self.screen_rect.midbottom

    def blitme(self):
        self.screen.blit(self.image, self.rect)