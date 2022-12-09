import pygame
import numpy

def main():
    # Initialise pygame
    pygame.init()

    # Show window
    screen = pygame.display.set_mode((640, 240))

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()
