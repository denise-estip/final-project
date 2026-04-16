import pygame


def main():
    pygame.init()
    pygame.display.set_caption("Todays Outfit")

    # mobile screen res
    resolution = (1080,1920)
    screen = pygame.display.set_mode(resolution)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        #render display
        white = pygame.Color(255, 255, 255)
        screen.fill(white)
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()