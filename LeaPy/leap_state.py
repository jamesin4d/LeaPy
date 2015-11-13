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
from bullet import Bullet
import random
random.seed

class LeapMotionState(State):
    listener = Listener()
    controller = Leap.Controller()

    def __init__(self):
        State.__init__(self)
        self.controller.add_listener(self.listener)
        self.canvas = pygame.Surface((1200,600))
        self.canvas.fill((150,150,210))
        self.canvas.convert()
        self.canv_rect = self.canvas.get_rect()
        self.sw_dir = None
        self.bullets = []
        x = (600,300)
        self.box = Box(x)

    def produce_bullets(self):
        if len(self.bullets) <= 20:
            pass


    def check_events(self):
        self.box.check_screen_bounds()
        frame = self.controller.frame()
        self.box.moveY(0)
        self.box.moveX(0)
        for hand in frame.hands:
            #if hand.id is not None:
                if hand.palm_position[0] < 0: self.box.moveX(-10)
                if hand.palm_position[0] > 0: self.box.moveX(10)
                if hand.palm_position[2] < 0: self.box.moveY(-10)
                if hand.palm_position[2] > 0: self.box.moveY(10)

        for gesture in frame.gestures():
            if gesture.type == Leap.Gesture.TYPE_SWIPE:
                swipe = SwipeGesture(gesture)
                self.sw_dir = swipe.direction
        # print 'swiper, no swiping!'
        for ev in pygame.event.get():
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_ESCAPE:
                    self.controller.remove_listener(self.listener)
                    self.quit()
                    pygame.QUIT
            if ev.type == pygame.QUIT:

                # QUIT LISTENING LEAP!
                self.controller.remove_listener(self.listener)
                self.quit()

    def update_screen(self):
        self.screen.blit(self.canvas, self.canv_rect)
        self.box.update()
        info(str(self.sw_dir), 1)
        pygame.display.update()
