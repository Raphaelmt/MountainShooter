import pygame

from Code.Const import WIN_WIDTH, WIN_HEIGHT
from Code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self, ):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # Check for all events
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #        print('Quitting...')
            #        pygame.quit()  # Close window
            #        quit()  # end Pygame
