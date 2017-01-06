# tiles.py

import os, pygame, configure
class Tile(pygame.sprite.Sprite):
    """docstring for Tile"""
    def __init__(self, tileType): # tileType will be used in Int
        super(Tile, self).__init__()
        self.c = configure.Configure()
        self.type = tileType
        pygame.display.init()
        self.initAttributes()
        self.bomb = None # None means no bomb here 

        # we need a function bombable ~~~~


    def initAttributes(self):
        # ground
        if self.type == self.c.GROUND:
            self.passable = True
            self.destroyable = False
        # wall
        if self.type == self.c.WALL:
            self.passable = False
            self.destroyable = False
        # brick
        if self.type == self.c.BRICK:
            self.passable = False
            self.destroyable = True
        self.path=self.c.IMAGE_PATH + "tiles/" + str(self.type) + ".png" 
        # special powers
        if (self.type in [self.c.BOMB_UP,self.c.POWER_UP,
                                        self.c.LIFE_UP,self.c.TIME_UP,self.c.DOOR]):

            self.passable = False # when initiate, it should be brick
            self.destroyable = True # this is more fun !
            self.beenDestroyed = False
            self.brickDown = False # the brick cover the bonus

            self.path=self.c.IMAGE_PATH + "tiles/" + str(self.c.BRICK) + ".png" 
        self.image = pygame.image.load(self.path)

    def destroy(self):
        if self.type == self.c.BRICK:
            self.type = self.c.GROUND
            self.initAttributes()
        # the following logic:
            # if the bomb first explodes, it takes down the brcks, set the breakDown
            # second time explodes, it takes down the self 
        elif self.type in [self.c.BOMB_UP,self.c.POWER_UP, self.c.LIFE_UP,self.c.TIME_UP,self.c.DOOR]:
            if self.brickDown == False:
                self.brickDown = True
                self.path = self.c.IMAGE_PATH + "tiles/" + str(self.type) + ".png"
                self.image = pygame.image.load(self.path)
                self.passable = True
            else:
                if self.beenDestroyed == True: # second time 
                    pass
                else: 
                    self.beenDestroyed = True
                    self.type = self.c.GROUND
                    self.initAttributes()

    # I hate this name !!!
    def passableTotal(self):
        return self.bomb == None and self.passable

    def hasPower(self):
        if self.type in [self.c.BOMB_UP,self.c.POWER_UP,self.c.LIFE_UP,self.c.TIME_UP,self.c.DOOR]:
            return True
        else:
            return False
    def bombable(self):
        return self.bomb == None and (self.type != self.c.WALL)