import sys 

import pygame

from settings import Settings

class AlienInvasion:

    def __init__(self):
        pygame.init()
        #Will create the display for the game
        pygame.display.set_caption("Alien Invasion")
        self.settings = Settings()

        self.screen=pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        

    #Controls the game, returns a list of events that have taken place inside the loop
    def run_game(self):
        while True:
            #Used to access the events that Pygame detects
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            #Tells the game to make most recently drawn screen visible
            #Continually updates screen, hiding previous one 

            self.screen.fill(self.settings.bg_color)      
            pygame.display.flip()

            #Redraw the screenduring each loop

if __name__ == '__main__':
    ai=AlienInvasion()
    #Game will only run if called directly 
    ai.run_game()