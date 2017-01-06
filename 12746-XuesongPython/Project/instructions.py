# instructions 
import pygame, configure

# base template is cited from 

class Instructions(object):
    """docstring for Instructions"""
    def __init__(self):
        self.c = configure.Configure
        # import images
        bgPath = self.c.IMAGE_PATH + "instructionsSingle.png"
        bgImage0 = pygame.image.load(bgPath).convert()
        bgPath = self.c.IMAGE_PATH + "instructionsMulti.png"
        bgImage1 = pygame.image.load(bgPath).convert()
        bgPath = self.c.IMAGE_PATH + "instructions2.png"
        bgImage2 = pygame.image.load(bgPath).convert()
        self.bgImageList = [bgImage0,bgImage1,bgImage2]
        # end of images

        self.mainloop()



    def mainloop(self):         
        # Define some colors
        BLACK = (0, 0, 0)
         
        pygame.init()
         
        # Set the width and height of the screen [width, height]
        size = (self.c.WIDTH, self.c.HEIGHT)
        self.screen = pygame.display.set_mode(size)
         
        pygame.display.set_caption("instructions")
        
        prevCor = [375, 620, (375+520)/2, 645]
        nextCor = [(375+520)/2+1, 620, 520, 645]
        backCor = [770, 620, 865, 655]

        # Loop until the user clicks the close button.
        self.done = False
        self.page = 0
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        
        # initial Draw Page
        self.drawBackground(0)
        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True
                elif event.type == pygame.MOUSEBUTTONDOWN:                    # get mouse position 
                    pos = pygame.mouse.get_pos()
                    x, y = pos[0], pos[1]

                    # click the previous button 

                    if (self.inBoundary(x,y,prevCor[0],prevCor[1], 
                                        prevCor[2],prevCor[3])):
                        self.page = (self.page + 1)%(len(self.bgImageList))
                        self.drawBackground(self.page)

                    # click the next button
                    elif (self.inBoundary(x,y,nextCor[0],nextCor[1], 
                                                nextCor[2],nextCor[3])):
                        self.page = (self.page - 1)%(len(self.bgImageList))
                        self.drawBackground(self.page)

                    # click the back button
                    elif (self.inBoundary(x,y,backCor[0],backCor[1], 
                                                backCor[2],backCor[3])):
                        self.done = True

            # --- Game logic should go here 
         
            # --- Drawing code should go here
         
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # --- Limit to 60 frames per second
            clock.tick(self.c.FPS)
         
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.



    def drawBackground(self,page):
        bgImage = self.bgImageList[page]
        self.screen.blit(bgImage,(0,0))

        # return true when x0 y0 in (x1,y1,x2,y2)
    def inBoundary(self,x0,y0,x1,y1,x2,y2):
        if ((x1 <= x0 <= x2) and (y1 <= y0 <= y2)):
            return True
        return False