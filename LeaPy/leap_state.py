# Created by a human
# when:
# 11/11/2015
# 10:11 PM
# monkey number one million with a typewriter
#
# --------------------------------------------------------------------
from eng import *
from listener import *
from box import *

class LeapMotionState(State):
    listener = Listener()
    controller = Leap.Controller()

    def __init__(self):
        State.__init__(self)
        self.controller.add_listener(self.listener)
        x = (600,300)
        self.box = Box(x)
    def check_events(self):
        if self.box.rect.x <= 0: self.box.rect.x = 0
        if self.box.rect.x >= 1200: self.box.rect.x = 1200
        frame = self.controller.frame()
        self.box.moveY(0)
        self.box.moveX(0)
        for hand in frame.hands:
            if hand.id is not None:
                if hand.palm_position[0] < 0: self.box.moveX(-2)
                if hand.palm_position[0] > 0: self.box.moveX(2)
                if hand.palm_position[2] < 0: self.box.moveY(-2)
                if hand.palm_position[2] > 0: self.box.moveY(2)



        for ev in pygame.event.get():
            if ev.type == pygame.QUIT:
                # QUIT LISTENING LEAP!
                self.controller.remove_listener(self.listener)
                self.quit()

    def update_screen(self):
        self.box.update()
        pygame.display.update()
