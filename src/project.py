import pygame



#sprite class
class Outfit(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
    # loads each outfit img as sprite grp
    


# mobile screen res
resolution = ((540),(960))

#game window
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Todays Outfit")

#load in button img
start_img = pygame.image.load('assets/R_button.png').convert_alpha()


#button class
class Button():
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (int(width * scale), int(height * scale)))
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)
        self.clicked = False

    def draw(self):
        action = False
        #get mouse position
        pos = pygame.mouse.get_pos()
        
        #check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True
        
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        #draw button on screen
        screen.blit(self.image, ((self.rect.x), self.rect.y))

        return action


# create button instance
button = Button(400,500, start_img, 0.5)

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

        if button.draw():
            print('Clicked')
            
        
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()