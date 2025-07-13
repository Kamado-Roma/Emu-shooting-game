import pygame
from player import *
class Game():
    
    def __init__(self):
        pygame.init()
        #screen
        self.screen = pygame.display.set_mode((800,600))
        pygame.display.set_caption("Emu Shooting game")
        
        #background
        self.bg = pygame.image.load("Background.jpg")
        self.bg = pygame.transform.scale(self.bg,((800,600)))
        
        #player
        self.pimg = pygame.image.load("Emu.png")
        self.pimg = pygame.transform.scale(self.pimg,(175//1.85, 175//1.85))
        self.player = Player(350,500, self.pimg)
        #Enemy
        self.eimg = pygame.image.load("Tsukasa.png")
        self.eimg = pygame.transform.scale(self.eimg,(175/1.25, 175//1.25))
        
        #Bullet
        self.bimg = pygame.image.load("Gihuh.png")
        self.bimg = pygame.transform.scale(self.bimg,(175//5, 175//5))
        
        #clock
        self.clock = pygame.time.Clock()
    def run (self):
        running = True
        while (running):
            delta_time = self.clock.tick(60)/1000
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.bg,(0,0))
            self.player.draw(self.screen)
            self.player.move(delta_time)
            self.screen.blit(self.eimg,(100,50))
            self.screen.blit(self.bimg,(200,50))
            pygame.display.update()
        pygame.quit()
        
game = Game()
game.run()