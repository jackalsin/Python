# bomb
import configure, pygame
    

class Bomb(pygame.sprite.Sprite):
    
    def __init__(self,player):
        pygame.init()
        pygame.sprite.Sprite.__init__(self)
        self.c = configure.Configure()
        imagePath = self.c.IMAGE_PATH + "/bomb.png"
        self.image = pygame.image.load(imagePath).convert()
        self.range = player.power # kill zone
        self.triggered = False
        self.countDown = 3 # how many seconds
        self.owner = player
        self.position = self.image.get_rect()
        self.position = self.position.move((player.position.x,player.position.y))

        tsize = self.c.TILE_SIZE
        self.rect = pygame.Rect(self.position[0],self.position[1],tsize,tsize)


    def countdown(self):
        self.countDown -= 1

    def explode(self):
        self.owner.curBombs += 1
        # shall i add animation here
