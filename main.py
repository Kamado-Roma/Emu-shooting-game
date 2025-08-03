import pygame
import random
from player import *
from bullet import *
from enemy import *
class Game():
    
    def __init__(self):
        pygame.init()
        #screen
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Emu Shooting game")
        
        #background
        self.bg = pygame.image.load("Background.jpg")
        self.bg = pygame.transform.scale(self.bg,((800,600)))
        
        #Bullet
        self.bimg = pygame.image.load("Gihuh.png")
        self.bimg = pygame.transform.scale(self.bimg,(175//5, 175//5))
        self.bullet = Bullet(355,500 , self.bimg)
        
        #bullet_group
        self.bullet_group = pygame.sprite.Group()
        
        
        #player
        self.pimg = pygame.image.load("Emu.png")
        self.pimg = pygame.transform.scale(self.pimg,(175//1.85, 175//1.85))
        self.player = Player(350,500, self.pimg, self.bimg)
        #Enemy
        self.eimg = pygame.image.load("Tsukasa.png")
        self.eimg = pygame.transform.scale(self.eimg,(175/1.25, 175//1.25))
        self.enemy_group = pygame.sprite.Group()
        
        #clock
        self.clock = pygame.time.Clock()
        self.start_time = pygame.time.get_ticks()
    def enemy_ai(self):
        current_time = pygame.time.get_ticks()
        if current_time - self.start_time >= 250:
            randomy = random.randint(25,600)
            enemy_r = Enemy(randomy,0,self.eimg)
            self.enemy_group.add(enemy_r)
            self.start_time = current_time
        for enemy in self.enemy_group:
            if enemy.rect.y >= 600:
                enemy.kill()
    def touch_bullet(self):
        for enemy in self.enemy_group:
            for bullet in self.bullet_group:
                if bullet.rect.colliderect(enemy.rect):
                    enemy.kill()
                    bullet.kill()
                    break
    def run (self):
        running = True
        while (running):
            delta_time = self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.bg,(0,0))
            self.player.draw(self.screen)
            bullet = self.player.move(delta_time)
            if bullet is not None:
                self.bullet_group.add(bullet)
            self.bullet_group.draw(self.screen)
            self.bullet_group.update()
            self.enemy_ai()
            self.enemy_group.draw(self.screen)
            self.enemy_group.update()
            self.touch_bullet()
            pygame.display.update()
        pygame.quit()
        
game = Game()
game.run()