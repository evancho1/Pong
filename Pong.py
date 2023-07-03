#import pygame
import pygame

#initialize pygame
pygame.init()

#constants and colours
size=(width,height)=(700,600)
white=(255,255,255)
red=(255,0,0)
blue=(0,0,255)
black=(0,0,0)

#variables 
x,y=350,300 #location of ball
xspeed,yspeed=8,0 #speed of ball
leftx,rightx=15,675 #location of paddles
lefty,righty=275,275 #location of paddles
leftyspeed,rightyspeed=0,0 #speed of paddles
p1score=0 #player 1's score
p2score=0 #player 2's score
pause=0 #variable to check if the game is paused 
count=360 #time remaining 
paused=False #variable to check if the game is paused 
started=False #variable to check if the game has started

#set screen size
screen=pygame.display.set_mode(size)

#name of game
pygame.display.set_caption("Pong")

#clock
clock=pygame.time.Clock()

#fonts
font1=pygame.font.SysFont("Trebuchet MS",18)
font2=pygame.font.SysFont("Impact",25)

#text
Msg=font1.render(f"Would you like to continue?",True, white)
continueMsg=font1.render(f"Press space to continue.",True, white)
quitMsg=font1.render(f"Press escape to quit.",True, white)
p1win=font2.render(f"Player 1 wins!",True, white)
p2win=font2.render(f"Player 2 wins!",True, white)
tie=font2.render(f"It's a tie!",True, white)
timesUp=font2.render(f"Time's up!",True, white)
start=font1.render(f"Press space to begin.",True, white)
restart=font2.render(f"Press space to restart.",True, white)
quitMsg2=font2.render(f"Press escape to quit.",True, white)

#functions
def keepPlaying(): #asks the user if they would like to keep playing 
        screen.blit(Msg,(250,150))
        screen.blit(continueMsg,(250,200))
        screen.blit(quitMsg,(250,250))

def winner(): #declares the winner of the game
    if p1score>p2score:
        screen.blit(p1win,(300,150))
    elif p1score<p2score:
        screen.blit(p2win,(300,150))
    else:
        screen.blit(tie,(300,150))

#main game code
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False

        #to move the paddles
        if paused==False:
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_w:
                    leftyspeed=-6
                if event.key==pygame.K_s:
                    leftyspeed=6
                if event.key==pygame.K_UP:
                    rightyspeed=-6
                if event.key==pygame.K_DOWN:
                    rightyspeed=6
            if event.type==pygame.KEYUP:
                if event.key==pygame.K_w:
                    leftyspeed=0
                if event.key==pygame.K_s:
                    leftyspeed=0
                if event.key==pygame.K_UP:
                    rightyspeed=0
                if event.key==pygame.K_DOWN:
                    rightyspeed=0

    #score in the corners
    score1=font1.render(f"Player 1: {p1score}",True, white)
    score2=font1.render(f"Player 2: {p2score}",True, white)
    screen.fill(black)

    #moving the paddles and ball
    x+=xspeed
    y+=yspeed
    lefty+=leftyspeed
    righty+=rightyspeed

    #require space bar to start the game
    if started==False:
        paused=True
        count+=1
        xspeed=0
        screen.blit(start,(300,150))
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                started=True
                paused=False
                xspeed,yspeed=8,0
                  
    #if p1 scores
    if x>width-10:
        x,y=350,300
        p1score+=1
        pause+=1

    #if p2 scores
    if x<10:
        x,y=350,300
        p2score+=1
        pause+=1

    #ball collision with top/bottom of screen
    if y>height-10 or y<10:
        yspeed=-yspeed

    #stops paddle from going out of screen
    if lefty<10 or lefty>515:
        leftyspeed=0
        
    #stops paddle from going out of screen
    if righty<10 or righty>515:
        rightyspeed=0

    #collision of ball with paddles
    if x+10>=rightx+10 and y+10>=righty and y+10<=righty+24 or \
       x-10<=leftx+10 and y+10>=lefty and y+10<=lefty+24:
        xspeed=-xspeed
        yspeed=-3
        
    #collision of ball with paddles
    if x+10>=rightx and y+10>=righty+24 and y-10<=righty+49 or \
       x-10<=leftx+10 and y+10>=lefty+24 and y-10<=lefty+49:
        xspeed=-xspeed 

    #collision of ball with paddles
    if x+10>=rightx and y-10>=righty+49 and y-10<=righty+75 or \
       x-10<=leftx+10 and y-10>=lefty+49 and y-10<=lefty+75:
        xspeed=-xspeed
        yspeed=3


    #after scoring, gives option to continue or quit
    if x==350 and y==300 and pause==1:
        xspeed,yspeed=0,0
        keepPlaying()
        count+=1
        paused=True
        leftx,rightx=15,675
        lefty,righty=275,275
        leftyspeed,rightyspeed=0,0
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                xspeed,yspeed=8,0
                pause-=1
                paused=False
        if event.type==pygame.KEYUP:
            if event.key==pygame.K_ESCAPE:
                pygame.draw.rect(screen,black,[225,125,250,200])
                winner()

    #game timer
    count-=1
    time=count//60
    timer=font1.render(f"Time Remaining: {time}",True, white)

    #when the game is finished 
    if time==0:
        count+=1
        x,y=350,300
        pause=0
        screen.blit(timesUp,(300,100))
        winner()
        paused=True
        leftx,rightx=15,675
        lefty,righty=275,275
        leftyspeed,rightyspeed=0,0
        screen.blit(restart,(300,200))
        screen.blit(quitMsg2,(300,250))
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                p1score=0
                p2score=0
                pause=0
                count=3600
                paused=False
            if event.key==pygame.K_ESCAPE:
                pygame.quit()
               
    #draw section
    screen.blit(timer,(275,10))
    screen.blit(score1,(10,10))
    screen.blit(score2,(580,10))
    pygame.draw.rect(screen,white,[leftx,lefty,10,75])
    pygame.draw.rect(screen,white,[rightx,righty,10,75])
    pygame.draw.circle(screen,white,(x,y),10)

    #update game 
    pygame.display.flip()

    #clock tick
    clock.tick(60)

#quit pygame
pygame.quit()





