# The Game Menu


import pygame, configure, instructions, game, pickle, maps, costumizedLevel
import highscore

# constant
PTS_WIDTH = 1024  # pre screen width
PTS_HEIGHT = 768  # pre Screen height


class TitleScreen(object):
    def __init__(self):
        self.c = configure.Configure()
        done = False
        pygame.init()
        clock = pygame.time.Clock()
        self.modifyMap = False
        wantToEnd = False
        while not done:
            self.screen = pygame.display.set_mode([PTS_WIDTH, PTS_HEIGHT])
            pygame.display.set_caption("Bomberman")

            # import background image
            bgImagePath = self.c.IMAGE_PATH + "titleScreen.png"
            bgImage = pygame.image.load(bgImagePath).convert()
            bgImage = pygame.transform.scale(bgImage, (PTS_WIDTH, PTS_HEIGHT))
            self.screen.blit(bgImage, [0, 0])

            pygame.mixer.music.load(self.c.AUDIO_PATH + "title.mid")
            pygame.mixer.music.play()

            notValidOp = False
            # under valid control mode
            while not notValidOp:
                # get mouse position
                pos = pygame.mouse.get_pos()
                # testCode
                for event in pygame.event.get():
                    # deal with the exit
                    if event.type == pygame.QUIT:
                        notValidOp = not notValidOp
                        done = not done
                        wantToEnd = True

                    # load the game
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_l:
                            with open("saved.pickle", "rb") as f:
                                self.total = pickle.load(f)
                            f.close()
                            self.playGame(self.c.SINGLE, self.total)

                    elif event.type == pygame.MOUSEBUTTONDOWN:
                        # map editor
                        if self.inBoundary(pos[0], pos[1], 25, 450, 250, 500):
                            # customize the map
                            costumizedLevel.CustomizedLevel()
                            # the following code are necessary for python3
                            notValidOp = not notValidOp
                            # it should work like above, when finished one op
                            # it should jump the loop so the video and music
                            # can be reinitialized again.
                        # single
                        elif self.inBoundary(pos[0], pos[1], 25, 500, 250, 550):
                            pygame.mixer.music.fadeout(1000)
                            self.playGame(self.c.SINGLE, None)
                            # following code are necessary for python 3
                            notValidOp = not notValidOp

                        # multi
                        elif self.inBoundary(pos[0], pos[1], 25, 550, 250, 600):
                            pygame.mixer.music.fadeout(1000)
                            self.playGame(self.c.MULTI, None)
                            # the following code are necessary for python3
                            notValidOp = not notValidOp

                        # instructions
                        elif self.inBoundary(pos[0], pos[1], 25, 600, 250, 650):
                            self.instructions()

                            notValidOp = not notValidOp
                            # it should work like above, when finished one op
                            # it should jump the loop so the video and music
                            # can be reinitialzed again.

                        # high Score
                        elif self.inBoundary(pos[0], pos[1], 25, 650, 250, 700):
                            self.highScores()

                            notValidOp = not notValidOp
                            # it should work like above, when finished one op
                            # it should jump the loop so the video and music
                            # can be reinitialzed again.

                        # exit
                        elif self.inBoundary(pos[0], pos[1], 40, 700, 250, 750):
                            done = not done
                            notValidOp = not notValidOp
                            # wantToEnd = True

                # Go ahead and update the screen with what we've drawn.

                pygame.display.flip()

                # Limit to 60 frames per second
                clock.tick(self.c.FPS)

        pygame.quit()

    def inBoundary(self, x0, y0, x1, y1, x2, y2):
        if (x1 <= x0 <= x2) and (y1 <= y0 <= y2):
            return True
        return False

    def instructions(self):
        instructions.Instructions()

    def playGame(self, mode, saved):
        game.Game(mode, saved)

    def highScores(self):
        hs = highscore.HighScores()
        hs.displayScores()
