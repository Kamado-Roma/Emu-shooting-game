import pygame

class Bullet(pygame.sprite.Sprite):
    
    def __init__(self, x,y,image):
        super().__init__()
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        
    def draw(self,screen):
        screen.blit(self.image,(self.rect.x,self.rect.y))
    
    def update(self):
        self.rect.y -= 5
        self.check_wall()
    def check_wall(self):
        if self.rect.y <= 0:
            self.kill() 