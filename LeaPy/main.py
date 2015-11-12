# Created by a human
# when:
# 11/11/2015
# 7:49 PM
# monkey number one million with a typewriter
#
# ----------------------------------------------------------------
from eng import *
import os
from leap_state import LeapMotionState
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d, %d" % (120,20)

def main():
    W = 1200
    H = 600
    D = (W, H)
    pygame.init()
    pygame.display.set_mode(D)
    pygame.display.set_caption("LEAP!")
    e = Engine()
    e.current_state = LeapMotionState()
    e.run()