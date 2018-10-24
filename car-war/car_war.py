import pygame
import time
import random
pygame.init()
width=800
height=600
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
best=-1
gameDisplay=pygame.display.set_mode((800,600))
pygame.display.set_caption('CAAAAAAAR')
carimg=pygame.image.load('carr.png')
carimge=pygame.image.load('car1.png')
carimage1=pygame.image.load('carrrr.png')
def car1(x2,y2):
    gameDisplay.blit(carimage1,(x2,y2))
def car(x,y):
    gameDisplay.blit(carimg,(x,y))
def opcar(x1,y1):
    gameDisplay.blit(carimge,(x1,y1))

def thing_dodged(count):
    font=pygame.font.SysFont(None,25)
    text=font.render("score: "+str(count),True,black)
    gameDisplay.blit(text,(0,0))

def txt_obj(text,font):
    txtsurface=font.render(text,True,red)
    return txtsurface,txtsurface.get_rect()
    
def display_massage(text):
    largeText=pygame.font.Font('freesansbold.ttf',50)
    txtsurf,txtrect=txt_obj(text,largeText)
    txtrect.center=(width/2,height/2)
    gameDisplay.blit(txtsurf,txtrect)
    pygame.display.update()
    
def crashed(cnt):
    global best
    display_massage('CRASHED PLAY MORE Y/N')
    time.sleep(1)
    gameDisplay.fill(white)
    if cnt>=best:
        best=cnt
        display_massage('CONGRATS IT WAS BEST')
    else:
        display_massage('BETTER LUCK NEXT TIME')
    time.sleep(1)
    gameDisplay.fill(white)
    car(0,0)
    for event in pygame.event.get():
        gameDisplay.fill(white)
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_y:
                display_massage('READY')
                time.sleep(1)
                game_loop()
            elif event.key==pygame.K_n:
                display_massage('BYE BYE')
                time.sleep(1)
                pygame.quit()
                exit()
            
   
def game_loop():
   
    x=(width*0.45)
    y=(height*0.7)
    count=0
    thing_x=random.randrange(0,width-78)
    thing_y=-600
    thing_x1=random.randrange(0,width-75)
    thing_y1=-500
    thing_speed1=4
    thing_speed=4
    change=0
    changey=0
    clock=pygame.time.Clock()
    crash=False
    while not crash:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()
               
            if event.type==pygame.KEYDOWN:
                if (event.key==pygame.K_RIGHT):
                    if(thing_speed<=5):
                        change=thing_speed+1
                    elif(thing_speed>8):
                        change=8
                    else:
                        change=int(thing_speed)
                if event.key==pygame.K_LEFT:
                    if(thing_speed<5):
                        change=-(thing_speed+2)
                    elif(thing_speed>8):
                        change=-8
                    else:
                        change=-int(thing_speed)
                if event.key==pygame.K_UP:
                    if(thing_speed<5):
                        changey=-(thing_speed+2)
                    elif(thing_speed>8):
                        changey=-8
                    else:
                        changey=-int(thing_speed)
                if event.key==pygame.K_DOWN:
                    if(thing_speed<5):
                        changey=(thing_speed+2)
                    elif(thing_speed>8):
                        changey=8
                    else:
                        changey=int(thing_speed)
            elif event.type==pygame.KEYUP:
                if event.key==pygame.K_RIGHT or event.key==pygame.K_LEFT:
                    change=0
                if event.key==pygame.K_UP or event.key==pygame.K_DOWN:
                    changey=0
        x=x+change 
        y=y+changey
        gameDisplay.fill(white)
        opcar(thing_x,thing_y)
        if (not(thing_x1+72>=thing_x and thing_x1<=thing_x+75 and thing_y1+154>=thing_y and thing_y1<thing_y+157)):
            car1(thing_x1,thing_y1)
        thing_y+=int(15*(1-1/(1.07**(thing_speed))))
        thing_y1+=int(15*(1-1/(1.07**(thing_speed))))
        if thing_y>height:
            count=int(count+thing_speed/3)
            thing_y=-50
            thing_x=random.randrange(0,width-72)
            thing_speed+=1;
        
        car(x,y)
        thing_dodged(count)
        
        if(thing_x1+76>=x and thing_x1<=x+89 and thing_y1+156>=y and thing_y1<y+180):
            thing_x1=random.randrange(0,width-75)
            thing_y1=-100
            count=int(count+5*thing_speed/3)
        
        
        if thing_y1>height:
            if count>=thing_speed1/3:
                count=int(count-thing_speed1/3)
            thing_y1=-50
            thing_x1=random.randrange(0,width-72)
            
        if(thing_x+74>=x and thing_x<=x+89 and thing_y+155>=y and thing_y<y+180):
            thing_speed=0
            thing_speed1=0
            change=0
            changey=0
            crashed(count)
        if y+180>height or y<=0:
            y=y-changey
        if x>width-89 or x<0:
            thing_speed=0
            thing_speed1=0
            change=0
            crashed(count)
            
        pygame.display.update()
        clock.tick(100)

game_loop()
pygame.quit()
exit()