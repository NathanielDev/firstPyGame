import pygame
import os
from Bullet import Bullet
from BulletHandler import BulletHandler

class Player():
    def __init__(self,x,y,width,height,pBulletW,pBulletH,pBulletV,pBulletC,pBulletM,spritePath,isP1):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 7
        self.rect = pygame.Rect(x,y,width,height)
        if isP1:
            self.sprite = pygame.transform.scale(pygame.image.load(spritePath),(width,height))
        else:
            self.sprite = pygame.transform.rotate(pygame.transform.scale(pygame.image.load(spritePath),(width,height)),180)
        self.pbList = BulletHandler() #player's bullet list, so there can only e a X number of shoots on screen at one time,
        self.pBulletW = pBulletW
        self.pBulletH = pBulletH
        self.pBulletV = pBulletV
        self.pBulletC = pBulletC
        self.pBulletM = pBulletM
        self.isP1 = isP1

    # def update_rect(self):
    #     self.rect.x = self.x
    #     self.rect.y = self.y

    
        
    def draw(self,WIN,debug):
        WIN.blit(self.sprite,(self.rect.x,self.rect.y))
        if debug: #draw only hitboxes
            pygame.draw.rect(WIN,(255,0,0),self.rect)
    def shoot(self):#TODO: center player shots
        Bullet(self.rect.x+20,self.rect.y+20,self.pBulletW,self.pBulletH,self.pBulletV,self.pBulletC,self.pBulletM,handler=self.pbList) #braindead moment
    def handle_movement(self):
        keys = pygame.key.get_pressed()

        if self.isP1:    
            if keys[pygame.K_w] and self.rect.y - self.vel > 700//2 + 30: #WIDTH//2 + BORDER_WIDTH
                self.rect.y -= self.vel
            
            if keys[pygame.K_s] and self.rect.y + self.vel < 700 - self.height:
                self.rect.y += self.vel
            
            if keys[pygame.K_a] and self.rect.x - self.vel > 0:
                self.rect.x -= self.vel
            
            if keys[pygame.K_d] and self.rect.x + self.vel < 1400 - self.width:
            
                self.rect.x += self.vel
        if keys[pygame.K_j]:
            self.shoot()
            print("hey")

        


        
        
   