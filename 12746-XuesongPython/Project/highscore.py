# The High Scores Class
# To document all the previous created scores.
import os, pygame, configure, pickle


class OneScore(object):
    """
        This class represents one player's score
    """

    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __repr__(self):
        return self.name + "\t" + str(self.score)

    def __eq__(self, other):
        return isinstance(other, OneScore) and (self.score > other.score)


class HighScores(object):
    """
        This represents the score board.
    """

    def __init__(self):
        self.c = configure.Configure()
        self.allScore = []
        self.loadScores()

    def loadScores(self):
        # when the player first time plays, no such files
        try:
            with open("highscroes.pickle", "rb") as f:
                self.allScore = pickle.load(f)
            f.close()
        except:
            pass

    def addScores(self, newScore):
        self.allScore.append(newScore)
        self.allScore.sort(key=lambda x: x.score)
        self.allScore.reverse()
        self.allScore = self.allScore[:6]

        with open("highscroes.pickle", "wb") as f:
            pickle.dump(self.allScore, f)
        f.close()

    # the main function in the highScores
    def displayScores(self):
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
        self.screen.blit(self.bgImage, (0, 0))

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
            lineRect = line.get_rect()
            lineRect.x = frLeft
            # index - 2 because index ++
            lineRect.y = (frTop + frBot) / 2 + (index - 2) * dHeight
            self.screen.blit(line, lineRect)


