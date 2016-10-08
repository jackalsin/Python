# character
# the template here also been partly cited from Lucas
# https://github.com/LBPeraza/Pygame-Asteroids

import pygame, configure,copy


class Character(pygame.sprite.Sprite):
    """docstring for Character"""
    def __init__(self,idNum,position,thisType):
        self.c = configure.Configure() # some constant 
        # pygame.sprite.Sprite.__init__(self)
        super(Character,self).__init__()
        pygame.init()
        self.id = idNum

        self.type = thisType # players/ enemies
        # test Code 

        size = (self.c.WIDTH, self.c.HEIGHT)
        self.screen = pygame.display.set_mode(size)



        # testCode ends\
        self.getImage("down")
        # self.direction = "down"

        self.rect = self.image.get_rect()
        self.position = self.image.get_rect()
        self.move(position)

    def getImage(self,direction):
        self.direction = direction
        if self.type == "players":
            imagePath = self.c.IMAGE_PATH + "players/" +"p_"+str(self.id)+"_" + direction + ".png"
        else:
            imagePath = self.c.IMAGE_PATH + "enemies/" +"e_"+str(self.id)+"_" + direction + ".png"

        self.image = pygame.image.load(imagePath).convert()
        
        # maybe test code

        # self.screen.blit(self.image.convert(),[0,0])

        # solve the face to 
    def face(self,key):
        self.getImage(key)

    def moveSquare(self,key):
        if key == pygame.K_RIGHT:
            self.face("right")
            return (1*self.c.TILE_SIZE, 0)
        elif key == pygame.K_LEFT:
            self.face("left")
            return (-1*self.c.TILE_SIZE, 0)
        elif key == pygame.K_UP:
            self.face("up")
            return (0, -1*self.c.TILE_SIZE)
        elif key == pygame.K_DOWN:
            self.face("down")
            return (0, 1 * self.c.TILE_SIZE)


    def move(self,point):
        self.old = copy.copy(self.rect) 
        # self.position = self.position.move(point)

        dx,dy = point[0],point[1]
        self.rect.x,self.rect.y = self.rect.x + dx,self.rect.y+dy
        self.position = self.position.move(point)



    def updateRect(self):
        tSize = self.c.TILE_SIZE


    def update(self):
        self.updateRect()

# --------- test code ------------- #
    def testRun(self):
        pygame.init()
        size = (700, 500)
        screen = pygame.display.set_mode(size)

        user = Character(1,(40,40),"players")
        self.userGroup = pygame.sprite.Group(user)
        # self.userGroup.add(self.user)

        # self.screen.blit(self.image.convert(),[0,0])
        pygame.display.set_caption("My Test")
         
        # Loop until the user clicks the close button.
        done = False
         
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
         
        # -------- Main Program Loop -----------
        while not done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                elif event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_LEFT,pygame.K_RIGHT,pygame.K_UP,pygame.K_DOWN]:
                        point = user.moveSquare(event.key)
                        user.move(point)

                        # self.userGroup.update()

            screen.fill((255,255,255))
            # self.userGroup.update()
            self.userGroup.draw(screen)
            # --- Game logic should go here
         
            # --- Drawing code should go here
         
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.

            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # --- Limit to 60 frames per second
            clock.tick(30)
         
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.
        pygame.quit()

# Character(1,(40,40),"players").testRun() # born at left top corner