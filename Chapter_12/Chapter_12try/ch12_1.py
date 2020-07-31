import sys 

import pygame

from mega_man import Mega

from chap12_1_settings import Try_Settings

class Mega_Man:

    def __init__(self):
        pygame.init()
        #Will create the display for the game
        pygame.display.set_caption("Mega Man")
        self.settings = Try_Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        
        self.ship = Mega(self)

    #Controls the game, returns a list of events that have taken place inside the loop
    def run_game(self):
        while True:
            self._check_events()
            self._update_screen()

    def _check_events(self):
            #Used to access the events that Pygame detects
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Tells the game to make most recently drawn screen visible
            #Continually updates screen, hiding previous one 

    def _update_screen(self):
            self.screen.fill(self.settings.bg_color)  

            self.ship.blitme() 

            pygame.display.flip()

if __name__ == '__main__':
    ai=Mega_Man()
    #Game will only run if called directly 
    ai.run_game()