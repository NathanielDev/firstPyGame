import pygame
from Bullet import Bullet
from BulletHandler import BulletHandler
from Player import Player
import os
pygame.font.init()

WIDTH, HEIGHT = 1400, 700
WIN = pygame.display.set_mode((WIDTH, HEIGHT))


# COLORS:
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
# ----------------------

# EVENTS:
PLAYER_HIT_1 = pygame.USEREVENT + 1
PLAYER_HIT_2 = pygame.USEREVENT + 2
# PLAYER DEFAULT STATE:
BULLET_WIDTH = 10
BULLET_HEIGTH = 20
BULLET_VEL = 10
BULLET_COLOR_P1 = WHITE
BULLET_COLOR_P2 = RED
BULLET_MODE_P1 = "-y"
BULLET_MODE_P2 = "+y"
P1_INIIAL_X = 500
P1_INITIAL_Y = 500
P2_INIIAL_X = 500
P2_INITIAL_Y = 100


# BORDER CONSTANTS:
BORDER_WIDTH = WIDTH
BORDER_HEIGHT = 30
BORDER_X = 0
BORDER_Y = HEIGHT//2 + BORDER_HEIGHT//2

# FONTS:
FONT_ON_WIN = pygame.font.SysFont("impact", 200)


pygame.display.set_caption("bruh.py")

BG = pygame.transform.scale(pygame.image.load(
    os.path.join("Assets", "space.png")), (WIDTH, HEIGHT))

#SPACESHIP = pygame.transform.scale(pygame.image.load("Assets/spaceship.png"),(50,50))

# SETTINGS:
IS_LOCAL = False
DEBUG = False

FPS = 60

#bhandler1 = BulletHandler()
#bullet1 = Bullet(500,100,10,10,5,YELLOW,"+y",bhandler1)
# bhandler1.append(bullet) no longer needed since bullets self-append now
p1 = Player(P1_INIIAL_X, P1_INITIAL_Y, 50, 50, BULLET_WIDTH, BULLET_HEIGTH, BULLET_VEL,
            BULLET_COLOR_P1, BULLET_MODE_P1, os.path.join("Assets", "spaceship2.2.png"), True, IS_LOCAL)
p2 = Player(P2_INIIAL_X, P2_INITIAL_Y, 50, 50, BULLET_WIDTH, BULLET_HEIGTH, BULLET_VEL,
            BULLET_COLOR_P2, BULLET_MODE_P2, os.path.join("Assets", "spaceship.png"), False, IS_LOCAL)


def draw_window(border):
    WIN.blit(BG, (0, 0))
    pygame.draw.rect(WIN, WHITE, border)
    p1.draw(WIN, DEBUG)
    p2.draw(WIN, DEBUG)

    # bhandler1.handleBullets()
    # bhandler1.draw_all(WIN)
    p1.pbList.handleBullets()
    p2.pbList.handleBullets()
    p1.pbList.draw_all(WIN)
    p2.pbList.draw_all(WIN)

    pygame.display.update()


def on_win(text):
    win_text = FONT_ON_WIN.render(text, 1, RED)
    WIN.blit(win_text, (WIDTH//2 - win_text.get_width() /
             2, HEIGHT//2 - win_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)


def main():
    doonce = True
    clock = pygame.time.Clock()
    run = True
    border = pygame.Rect(BORDER_X, BORDER_Y, BORDER_WIDTH, BORDER_HEIGHT)
    while run:

        if DEBUG:
            print(p1.pbList.bulletList)
            print(p2.pbList.bulletList)
        clock.tick(FPS)
        for p2bullet in p2.pbList.bulletList:

            if p1.rect.colliderect(p2bullet):  # TODO make gameover screen
                pygame.event.post(pygame.event.Event(PLAYER_HIT_1))
        for p1bullet in p1.pbList.bulletList:
            if p2.rect.colliderect(p1bullet):
                pygame.event.post(pygame.event.Event(PLAYER_HIT_2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
            if event.type == PLAYER_HIT_1 and doonce:
                on_win("P2 WINS!!!!!!!!")
                run = False
            elif event.type == PLAYER_HIT_2 and doonce:
                on_win("P1 WINS!!!!!!!!")
                run = False

                # pygame.quit()

        p1.handle_movement()
        p2.handle_movement()

        draw_window(border)

    print("Restarting...")
    p1.pbList.bulletList.clear()
    p2.pbList.bulletList.clear()
    p1.rect.x = P1_INIIAL_X
    p1.rect.y = P1_INITIAL_Y

    p2.rect.x = P2_INIIAL_X
    p2.rect.y = P2_INITIAL_Y

    main()
    # pygame.quit()


if __name__ == "__main__":
    main()
