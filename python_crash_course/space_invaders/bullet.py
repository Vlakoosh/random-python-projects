import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    #Class used for managing bullets in the alien invasion game
    
    def __init__(self, ai_game):
        #Creating a bullet at the current ship position
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        #Creting a bullet rectangle at the (0,0) point and defining its "real" position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop
        
        #Position of the bullet using a float value rather than an int
        self.y = float(self.rect.y)
    
    def update(self):
        #Moving the bullet across the screen
        
        #Updating bullet's position
        self.y -= self.settings.bullet_speed
        #Updating bullet's rectangle's position
        self.rect.y = self.y
    
    def draw_bullet(self):
        #Showing the bullet on the screen
        pygame.draw.rect(self.screen, self.color, self.rect)
        
        