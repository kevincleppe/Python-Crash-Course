import sys 

import pygame

from ship import Ship

from settings import Settings

class AlienInvasion:

    def __init__(self):
        pygame.init()
        #Will create the display for the game
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.ship = Ship(self)

    #Controls the game, returns a list of events that have taken place inside the loop
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()
            self.ship.update()

    def _check_events(self):
            #Used to access the events that Pygame detects
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Tells the game to make most recently drawn screen visible
            #Continually updates screen, hiding previous one 
                elif event.type == pygame.KEYDOWN:
                    if event.key ==pygame.K_RIGHT:
                        self.ship.moving_right = True
                    elif event.key == pygame.K_LEFT:
                        self.ship.moving_left = True

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.ship.moving_right = False
                    elif event.key==pygame.K_LEFT:
                        self.ship.moving_left = False
                
                

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)  

            self.ship.blitme() 

            pygame.display.flip()

if __name__ == '__main__':
    ai=AlienInvasion()
    #Game will only run if called directly 
    ai.run_game()