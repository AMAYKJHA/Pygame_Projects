import pygame as pg
import math
import random
from pygame import mixer
pg.init()


screen  = pg.display.set_mode((800,600))
mixer.music.load("gameloop.mp3")
mixer.music.play(-1)

bonus_sound = mixer.Sound('bonus.wav')
damage_sound = mixer.Sound('loose.wav')
gameover_sound = mixer.Sound('game_over.wav')

upper_background = pg.image.load("background1.png")
lower_background = pg.image.load("background2.png")
player_img = pg.image.load("player.png")
apple = pg.image.load("apple.png")
thorn = pg.image.load("thorny.png")
star = pg.image.load("stars.png")
heart = pg.image.load("heart.png")

pg.display.set_caption("Newton`s Apple")
pg.display.set_icon(apple)

font1 = pg.font.Font('freesansbold.ttf',28)
font2 = pg.font.Font('freesansbold.ttf',40)



playerX = 60
playerY = 200
playerX_Change = 0


appleX = 0
appleY = 0
appleY_change = 0.5

thornX = 0
thornY = 0
thornY_change = 1.0
isfalling = False

apple_rect = apple.get_rect()
thorn_rect = thorn.get_rect()
player_rect = player_img.get_rect()

score = 0
life = 3

timer_running = False
start_time = 0

game_end = False
def falling_apple(x,y):
    screen.blit(apple,(x,y))
    
def falling_thorn(x,y):
    screen.blit(thorn,(x,y))

def show_player(X,Y):
    screen.blit(player_img,(X,Y))

def distance(X1,Y1,X2,Y2,cenX,cenY):
    dist = math.sqrt(math.pow((X1+75-X2-cenX),2)+math.pow((Y1+30-Y2-cenY),2))
    return dist

def show_score(value):
    text_score = font1.render("Score: "+str(value), True, (255,255,255))
    screen.blit(text_score, (580,160))

def show_heart(value):
    for i in range(0,value):
        screen.blit(heart,(580 + i*60,200))
    
def show_state():
    msg = font1.render("Press Space_Bar to play", True, (255,255,255))
    screen.blit(msg, (200,480))

def game_over():
    msg = font2.render("Game Over", True, (255,255,255))
    screen.blit(msg, (300,200))
   
isrunning = True
while isrunning:
    screen.blit(upper_background,(0,0))
    screen.blit(lower_background,(0,318))
    show_score(score)
    if(life != 0):
        show_heart(life)    
    else:
        game_over()     
    for event in pg.event.get():
        if(event.type == pg.QUIT): isrunning = False
        if(event.type == pg.KEYDOWN):
            if(event.key == pg.K_LEFT):
               playerX_Change = -2
            if(event.key == pg.K_RIGHT):
                playerX_Change = 2
            if(event.key == pg.K_SPACE):
                if(life!=0):
                    isfalling = not isfalling
                    appleX = random.randint(70,700)
                    appleY = random.randint(10,70)
                    thornX = random.randint(70,700)
                    thornY = random.randint(10,60)
        if(event.type == pg.KEYUP):
            playerX_Change = 0
            
    
    playerX+=playerX_Change   
    if(playerX >= 650): playerX = 650
    elif(playerX <= 5): playerX = 5
    
       
    if(appleY <= 370 and isfalling):
        appleY += appleY_change
        falling_apple(appleX,appleY)
    else:
        appleX = random.randint(70,700)
        appleY = random.randint(10,70)
        
    if(thornY <= 360 and isfalling):
        thornY += thornY_change
        falling_thorn(thornX,thornY)
    else:
        thornX = random.randint(70,700)
        thornY = random.randint(10,70)
    
    if(isfalling and distance(playerX,playerY,appleX,appleY,apple_rect.centerx,apple_rect.centery)<=28): #checking collision with apple
        score +=1
        bonus_sound.play()
        if(score%9 == 0): 
            appleY_change+= 0.4
            thornY_change+= 0.4
        appleX = random.randint(70,700)
        appleY = random.randint(10,70)  
    
    if(isfalling and distance(playerX,playerY,thornX,thornY,thorn_rect.centerx,thorn_rect.centery)<=28): #checking collision with thorn
        life -=1
        if(life!=0):
            damage_sound.play()
        else:
            mixer.music.stop()
            isfalling = False
            gameover_sound.play()
        thornY = random.randint(10,70)
        thornX = random.randint(70,700)
        start_time = pg.time.get_ticks()
        timer_running = True  
    
    
    
    if(not isfalling and life!=0): show_state()
    
    
    if(timer_running and (pg.time.get_ticks()-start_time)<4000):  # display stars over head for 4 seconds
        screen.blit(star,(playerX +50,180))
    else:
        timer_running = False
        
    
    #screen.set_at((playerX+75,playerY+30),(255,0,0)) # player`s head center
    #screen.set_at((appleX+10,appleY+11),(0,0,255)) #apple`s center
    show_player(playerX,playerY)
    pg.display.update()
    
    
