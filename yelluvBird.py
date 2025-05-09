import pygame as pg

class Ybird(pg.sprite.Sprite):
    def __init__(self,bird_scale_factor):
        super(Ybird,self).__init__()
        self.birdImg=[pg.transform.scale_by(pg.image.load('Requirements/FlappyBirdDn2.png').convert_alpha(),bird_scale_factor),
                      pg.transform.scale_by(pg.image.load('Requirements/FlappyBirdUp2.png').convert_alpha(),bird_scale_factor)]
        self.imgIndex=0
        self.image=self.birdImg[self.imgIndex]
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.gravity=5
        self.flap_speed=350
        self.animCounter=0
        self.set_gravity=False
        
    def update(self,dt):
        if self.set_gravity:
           self.animation()
           self.applyGravity(dt)
        
           if self.rect.y<=0 :
              self.rect.y=0
              self.flap_speed=0
            
           elif self.rect.y>=0 and self.flap_speed==0:
              self.flap_speed=350
        
        
    def applyGravity(self,dt):
           self.y_velocity+=self.gravity*dt
           self.rect.y+=self.y_velocity
        
    def flap(self,dt):
        self.y_velocity-=self.flap_speed*dt
        
    def animation(self):
        if self.animCounter==20:
            self.image=self.birdImg[self.imgIndex]
            if self.imgIndex==0:
                self.imgIndex=1
            else:
                self.imgIndex=0
            self.animCounter=0
        self.animCounter+=1
        
    def resetPostion(self):
        self.rect=self.image.get_rect(center=(100,100))
        self.y_velocity=0
        self.animCounter=0
        
    