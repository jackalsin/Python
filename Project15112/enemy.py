# enemy
import pygame, character,random
class Enemy(character.Character):
    """docstring for Enemy"""
    def __init__(self, idNum,position,thisType):
        super().__init__(idNum,position,thisType)
        # imagePath = self.c.IMAGE_PATH + "enemies/" +"e_"+str(self.id)+"_" + direction + ".png"
        # self.image = pygame.image.load(imagePath).convert()


    def movement(self):
        patterns = [pygame.K_UP,pygame.K_DOWN,pygame.K_LEFT,pygame.K_RIGHT]

        # this move pattern can be improved
        return self.moveSquare(random.choice(patterns))
