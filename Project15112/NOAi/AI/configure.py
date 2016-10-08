class Configure(object):
# partly cited from package onwer 
    GROUND = 0
    WALL = 1
    BRICK = 2
    BOMB_UP = 3 # deal with in player
    POWER_UP = 4 # deal with in player
    LIFE_UP = 5 # deal with in player
    TIME_UP = 6
    DOOR = 7
    FPS = 60
    WIDTH = 880
    HEIGHT = 690
    COLS = 19 # must be odd !!!
    ROWS = 15 # must be odd !!!!!!
    TILE_SIZE = 40
    IMAGE_PATH = "resources/images/"
    AUDIO_PATH = "resources/sounds/"
    FONT_PATH = "resources/font/"
    HIGHSCORES_PATH = "resources/highscores.txt"
    SINGLE = 'Single'
    MULTI = 'Multi'
    MAX_ENEMY_SPRITES = 12
    BLACK = (0, 0, 0)
    # the bottom menu width
    RECT_MENU_WIDTH = 191
    RECT_MENU_STARTY = 600

    RIGHT_MENU_STARTX = 760
    RIGHT_MENU_HEIGHT = 120

    # win lose statues
    SINGLE_WIN = 1
    SINGLE_LOSE = 2

    MULTI_PLAYER_1_WIN = 3
    MULTI_PLAYER_2_WIN = 4

    # music Event
    BIGBOSS = 1
    BLAST = 2
    PING = 3
    M_BIGBOSS = "bigboss.mid"
    M_BLAST = "Blast_01.wav"
    M_PING = "Ping_01.ogg"