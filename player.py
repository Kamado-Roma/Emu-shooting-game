import pygame
from bullet import *
class Player():
    
    def __init__(self,x,y,image,bimg):
        self.image = image
        self.bimg = bimg
        self.rect = image.get_rect(x=x,y=y)
        self.velocity = 500
        self.flipped = True
        self.fired = False
        self.update_time = pygame.time.get_ticks()
        
    def draw(self, screen):
        flipped_img = pygame.transform.flip(self.image,self.flipped,False)
        screen.blit(flipped_img,(self.rect.x, self.rect.y))
        pygame.draw.rect(screen, (0,255,0),(self.rect.x,self.rect.y,self.rect.w,self.rect.h), 1)
    def move(self, dt):
        current_time = pygame.time.get_ticks()
        if current_time - self.update_time  >= 120:
            self.fired = False
            self.update_time = current_time 
        bullet = None
        pressed = pygame.key.get_pressed()
        dx = 0
        if pressed[pygame.K_d]:
            dx = 1
            self.flipped = True
        if pressed[pygame.K_a]:
            dx = -1
            self.flipped = False
        if self.fired == False and pressed[pygame.K_SPACE]:
            self.fired = True
            bullet = Bullet(self.rect.x + (self.rect.w // 2) - (self.bimg.get_width()//2), self.rect.y,self.bimg)
            
        self.rect.x += dx * self.velocity * dt
        self.check_wall()
        return (bullet)
    def check_wall(self):
        if self.rect.x <= 0:
            self.rect.x = 0
        if self.rect.x >= 800 - self.rect.w:
            self.rect.x = 800 - self.rect.w