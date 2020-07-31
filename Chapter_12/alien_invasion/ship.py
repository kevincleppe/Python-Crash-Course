import pygame

class Ship:

    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings


        self.image = pygame.image.load('/Users/kev/Desktop/python/Python-Crash-Course/Chapter_12/alien_invasion/ship.bmp')
        self.rect = self.image.get_rect()

        #Start each new ship at the bottom center of the screen
        self.rect.midbottom =self.screen_rect.midbottom
        self.x = float(self.rect.x)

        self.moving_right =False
        self.moving_left =False 

    def update(self):
        if self.moving_right:
            self.x +=self.settings.ship_speed
        if self.moving_left:
            self.x -=self.settings.ship_speed
            
        #Adjusting ship speed 
        self.rect.x = self.x

    def blitme(self):
        self.screen.blit(self.image, self.rect)