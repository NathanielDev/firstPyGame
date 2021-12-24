import pygame
from Bullet import Bullet
from BulletHandler import BulletHandler
from Player import Player
import os
pygame.font.init()

WIDTH, HEIGHT = 1400, 700
WIN = pygame.display.set_mode((WIDTH,HEIGHT))


#COLORS:
WHITE = (255,255,255)
YELLOW = (255,255,0)
#----------------------

#EVENTS:
#TODO: raise player hit event upon collision with bullet.
PLAYER_HIT = pygame.USEREVENT + 1

#PLAYER DEFAULT STATE:
BULLET_WIDTH = 10
BULLET_HEIGTH = 20
BULLET_VEL = 10
BULLET_COLOR = WHITE
BULLET_MODE_P1 = "-y"
BULLET_MODE_P2 = "+y"

#BORDER CONSTANTS:
BORDER_WIDTH = WIDTH
BORDER_HEIGHT = 30
BORDER_X = 0
BORDER_Y = HEIGHT//2 + BORDER_HEIGHT//2





pygame.display.set_caption("bruh.py")

BG = pygame.transform.scale(pygame.image.load(os.path.join("Assets","space.png")),(WIDTH,HEIGHT))

#SPACESHIP = pygame.transform.scale(pygame.image.load("Assets/spaceship.png"),(50,50))


DEBUG = False

FPS = 60

bhandler1 = BulletHandler()
bullet1 = Bullet(500,100,10,10,5,YELLOW,"+y",bhandler1)
#bhandler1.append(bullet) no longer needed since bullets self-append now
p1 = Player(500,500,50,50,BULLET_WIDTH,BULLET_HEIGTH,BULLET_VEL,BULLET_COLOR,BULLET_MODE_P1,os.path.join("Assets","spaceship2.2.png"),True)
p2 = Player(500,100,50,50,BULLET_WIDTH,BULLET_HEIGTH,BULLET_VEL,BULLET_COLOR,BULLET_MODE_P2,os.path.join("Assets","spaceship.png"),False)


def draw_window(border):
    WIN.blit(BG,(0,0))
    pygame.draw.rect(WIN,WHITE,border)
    p1.draw(WIN,DEBUG)
    p2.draw(WIN,DEBUG)
    
    bhandler1.handleBullets()
    bhandler1.draw_all(WIN)
    p1.pbList.handleBullets()
    p2.pbList.handleBullets()
    p1.pbList.draw_all(WIN)
    p2.pbList.draw_all(WIN)

    pygame.display.update()



def main():
    clock = pygame.time.Clock()
    run = True
    border = pygame.Rect(BORDER_X,BORDER_Y,BORDER_WIDTH,BORDER_HEIGHT)
    while run:
        print(p1.pbList.bulletList)
        print(p2.pbList.bulletList)
        clock.tick(FPS)
        if p1.rect.colliderect(bullet1):#TODO make gameover screen
            pygame.event.post(pygame.event.Event(PLAYER_HIT))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                
        
                run = False
            if event.type == PLAYER_HIT:
                
                pygame.quit()

        p1.handle_movement()
        p2.handle_movement()

        draw_window(border)


        


    pygame.quit()


if __name__ == "__main__":
    main()