import pygame as pg
from random import randint


class Pipe:
    def __init__(self,pipe_scale_factor,moveSpeed):
        self.img_up=pg.transform.scale_by(pg.image.load('Requirements/pipeup.png').convert_alpha(),pipe_scale_factor)
        self.img_down=pg.transform.scale_by(pg.image.load('Requirements/pipedown.png').convert_alpha(),pipe_scale_factor)
        self.rect_up=self.img_up.get_rect()
        self.rect_down=self.img_down.get_rect()
        self.pipe_distance=200
        self.rect_up.y=randint(240,420)
        self.rect_up.x=400
        self.rect_down.y=self.rect_up.y-self.pipe_distance-self.rect_up.height
        self.rect_down.x=400
        self.moveSpeed=moveSpeed
        
    def drawPipe(self,win):
        win.blit(self.img_up,self.rect_up)
        win.blit(self.img_down,self.rect_down)
    
    def update(self,dt):
        self.rect_up.x-=int(self.moveSpeed*dt)
        self.rect_down.x-=int(self.moveSpeed*dt)