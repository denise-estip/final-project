import pygame



#sprite class
    # loads each clothing img as sprite grp
    # 


# mobile screen res
resolution = ((1080/2),(1920/2))
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Todays Outfit")

#load in img
start_img = pygame.image.load('assets/R_button.png').convert_alpha()


#button class
class Button():
    def __init__(self, x, y, image):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):
        #draw button on screen
        screen.blit(self.image, (self.rect.x, self.rect.y))

button = Button(100,200, start_img)

def main():
    pygame.init()

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