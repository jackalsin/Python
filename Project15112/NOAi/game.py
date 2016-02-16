# real Game
# this is the Main Game class

import pygame,random,configure,maps,player,bomb,enemy,fire,copy, highscore
import os, pickle, string

BLACK = (0,0,0)
WHITE = (255, 255, 255)


class Game(object):
    """docstring for Game"""
    # define const
    # saved: true load last game 
    # modified: true load last map
    def __init__(self, mode,saved = None, modified = False):
        self.c = configure.Configure()
        self.mode = mode
        pygame.display.init()
        # self.modified = modified
        self.modified = modified
    
        # Call this function so the Pygame library can initialize itself
        pygame.init()
        self.user =[None,None]
        # Create an 800x600 sized screen
        self.screen = pygame.display.set_mode([self.c.WIDTH, self.c.HEIGHT])
        # This sets the name of the window
        pygame.display.set_caption("Bomberman")
        self.gameStatues = None
                 
        done = False
        # not loading the saved game
        if saved == None:
            self.players = pygame.sprite.Group()
            self.enemyGroup = pygame.sprite.Group()
            self.bombsGroup = pygame.sprite.Group()
            self.powerGroup = pygame.sprite.Group()
            self.fireGroup = pygame.sprite.Group()

            # import board
            if self.modified == False:
                # didn't customize the map
                self.superBoard = maps.Maps()
            else:
                # customize the map
                self.superBoard = maps.Maps()
                importBoard = pickle.load(open("board.pickle", "rb"))
                self.superBoard.map = copy.deepcopy(importBoard)
                self.superBoard.rows = len(self.superBoard.map)
                self.superBoard.cols = len(self.superBoard.map[0])
                self.superBoard.board = []
                self.superBoard.initBoard()

            self.initGame()
        else:
            self.players = pygame.sprite.Group()
            self.enemyGroup = pygame.sprite.Group()
            self.bombsGroup = pygame.sprite.Group()
            self.powerGroup = pygame.sprite.Group()
            self.fireGroup = pygame.sprite.Group()
            
            self.superBoard = saved[0]
            self.drawBoard()

            self.players = saved[1]
            i = 0
            for p in self.players:
                self.user[i] = p
                self.user[i].getImage(self.user[i].direction)
                i += 1

            self.enemyGroup = saved[2]
            for e in self.enemyGroup:
                e.getImage(e.direction)

            self.bombsGroup = saved[3]
            self.powerGroup = saved[4]
            self.fireGroup = saved[5]
            self.runGame()
        

        
    def drawBoard(self):
        rows = len(self.superBoard.board)
        cols = len(self.superBoard.board[0])
        for row in range(rows):
            for col in range(cols):
                thisTile = self.superBoard.board[row][col]
                x = col * self.c.TILE_SIZE
                y = row * self.c.TILE_SIZE
                imagePath = thisTile.path
                image = pygame.image.load(imagePath)


                pos_rect = image.get_rect()
                pos = pos_rect.move((x,y))

                self.screen.blit(image,pos)

    def initGame(self):
        self.drawBoard()

        self.initPlayers()

        self.initEnemies()

        self.runGame()


    def playSound(self,musicEvent):
        if musicEvent == self.c.BIGBOSS:
            subPath = self.c.M_BIGBOSS
        elif musicEvent == self.c.BLAST:
            subPath = self.c.M_BLAST
        elif musicEvent == self.c.PING:
            subPath = self.c.M_PING

        pygame.mixer.music.load(self.c.AUDIO_PATH + subPath)
        pygame.mixer.music.play()

    def initPlayers(self):
        player1BirthCor = (40,40)
        player2BirthCor = (680,40)
        if self.mode == self.c.SINGLE:
            self.user[0] = player.Player(1,player1BirthCor,"players")
            self.players.add(self.user[0])
        elif self.mode == self.c.MULTI:
                self.user[0] = player.Player(1,player1BirthCor,"players")
                self.user[1] = player.Player(2,player2BirthCor,"players")
                self.players.add(self.user[0])
                self.players.add(self.user[1])

    def initEnemies(self):
        MaxEnemies = random.randint(self.c.MAX_ENEMY_SPRITES - 2,
                                                    self.c.MAX_ENEMY_SPRITES)
        cols = self.superBoard.cols
        rows = self.superBoard.rows
        for i in range(MaxEnemies):
            x = random.randint(3, cols-2) * self.c.TILE_SIZE
            y = random.randint(3, rows-2) * self.c.TILE_SIZE
            # cordinates

            if self.superBoard.getTile((x,y)).passable:
                idNum = random.randint(1,9) # to generate enemy type
                Aenemy = enemy.Enemy(idNum,(x,y),"enemies") 
                self.enemyGroup.add(Aenemy)


    def runGame(self):
        pygame.init()         
        # Loop until the user clicks the close button.
        self.done = False
        self.end = False # label for second loops     
        # Used to manage how fast the screen updates
        clock = pygame.time.Clock()
        # define event
        BOMB_LABLE = pygame.USEREVENT
        ENEMY_LABLE = pygame.USEREVENT + 1
        CHECK_COLLISION = pygame.USEREVENT + 2
        FLAME_COUNTDOWN = pygame.USEREVENT + 3

        pygame.time.set_timer(BOMB_LABLE,1000) # every second trigged once
        pygame.time.set_timer(ENEMY_LABLE,500) # for enemy moving 
        pygame.time.set_timer(CHECK_COLLISION,1000)
        pygame.time.set_timer(FLAME_COUNTDOWN, 1000)

        # -------- Main Program Loop -----------
        while not self.done:
            # --- Main event loop
            for event in pygame.event.get():
            
                if event.type == pygame.QUIT:
                    self.done = True
                    self.end = True
                elif event.type == pygame.KEYDOWN:
                    k = event.key
                    # player 1 controls 
                    if self.mode == self.c.SINGLE:
                        if k == pygame.K_SPACE:
                            self.deployBomb(self.user[0])
                            # add score by deploying bombs
                            self.user[0].scores += 100

                        elif (k == pygame.K_UP or k == pygame.K_DOWN or 
                                    k == pygame.K_LEFT or k == pygame.K_RIGHT):
                            # change it to std mode:
                            squareOffset = self.user[0].moveSquare(k) 
                            # [above]in Char, return a tuple
                            self.moveCheck(self.user[0], squareOffset) 
                            # [above] input is x y cordination
                        
                    # player 2 controls
                    if self.mode == self.c.MULTI:
                        if k == pygame.K_LCTRL:
                            self.deployBomb(self.user[0])
                            # add score by deploying bombs
                            self.user[0].scores += 100

                        elif (k == pygame.K_w or k == pygame.K_a or 
                                    k == pygame.K_s or k == pygame.K_d):
                            # change it to std mode:
                            if (k == pygame.K_w):
                                k = pygame.K_UP
                            elif (k == pygame.K_a):
                                k = pygame.K_LEFT
                            elif (k == pygame.K_s):
                                k = pygame.K_DOWN
                            elif (k == pygame.K_d):
                                k = pygame.K_RIGHT
                            squareOffset = self.user[0].moveSquare(k) 
                            # [above]in Char, return a tuple
                            self.moveCheck(self.user[0], squareOffset) 
                            # [above] input is x y cordination

                        elif (k == pygame.K_RALT):
                            # player 2 deploy a bomb 
                            self.deployBomb(self.user[1])
                            # add score by deploying bombs
                            self.user[1].scores += 100
                        elif (k == pygame.K_UP or k == pygame.K_DOWN or 
                                    k == pygame.K_LEFT or k == pygame.K_RIGHT):
                            squareOffset = self.user[1].moveSquare(k) 
                            # [above]in Char, return a tuple
                            self.moveCheck(self.user[1], squareOffset) 
                            # [above] input is x y cordination


                # customized event 
                elif event.type == ENEMY_LABLE:
                    # enemies moves
                    for e in self.enemyGroup:
                        self.moveCheck(e,e.movement())
                # count down the bomb in 3 seconds
                elif event.type == BOMB_LABLE:
                    self.bombCountDown()

                # when player dies he becomes in god mode for 3 seconds
                elif event.type == CHECK_COLLISION:
                    for u in self.user:
                        if (u != None and u.reborn > 0):
                            u.reborn -= 1

                elif event.type == FLAME_COUNTDOWN:
                    for f in self.fireGroup:
                        if f.fire():
                            self.fireGroup.remove(f)

                # for users interact with menu
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    # get mouse position 
                    pos = pygame.mouse.get_pos()
                    rMenuStartX = self.c.RIGHT_MENU_STARTX
                    rMenuHeight = self.c.RIGHT_MENU_HEIGHT
                    # Save the game 
                    if self.inBoundary(pos[0],pos[1],rMenuStartX, 1, 
                                                    self.c.WIDTH, rMenuHeight):
                        self.total = [self.superBoard,self.players,
                            self.enemyGroup, self.bombsGroup,self.powerGroup,
                                    self.fireGroup]
                        with open("saved.pickle","wb") as f:
                            pickle.dump(self.total,f)
                        f.close()

                    # load the game
                    elif self.inBoundary(pos[0],pos[1],rMenuStartX, rMenuHeight, 
                                                self.c.WIDTH,2 * rMenuHeight):
                        with open("saved.pickle","rb") as f:
                            self.total = pickle.load(f)
                        f.close()
                        self.__init__(self.c.SINGLE,self.total)

                    # load Map
                    elif self.inBoundary(pos[0],pos[1],rMenuStartX, 
                                3*rMenuHeight+1, self.c.WIDTH,4 * rMenuHeight):
                        self.__init__(self.mode, None, True)

                    # Exit
                    elif self.inBoundary(pos[0],pos[1],rMenuStartX, 
                                self.c.RECT_MENU_STARTY, self.c.WIDTH, 
                                                        self.c.HEIGHT):

                        self.done = not self.done

            self.update()

            self.redrawAll(self.screen)
         
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            
         
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # --- Limit to 60 frames per second
            clock.tick(self.c.FPS)
         
        # Close the window and quit.
        # If you forget this line, the program will 'hang'
        # on exit if running from IDLE.

        
        # -------- Main Program Loop -----------
        while not self.end:
            # --- Main event loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.end = True
                elif event.type == pygame.KEYDOWN:
                    self.end = True
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    self.end = True
            # --- Game logic should go here
         
            # --- Drawing code should go here
         
            # First, clear the screen to white. Don't put other drawing commands
            # above this, or they will be erased with this command.
            self.screen.fill((0,0,0))
            self.drawEnding()
            # --- Go ahead and update the screen with what we've drawn.
            pygame.display.flip()
         
            # --- Limit to 60 frames per second
            clock.tick(self.c.FPS)




    def drawEnding(self):
        gs = self.gameStatues
        if gs == self.c.SINGLE_WIN:
            self.drawSingleWin()
        elif gs == self.c.SINGLE_LOSE:
            self.drawSingleLose()
        elif gs == self.c.MULTI_PLAYER_1_WIN:
            self.drawMultiWin(1) # player 1 win
        elif gs == self.c.MULTI_PLAYER_2_WIN:
            self.drawMultiWin(2)
        elif gs == None:
            self.end = True

    def drawSingleWin(self):
        winPagePath = self.c.IMAGE_PATH + "singleWin.png"
        winImage = pygame.image.load(winPagePath).convert()
        self.screen.blit(winImage,(0,0))
        self.askName()

    # to implement a dialog
    def askName(self):
        # partly modified from http://www.pygame.org/pcr/inputbox/
        get_str = []
        self.display_box(self.screen, "".join(get_str))
        maxChar = 11
        while 1:
            inkey = self.get_key()
            if inkey == pygame.K_BACKSPACE:
                get_str = get_str[0:-1]
            # get the full name
            elif inkey == pygame.K_RETURN:
                name = "".join(get_str)
                score = self.user[0].scores
                self.end = True
                self.saveScore(name, score)
                break
            elif inkey == pygame.K_MINUS:
                get_str.append("_")
            elif inkey <= 127:
                get_str.append(chr(inkey))

            if len(get_str) > maxChar:
                get_str = copy.copy(get_str[0:maxChar])
            self.display_box(self.screen, "".join(get_str))

        return "".join(get_str)
        
    def get_key(self):
        while 1:
            event = pygame.event.poll()
            if event.type == pygame.KEYDOWN:
              return event.key
            else:
              pass

    def display_box(self, screen, message):
        nameObj = pygame.font.SysFont("Calibri",30)
        innerBoxRect = (357,330,168,34)
        pygame.draw.rect(screen, WHITE, innerBoxRect, 0)
        if len(message) != 0:
            self.screen.blit(nameObj.render(message, 1, BLACK),
                (innerBoxRect[0], innerBoxRect[1]))

        pygame.display.flip()


    def saveScore(self, name, score):
        newScore = highscore.OneScore(name,score)
        hs = highscore.HighScores()
        hs.addScores(newScore)
        hs.displayScores()
        

    def drawSingleLose(self):
        losePagePath = self.c.IMAGE_PATH + "singleLose.png"
        loseImage = pygame.image.load(losePagePath).convert()
        self.screen.blit(loseImage,(0,0))

    def drawMultiWin(self, winner):
        if winner == 1:
            imagePath = self.c.IMAGE_PATH + "player1Win.png"
        else:
            imagePath = self.c.IMAGE_PATH + "player2Win.png"

        image = pygame.image.load(imagePath).convert()
        self.screen.blit(image,(0,0)) 

    def moveCheck(self, player, position):
        # next point is the point to move, but nothing happens so far
        # position like (0,-40)

        nextPoint = player.position.move(position)
        nextTile = self.superBoard.getTile(nextPoint)

        if nextTile.passableTotal():
            if player.type == "players" and nextTile.hasPower():
                player.getPower(nextTile.type)
                nextTile.destroy()

            player.move(position) ## consider it !!!!!!!!!!!!!!!!!!!!

    def redrawAll(self, screen):
        # player should be drawn the last, so bomb won't be overlayed
        self.drawInterface()
        self.drawBoard()
        self.enemyGroup.draw(screen)
        self.bombsGroup.draw(screen)
        self.bombUpdate()
        self.players.draw(screen)
        self.fireGroup.draw(screen)
        self.drawPlayerStatus(screen)

    def drawPlayerStatus(self,screen):
        player1_bombPos = (245, 610)
        player1_power = (245, 650)
        player1_life = (310, 610)
        player1_score = (280, 650)

        player2_bombPos = (240+191*2, 610)
        player2_power = (240+191*2, 650)
        player2_life = (305+191*2, 610)
        player2_score = (275+191*2, 650)

        self.subDrawSinglePlayerStatus(self.user[0],
                player1_bombPos, player1_power, player1_life, player1_score)
        if self.mode == self.c.MULTI:
            self.subDrawSinglePlayerStatus(self.user[1], player2_bombPos, 
                                player2_power, player2_life, player2_score) 

        # input positions are tuples 
    def subDrawSinglePlayerStatus(self, player, bombPos, powerPos, 
                                                    lifePos, scorePos):
        pMaxbombs = player.maxBombs
        pPower = player.power
        pLife = player.lives
        pScore = player.scores

        font = pygame.font.SysFont('Calibri', 35)
        contextList = [pMaxbombs, pPower, pLife, pScore]
        posList = [bombPos, powerPos, lifePos, scorePos]
        # draw player's life power and bombs
        for i in range(len(posList)):
            if i == 3:
                formatStr = " %7d" % (contextList[i])
            else:
                formatStr = " %3d" % (contextList[i])
            # this will get a new surface 
            line = font.render(formatStr, True, WHITE)
            # the following three lines are modified but cited from 
# http://nullege.com/codes/show/
# src%40w%40r%40writing_games_tutorial-HEAD%40examples%40example4%40example1.py/
# 221/pygame.font.Font.render/python
            lineRect = line.get_rect()
            lineRect.x = posList[i][0]
            lineRect.y = posList[i][1]
            self.screen.blit(line,lineRect)

    def drawInterface(self):
        if self.mode == self.c.SINGLE:
            bgName = "GameMenuSingle.png"
        elif self.mode == self.c.MULTI:
            bgName = "GameMenuMulti.png"
        self.menuImagePath = self.c.IMAGE_PATH + bgName
        image = pygame.image.load(self.menuImagePath).convert()
        pos_rect = image.get_rect()
        pos = pos_rect.move((0,0))
        self.screen.blit(image,pos)

    def update(self):
        self.checkEnemyVSplayer()
        self.checkWin()

    def checkWin(self):
        if self.mode == self.c.SINGLE:
            for player in self.players:
                if player.lives < 0:
                    self.gameStatues = self.c.SINGLE_LOSE
                    self.done = not self.done
            # enemy all die win
            i = 0   
            for e in self.enemyGroup:
                i += 1
                break
            if i == 0:
                self.gameStatues = self.c.SINGLE_WIN
                self.done = not self.done

        elif self.mode == self.c.MULTI:
            for player in self.players:
                if player.lives < 0:
                    if player.id == 1:
                        self.gameStatues = self.c.MULTI_PLAYER_2_WIN
                    else:
                        self.gameStatues = self.c.MULTI_PLAYER_1_WIN
                    self.done = not self.done



    # player runs into enemies
    def checkEnemyVSplayer(self):
        for u in self.user:
            if (u != None and u.reborn == 0 and 
                    pygame.sprite.groupcollide(self.players,self.enemyGroup,
                                                            False,False)):
                u.kill() # deduct 100
                self.playSound(self.c.PING)
                
    def checkBombKill(self, position):
        for player in self.players:
            if (player.reborn == 0 and player.position == position):
                player.kill()

        for e in self.enemyGroup:
            if e.position == position:
                self.enemyGroup.remove(e)
                # kill enemy + 1000
                return True

    def deployBomb(self,user):
        curTile = self.superBoard.getTile(user.position)
        if user.curBombs > 0 and curTile.bomb == None: # to check if bombable
             curBomb = user.deployBomb() # generate a bomb, no position is right
             curTile.bomb = curBomb
             self.bombsGroup.add(curBomb)

    def bombCountDown(self):
        for b in self.bombsGroup:
            b.countdown()

    def bombUpdate(self): # put into draw Function 
        for b in self.bombsGroup:
            if b.countDown == 0:
                self.triggerBombsGroup(b)
                self.playSound(self.c.BLAST)

    def triggerBombsGroup(self,bomb):
        bomb.explode()
        self.playFireWork(bomb)
        # play the firework
        curTile = self.superBoard.getTile(bomb.position)
        curTile.bomb = None
        curTile.destroy()

        self.bombsGroup.remove(bomb)

    def playFireWork(self,bomb):
        self.bombFireInDirection(bomb,"left")
        self.bombFireInDirection(bomb,"right")
        self.bombFireInDirection(bomb,"up")
        self.bombFireInDirection(bomb,"down")

    def bombFireInDirection(self,bomb,direction):
        tSize = self.c.TILE_SIZE
        fireImagePath = self.c.IMAGE_PATH + "explosion_c.png"
        fireImage = pygame.image.load(fireImagePath)

        if direction == 'right':
            offset = (tSize,0)
        elif direction == 'left':
            offset = (-tSize,0)
        elif direction == 'up':
            offset = (0,-tSize)
        elif direction == 'down':
            offset = (0,tSize)

        # consider range, passable, 
        x,y = 0, 0
        while True:
            # x,y += offset
            x += offset[0]
            y += offset[1]
            nextPoint = bomb.position.move((x,y))
            curTile = self.superBoard.getTile(nextPoint)
            if curTile.bombable(): # throw fire
                curTile.destroy()

                # self.screen.blit(fireImage,nextPoint)
                confirmKill = self.checkBombKill(nextPoint)
                if confirmKill:
                    bomb.owner.scores += 1000
                flame = fire.Fire(nextPoint)
                self.fireGroup.add(flame)
            else:
                break
            # range control
            if (abs(x)//40 == bomb.range or abs(y)// 40 == bomb.range):
                break

    # return true when x0 y0 in (x1,y1,x2,y2)
    def inBoundary(self,x0,y0,x1,y1,x2,y2):
        if ((x1 <= x0 <= x2) and (y1 <= y0 <= y2)):
            return True
        return False