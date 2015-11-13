# Created by a human
# when:
# 11/12/2015
# 6:40 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from box import *

class Bullet(Box):
    def __init__(self, x,y, direction):
        Box.__init__(self)
        self.set_pos(x,y)
        self.direction = direction
        if self.direction == 'south': self.yvel = 10
        if self.direction == 'north': self.yvel = -10
        if self.direction == 'east': self.xvel = 10
        if self.direction == 'west': self.xvel = -10
