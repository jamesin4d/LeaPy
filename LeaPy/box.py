# Created by a human
# when:
# 11/12/2015
# 12:02 AM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
import pygame as pg

class Box(pg.sprite.Sprite):
    def __init__(self,(x,y)):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((32,32))
        self.rect = self.image.get_rect()
        self.image.fill((130,130,135))
        self.set_pos(x,y)
        self.xvel = 0
        self.yvel = 0
        self.screen = pg.display.get_surface()

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
        pg.display.update(self.rect)
