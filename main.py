import pygame
import numpy

def main():
    # Initialise pygame
    pygame.init()

    # Show window
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()


if __name__ == '__main__':
    main()
