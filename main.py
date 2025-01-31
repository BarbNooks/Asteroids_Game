import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    print("Starting asteroids!")
    print("Screen width: 1280")
    print("Screen height: 720")

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # when you click X
                running = False
        
        # Fill the screen with black
        screen.fill((0, 0, 0))
        
        # Update the display
        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()
