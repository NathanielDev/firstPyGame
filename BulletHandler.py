import pygame
#TODO: maybe create child class for diffent kind of enemy patterns. SP
#TODO!: limitplayer shot rate XDDD
class BulletHandler():
    def __init__(self):
        self.bulletList = []
    
    def append(self,newBullet):
        self.bulletList.append(newBullet)
    def handleBullets(self): #TODO: merge handleBullets and drawall so it can become O(n)?
        for bullet in self.bulletList:
            if bullet.moveType == "-x":
                bullet.x -= bullet.vel
            elif bullet.moveType == "+x":
                bullet.x += bullet.vel
            elif bullet.moveType == "-y":
                bullet.y -= bullet.vel
            elif bullet.moveType == "+y":
                bullet.y += bullet.vel
            if bullet.y > 700 or bullet.y < 0:
                self.bulletList.pop(self.bulletList.index(bullet))
                
    def draw_all(self,WIN):
        for bullet in self.bulletList:
            bullet.rect.x = bullet.x
            bullet.rect.y = bullet.y
            
            pygame.draw.rect(WIN,bullet.color,bullet.rect)
    def __len__(self):
        return len(self.bulletList)
                