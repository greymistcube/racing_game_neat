import sys
import pygame

pygame.init()

class Events:
    def __init__(self):
        self.multiplier = 1
        self.acc = False
        self.dec = False
        self.left = False
        self.right = False
        self.info = False
        self.debug = False
        # temporary debugging feature
        self.stop = False
        return

    def update(self):
        self.info = False
        self.debug = False
        # check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_i:
                self.info = True
            if event.type == pygame.KEYDOWN and event.key == pygame.K_d:
                self.debug = True
        # check for pressed keys and update variables accordingly
        pressed_keys = pygame.key.get_pressed()
        self.acc = pressed_keys[pygame.K_UP]
        self.dec = pressed_keys[pygame.K_DOWN]
        self.left = pressed_keys[pygame.K_LEFT]
        self.right = pressed_keys[pygame.K_RIGHT]
        self.stop = pressed_keys[pygame.K_SPACE]
        for i, pressed in enumerate(pressed_keys[pygame.K_0:pygame.K_0 + 10]):
            if pressed:
                self.multiplier = i
                break
        return
