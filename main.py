import pygame
import numpy

from characters.miel_monteur import MielMonteur

COLOURS = {
    'gray': (150, 150, 150),
    'blue': (0, 0, 255)
}

MIEL = MielMonteur({'height': 200, 'width': 50}, {}, position={'x': 300, 'y': 500})

characters = [MIEL]


def main():
    # Initialise pygame
    pygame.init()

    # Show window
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)

    # Main loop
    running = True
    while running:
        for event in pygame.event.get():
            # Quit on ESCAPE or close
            if event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                running = False
            if event.type == pygame.QUIT:
                running = False

            # Draw background
            screen.fill(COLOURS['gray'])
            # Draw characters
            for character in characters:
                pygame.draw.rect(screen, COLOURS['blue'], character.rectangle)

            pygame.display.update()

    pygame.quit()


if __name__ == '__main__':
    main()
