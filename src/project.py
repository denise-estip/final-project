import pygame


pygame.init()

#sprite class
class Outfit(pygame.sprite.Sprite):
    def __init__(self, x, y, scale=0.5):
        super().__init__()
        # Load your initial outfit image
        self.scale = scale

        self.outfit_paths = [
            'assets/outfits/base_character.png',
            'assets/outfits/outfit_1.png',
            'assets/outfits/outfit_2.png',
            'assets/outfits/outfit_3.png',
            'assets/outfits/outfit_4.png',
            'assets/outfits/outfit_5.png',
            'assets/outfits/outfit_6.png'
        ]
        
    
    def change_outfit(self, new_image_path):
        # Method to swap the sprite's image
        self.image = pygame.image.load(new_image_path).convert_alpha()
        # Keep the sprite in the same position after changing size
        old_center = self.rect.center
        self.rect = self.image.get_rect(center=old_center)
    


# mobile screen res
resolution = ((540),(960))
#game window
screen = pygame.display.set_mode(resolution)
pygame.display.set_caption("Todays Outfit")

# Create the character sprite
player_character = Outfit((resolution[0]) // 2, 570)

# Create a GroupSingle and add your character
player_group = pygame.sprite.GroupSingle()
player_group.add(player_character)
omg 
#load in button img
r_button = pygame.image.load('assets/R_button.png').convert_alpha()
l_button = pygame.image.load('assets/L_button.png').convert_alpha()
#load title img
title = pygame.image.load('assets/title.png').convert_alpha()
title = pygame.transform.scale_by(title, .5)
#load bg img
background = pygame.image.load('assets/bg.png').convert_alpha()
background = pygame.transform.scale_by(background, .5)


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
r_button = Button(450,600, r_button, 0.5)
l_button = Button(30, 600, l_button, 0.5)
click_sfx = pygame.mixer.Sound('assets/audio/click_sfx.mp3')


def main():

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
        
        #render display
        white = pygame.Color(255, 255, 255) 
        screen.fill(white)
        screen.blit(background, (0,0))
        screen.blit(title,(100,30))

        if r_button.draw():
            print('Clicked')
            player_character.change_outfit('assets/outfits/outfit_1.png')
            click_sfx.play()

        if l_button.draw():
            print('Clicked')
            player_character.change_outfit('assets/outfits/base_character.png')
            click_sfx.play()


        player_group.draw(screen) 
        
        
        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()