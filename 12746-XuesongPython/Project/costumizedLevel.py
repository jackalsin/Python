# make self level
import pygame, configure, random, tiles, maps, pickle, game
BLACK = (0, 0, 0)
class CustomizedLevel(maps.Maps):
    """docstring for CustomizedLevel"""
    def __init__(self):
        # super().__init__()
        maps.Maps.__init__(self)
# the following template cited from 
# http://programarcadegames.com/
# index.php?chapter=introduction_to_graphics&lang=en#section_5
 
        # Initialize the game engine
        pygame.init()
        self.superBoard = maps.Maps()
        # Set the height and width of the screen
        size = (self.c.WIDTH, self.c.HEIGHT)
        self.screen = pygame.display.set_mode(size)
         
        pygame.display.set_caption("MapGenerators")
        
        bgPath = (self.c.IMAGE_PATH + "mapEditor.png")
        self.bgImage = pygame.image.load(bgPath).convert()
        
        self.runModifier()


    # main loop of pygame
    def runModifier(self):
        # Loop as long as done == False
        # Loop until the user clicks the close button.
        self.done = False
        clock = pygame.time.Clock()
        WIDTH = self.c.WIDTH
        self.rows = self.c.ROWS
        self.cols = self.c.COLS
        booleanDraw = True
        while not self.done:
                 
            for event in pygame.event.get():  # User did something
                if event.type == pygame.QUIT:  # If user clicked close
                    self.done = True  # Flag that we are done so we exit this loop
                
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse position 
                    bottomMenuWidth = self.c.RECT_MENU_WIDTH
                    rMenuStartX = self.c.RIGHT_MENU_STARTX 
                    pos = pygame.mouse.get_pos()
                    if self.isInMap(pos):
                        thisTile = self.superBoard.getTile(pos)
                        thisTile.type = (thisTile.type + 1) % 7

                    # rows +
                    elif self.inBounday(pos,0,600,bottomMenuWidth,self.c.HEIGHT):
                        self.rows = min(self.rows + 2, self.c.ROWS)
                        self.superBoard.rows = self.rows
                        self.reGenerate(self.rows, self.cols)

                    # row -
                    elif self.inBounday(pos,bottomMenuWidth,600,
                                            bottomMenuWidth*2,self.c.HEIGHT):
                        self.rows = max(self.rows - 2, 7)   
                        self.superBoard.rows = self.rows
                        self.reGenerate(self.rows, self.cols)

                    # cols +self.c.HEIGHT
                    elif self.inBounday(pos,bottomMenuWidth*2,600,
                                            bottomMenuWidth*3,self.c.HEIGHT):
                        self.cols = min(self.cols + 2, self.c.COLS)
                        self.superBoard.cols = self.cols
                        self.reGenerate(self.rows, self.cols)

                    # cols -
                    elif self.inBounday(pos,bottomMenuWidth*3,600,
                                            bottomMenuWidth*4,self.c.HEIGHT):
                        self.cols = max(self.cols - 2, 7)
                        self.superBoard.cols = self.cols
                        self.reGenerate(self.rows, self.cols)

                    # exit the program
                    elif self.inBounday(pos,rMenuStartX,600,
                                            self.c.WIDTH,self.c.HEIGHT):
                        self.done = True

                    # Save the map and play
                    elif self.inBounday(pos,rMenuStartX,1,WIDTH,110): # very trick
                        # do not use 0, use 1, so it won't 
                        pickle.dump(self.superBoard.map, 
                                                open("board.pickle", "wb"))
                        self.done = True

                self.redrawAll()         
             
                # --- Go ahead and update the screen with what we've drawn.
                pygame.display.flip()
             
                # --- Limit to 60 frames per second
                clock.tick(self.c.FPS)

    # return true when in the bonndary 
    def inBounday(self, pos,x1,y1,x2,y2):
        x,y = pos[0],pos[1]
        return (x1 <= x <= x2 and y1 <= y <= y2)

    def isInMap(self,pos):
        x,y = pos[0], pos[1]
        tSize = self.c.TILE_SIZE
        rows = len(self.superBoard.board)
        cols = len(self.superBoard.board[0])
        if ( (tSize <= x <= (cols - 1) * tSize) and 
                            (tSize <= y <= (rows - 1) * tSize) ):
            return True

    def redrawAll(self):
        self.screen.fill(self.c.BLACK)
        self.drawBg()
        self.drawBoard()

    def drawBg(self):
        self.screen.blit(self.bgImage,(0,0))

    def drawBoard(self):
        rows = len(self.superBoard.board)
        cols = len(self.superBoard.board[0])
        for row in range(rows):
            for col in range(cols):
                thisTile = self.superBoard.board[row][col]
                x = col * self.c.TILE_SIZE
                y = row * self.c.TILE_SIZE

                # reserve these lines so that the game can normally load
                imagePath = (self.c.IMAGE_PATH + "tiles/" + 
                                                str(thisTile.type) + ".png")
                image = pygame.image.load(imagePath)


                pos_rect = image.get_rect()
                pos = pos_rect.move((x,y))

                self.screen.blit(image,pos)


    def reGenerate(self, rows, cols):
        self.superBoard.generateMaps(rows,cols)
        self.superBoard.board = [] # map is digits, but board have tiles
        self.superBoard.initBoard()

