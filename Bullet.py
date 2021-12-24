import pygame
from BulletHandler import BulletHandler
#THIS CLASS IS PROBABLY ONLY USEFUL FOR SINGLE PLAYER, maybe for multiplayer it's best bullets are no a objecy
#nvm

class Bullet():
    def __init__(self,x,y,width,height,vel,color,moveType,handler = None):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        # self.sprite = sprite
        self.color = color
        self.moveType = moveType
        if handler != None:
            if type(handler) != BulletHandler:
                raise TypeError("Handler can only be a BulletHandler.")
            else:
                handler.append(self)

    

if __name__ == "__main__":
    bh1 = BulletHandler()
    b1 = Bullet(100,100,100,100,100,100,"-x",handler=bh1)
    print(bh1.bulletList[0].moveType)

        

    