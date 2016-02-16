# player
import pygame, configure,character,bomb

# the difference betwween character and player :
    # the charactor are monster and players prototype
    # the player are the user and AI controls


class Player(character.Character):
    """docstring for Player"""

    def __init__(self,id,position,type):
        self.c = configure.Configure()
        self.id = id
        super().__init__(self.id,position,type)
        self.lives = 3
        self.maxBombs = 3
        self.curBombs = 3
        self.speed = 1
        self.power = 3
        self.reborn = 3
        self.scores = 0
        self.draw = True

    def getPower(self,powerType):
        print("we get power ", powerType)
        if powerType == self.c.POWER_UP:
            self.power += 1
        elif powerType == self.c.BOMB_UP:
            print("we are adding maxBombs",self.maxBombs)
            self.maxBombs += 1
            self.curBombs = self.maxBombs
            
        elif powerType == self.c.LIFE_UP:
            self.lives += 1

    def deployBomb(self):
        if self.curBombs > 0:
            self.curBombs -= 1
            return bomb.Bomb(self) # pass player in
        return None

    def kill(self):
        self.lives -= 1
        self.reset()
        self.scores -= 1000
        return self.lives <= 0

    def reset(self):
        self.reborn = 3
        self.curBombs = 3
        self.maxBombs = 3
        self.speed = 3
        self.power = 3

