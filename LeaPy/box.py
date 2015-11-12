# Created by a human
# when:
# 11/12/2015
# 12:02 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame

class Box(pygame.sprite.Sprite):
    def __init__(self,(x,y)):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill((90,190,90))
        self.set_pos(x,y)
        self.xvel = 0
        self.yvel = 0
        self.screen = pygame.display.get_surface()

    def set_pos(self, x,y):
        self.rect.topleft = (x,y)

    def moveX(self,s):
        self.xvel = s

    def moveY(self,s):
        self.yvel = s

    def update(self):
        self.rect.x += self.xvel
        self.rect.y += self.yvel
        self.screen.blit(self.image, self.rect)

