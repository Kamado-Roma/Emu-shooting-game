import pygame
class Player():
    
    def __init__(self,x,y,image):
        self.image = image
        self.rect = image.get_rect(x=x,y=y)
        self.velocity = 250
        self.flipped = True
        
        
    def draw(self, screen):
        flipped_img = pygame.transform.flip(self.image,self.flipped,False)
        screen.blit(flipped_img,(self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (0,255,0),(self.rect.x,self.rect.y,self.rect.w,self.rect.h), 1)
    def move(self, dt):
        pressed = pygame.key.get_pressed()
        dx = 0
        if pressed[pygame.K_d]:
            dx = 1
            self.flipped = True
        if pressed[pygame.K_a]:
            dx = -1
            self.flipped = False
            
        self.rect.x += dx * self.velocity * dt
        self.check_wall()
        
    def check_wall(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 800 - self.rect.w:
            self.rect.x = 800 - self.rect.w