import pygame



#sprite class
    # loads each clothing img as sprite grp
    # 

#button class
    # get mouse pos
    # when clicked change sprite
    # button sprite gets smaller when clicked

def main():
    pygame.init()
    pygame.display.set_caption("Todays Outfit")

    # mobile screen res
    resolution = ((1080/2),(1920/2))
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