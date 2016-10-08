# highScroes
import os, pygame, configure, pickle,copy


class OneScore(object):
    """docstring for oneScore"""
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return name + "\t" + str(score)

    def __eq__(self, other):
        return (isinstance(other, oneScore) and (self.score > other.score))

class HighScores(object):
    """docstring for highScroes"""
    def __init__(self):
        self.c = configure.Configure()
        self.allScore = []
        # testCode 
        # self.testSave()
        # testCode ends
        self.loadScores()

    def loadScores(self):
        # when the player first time plays, no such files
        try:
            with open("highscroes.pickle","rb") as f:
                self.allScore = pickle.load(f)
            print("loaded")
            f.close()
        except:
            pass
  
    def addScores(self, newScore):
        self.allScore.append(newScore)
        self.allScore.sort(key = lambda x: x.score)
        self.allScore.reverse()
        self.allScore = self.allScore[:6]

        with open("highscroes.pickle","wb") as f:
            pickle.dump(self.allScore, f)
        print("saved ") # testCode
        f.close()
    
    # the main function in the highScores
    def displayScores(self):
        """ the following template cited from 
            http://programarcadegames.com/python_examples/
            f.php?file=pygame_base_template.py
        """
        # Define some colors
        BLACK = (0, 0, 0)         
        pygame.init()
         
        # Set the width and height of the screen [width, height]
        size = (self.c.WIDTH, self.c.HEIGHT)
        self.screen = pygame.display.set_mode(size)
         
        pygame.display.set_caption("HighScores")
        
        self.drawBackground()
        # Loop until the user clicks the close button.
        self.done = False
         
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
         
        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.done = True

                if event.type == pygame.MOUSEBUTTONDOWN:
                    self.done = True
                    print("MOUSEBUTTONDOWN")

            # --- Game logic should go here
         
            # --- Drawing code should go here
            self.redrawAll()
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # --- Limit to 60 frames per second
            clock.tick(self.c.FPS)
         
        # Close the window and quit.

    def drawBackground(self):
        self.bgPath = self.c.IMAGE_PATH + "highScores.png"
        self.bgImage = pygame.image.load(self.bgPath).convert()
        self.screen.blit(self.bgImage,(0,0))

    def redrawAll(self):
        self.drawScore()

    def drawScore(self):
        # 170 + 39 
        # the bottom of the size 
        frLeft = 327
        frRight = 581
        frBot = 170
        dHeight = 39
        frTop = frBot - dHeight
        font = pygame.font.Font(None, 35)
        index = 1
        for obj in self.allScore:
            name = obj.name
            score = obj.score
            formatStr = " #%d %11s %9d" % (index, name, score)
            index += 1
            # this will get a new surface 
            line = font.render(formatStr, True, (0, 0, 0))
            # the following three lines are modified but cited from 
# http://nullege.com/codes/show/
# src%40w%40r%40writing_games_tutorial-HEAD%40examples%40example4%40example1.py/
# 221/pygame.font.Font.render/python
            lineRect = line.get_rect()
            lineRect.x = frLeft
            # index - 2 because index ++ 
            lineRect.y = (frTop + frBot)/2 + (index - 2) * dHeight
            self.screen.blit(line,lineRect)

    # testCode
    def testSave(self):
        score = 100
        for i in range(6):
            name = chr(ord('a') + i)
            score -= 10
            self.addScores(OneScore(name, score))

        # [90, 80, 70, 60, 50, 40]
