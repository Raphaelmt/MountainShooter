import pygame
import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(600, 400))

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
