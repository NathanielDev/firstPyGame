import pygame
from Bullet import Bullet
#maybe a bullet pattern class would be useful for each enemy/boss
class BulletCreator():
    def __init__(self,x,y,width,height,vel,color,moveType):
        self.rect = pygame.Rect(x,y,width,height)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = vel
        # self.sprite = sprite
        self.color = color
        self.moveType = moveType
    def draw(self,WIN):
        self.rect.x = self.x
        self.rect.y = self.y
        pygame.draw.rect(WIN,self.color,self.rect)
