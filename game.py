import pygame as pg
import sys,time
from yelluvBird import Ybird
from pipe import Pipe
pg.init()

class Game:
    def __init__(self):
        self.width=400
        self.height=650
        self.scale_factor=1.1
        self.pipe_scale_factor=0.35
        self.bg_scale_factor=2
        self.bird_scale_factor=1
        self.win=pg.display.set_mode((self.width,self.height))
        self.clock=pg.time.Clock()
        self.moveSpeed=250
        self.game_score_count=False
        self.score_count=0
        self.font=pg.font.Font('Requirements\DragonHunter-9Ynxj.otf',24)
        self.score_text=self.font.render('Score : 0',True,(0,0,0))
        self.score_text_rect=self.score_text.get_rect(center=(60,30))
        
        self.play_again_text=self.font.render('Play Again',True,(0,0,0))
        self.play_again_text_rect=self.play_again_text.get_rect(center=(200,600))
        self.yelluvBird=Ybird(self.scale_factor)
        self.is_enter_pressed=False
        self.is_game_started=True 
        
        self.pipes=[]
        self.pipe_counter=201
        self.backgroundAndGroundImg()
        
        
      
        self.gameloop()
    
    def gameloop(self):
        lastTime=time.time()
        while True:
            newTime=time.time()
            dt=newTime-lastTime
            lastTime=newTime
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type==pg.KEYDOWN and self.is_game_started:
                    if event.key==pg.K_RETURN:
                        self.is_enter_pressed=True
                        self.yelluvBird.set_gravity=True
                    if event.key==pg.K_SPACE and self.is_enter_pressed:
                        self.yelluvBird.flap(dt) 
                if event.type==pg.MOUSEBUTTONUP:
                    if self.play_again_text_rect.collidepoint(pg.mouse.get_pos()):
                     self.play_again_theGame()
            self.UpdateEverythings(dt)
            self.ground_stay()        
            self.draw()
            self.game_score()
            pg.display.update()
            self.clock.tick(120)
            
    def play_again_theGame(self):
        self.score=0
        self.score_text=self.font.render('Score : 0',True,(0,0,0))
        self.is_enter_pressed=False
        self.is_game_started=False
        self.yelluvBird.resetPostion()
        self.pipes.clear()
        self.pipe_counter=201
        self.yelluvBird.set_gravity=False
            
    def game_score(self):
        if len(self.pipes)>0:
            if (self.yelluvBird.rect.left > self.pipes[0].rect_down.left and 
            self.yelluvBird.rect.right < self.pipes[0].rect_down.right and not self.game_score_count):
                self.game_score_count=True
            if self.yelluvBird.rect.left > self.pipes[0].rect_down.right and self.game_score_count:
                self.game_score_count=False 
                self.score_count+=1   
                self.score_text=self.font.render(f"Score : {self.score_count}",True,(0,0,0))
            
    def ground_stay(self):
        if len(self.pipes):
          if self.yelluvBird.rect.bottom>519:
              self.yelluvBird.set_gravity=False
              self.is_enter_pressed=False
              self.is_game_started=False
          if(self.yelluvBird.rect.colliderect(self.pipes[0].rect_down)or
              self.yelluvBird.rect.colliderect(self.pipes[0].rect_up)):
              self.is_enter_pressed=False
              self.is_game_started=False
             
            
    def UpdateEverythings(self,dt):
        if self.is_enter_pressed:
           self.ground1Rect.x-=int(self.moveSpeed*dt)
           self.ground2Rect.x-=int(self.moveSpeed*dt)
        
           if self.ground1Rect.right<0:
              self.ground1Rect.x=self.ground2Rect.right
           if self.ground2Rect.right<0:
              self.ground2Rect.x=self.ground1Rect.right
              
          
            
           if self.pipe_counter>200:
               self.pipes.append(Pipe(self.pipe_scale_factor,self.moveSpeed))
               self.pipe_counter=0
               
           self.pipe_counter+=1
           for pipe in self.pipes:
               pipe.update(dt)
            
           if len(self.pipes)!=0:
                if self.pipes[0].rect_up.right<0:
                    self.pipes.pop(0)
                    
                   
            
        self.yelluvBird.update(dt)
                
            
    def draw(self):
        self.win.blit(self.bg_img,(-200,0))
        for pipe in self.pipes:
            pipe.drawPipe(self.win)
        self.win.blit(self.grnd1_img,self.ground1Rect)
        self.win.blit(self.grnd2_img,self.ground2Rect)
        self.win.blit(self.yelluvBird.image,self.yelluvBird.rect)
        self.win.blit(self.score_text,self.score_text_rect)
        if not self.is_game_started:
             self.win.blit(self.play_again_text,self.play_again_text_rect)
            
        
            
    def backgroundAndGroundImg(self):
         self.bg_img=pg.transform.scale_by(  pg.image.load('Requirements/bluebg.jpg').convert(),self.bg_scale_factor)
         self.grnd1_img=pg.transform.scale_by(pg.image.load('Requirements/groundimg.png').convert(),self.scale_factor)
         self.grnd2_img=pg.transform.scale_by(pg.image.load('Requirements/groundimg.png').convert(),self.scale_factor)
         self.ground1Rect=self.grnd1_img.get_rect()
         self.ground2Rect=self.grnd2_img.get_rect()
         self.ground1Rect.x=0
         self.ground2Rect.x=self.ground1Rect.right
         self.ground1Rect.y=516
         self.ground2Rect.y=516
         
        
        

game=Game()
        
                
        