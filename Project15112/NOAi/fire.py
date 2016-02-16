# fire.py
import os, pygame, configure


class Fire(pygame.sprite.Sprite):
    """docstring for Fire"""
    def __init__(self,position): # position assumed as tuple of nextpoint
        super(Fire, self).__init__()
        self.c = configure.Configure()
        fireImagePath = self.c.IMAGE_PATH + "explosion_c.png"
        self.image = pygame.image.load(fireImagePath).convert_alpha()
        # we need a function bombable ~~~~
        self.position = position
        tSize = self.c.TILE_SIZE
        self.rect = pygame.Rect(position[0],position[1],tSize,tSize)

        self.time = 1

    def fire(self):
        self.time -= 1
        return self.time <= 0