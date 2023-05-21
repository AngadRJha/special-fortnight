import pygame
import random
import time
from pygame import mixer
pygame.init()
win=pygame.display.set_mode((500,450))
pygame.display.set_caption("*Flawless Graphics*")
clock=pygame.time.Clock()
gamestate="Initial"
second=0
#main character
bloack1=pygame.image.load("Man running\Man1.png").convert_alpha()
bloack2=pygame.image.load("Man running\Man2.png").convert_alpha()
bloack3=pygame.image.load("Man running\Man3.png").convert_alpha()
bloack4=pygame.image.load("Man running\Man4.png").convert_alpha()
bloack5=pygame.image.load("Man running\Man5.png").convert_alpha()
bloack6=pygame.image.load("Man running\Man6.png").convert_alpha()
bloack7=pygame.image.load("Man standing\Man_Standing.png").convert_alpha()
bloack8=pygame.image.load("Man_Rising.png").convert_alpha()
bloack9=pygame.image.load("Skull.png").convert_alpha()
x_pos_main=-125
y_pos_main=255
player_gravity=0
block_state="Run"
block=[bloack1,bloack2,bloack3,bloack4,bloack5,bloack6]
block_index=0
block_surf=block[block_index]
vel_=0.5
#Backdrop
backdrop=pygame.image.load("Backdrop.png")
ground=pygame.Surface((500,50))



#Writing Text
textfont=pygame.font.Font("Pokemon GB.ttf",40)
text=textfont.render("Rotate",False,"Black")

#introduction
intro=pygame.image.load("Intro.png")

#loading
load1=pygame.image.load("Loading animation\Loading1.png")
load2=pygame.image.load("Loading animation\Loading2.png")
load3=pygame.image.load("Loading animation\Loading3.png")
loadarray=[load1,load2,load3]
load_index=0
load=loadarray[load_index]
x_pos_load=-280
y_pos_load=-160

#Velocities
vel=5
vel_rot=0.04


#animations
x_pos_tb=250
x_pos=510
xp=-500
def produce_blocks():
    global x_pos,xp,vel_rot
    for i in range(5):
        rect=pygame.draw.rect(win,("Grey"),(x_pos-((100)/2-20),0,100,400))
        rect=pygame.draw.rect(win,("Yellow"),(x_pos,(int(random.choice("123")))*100,50,50))
        vel_rot+=0.0000000000000000000000000000000000001
        x_pos-=vel
        if x_pos<-250:
            x_pos=737
        

def Load():
    global load, load1, load2, load3, loadarray,load_index,x_pos_load,y_pos_load
    if load_index>3:
        load_index=0
    load=loadarray[int(load_index)] 
    load_index+=0.1
   
def Run():
    global bloack1,bloack2,bloack3,bloack4,bloack5,bloack6,block_index,block,block_surf
    if block_state=="Run":
        if block_index>6:
            block_index=0
        block_surf=block[int(block_index)]
        block_index+=0.15
    if block_state=="Standing":
        block_surf=bloack7
    if block_state=="Heaven":
        block_surf=bloack8
    if block_state=="Dead":
        block_surf=bloack9
    

#play sounds
mixer.music.load("Push-Long-Version.mp3")
mixer.music.play(-1)
run=True
while run:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            run=False
        #if event.type==pygame.MOUSEMOTION:
            #print(event.pos)

    keys=pygame.key.get_pressed()

    
    
    if gamestate=="Initial":
        #Displaying ground
        #ground.fill("Brown")
        #win.blit(ground,(0,450))
        #pygame.draw.rect(win,(250,250,250),(0,440,500,10))


        #Intro
        #win.blit(intro,(-80,-100))

        #Displaying backdrop
        win.blit(backdrop,(0,0))

        #loading animation
        Load()
        Run()
        load=pygame.transform.scale(load,(705,354))
        win.blit(load,(x_pos_load+185,y_pos_load+130))

        #Displaying text
        Start=pygame.draw.rect(win,("Red"),(115,60,300,70),3,35)
        Start=pygame.draw.rect(win,("#FFCCCB"),(115,60,300,70),0,35)
        win.blit(text,(125,70))
        
        #Detecting if Start button has been clicked
        mouse=pygame.mouse.get_pos()
        if Start.collidepoint(mouse):
                if event.type==pygame.MOUSEBUTTONDOWN:
                    print("Start Button has been clicked")
                    gamestate="Part 2"
        
        #Displaying character on screen
        block_surf=pygame.transform.scale(block_surf,(173*2,90*2))
        win.blit(block_surf,(x_pos_main,y_pos_main))
        
        #Allowing character to jump
        player_gravity+=0.5
        y_pos_main+=player_gravity
        if y_pos_main>255:
            y_pos_main=255
        if y_pos_main>=255:   
            if event.type==pygame.KEYDOWN:
                if keys[pygame.K_UP]:
                    player_gravity=-10
                
        #moving character
        x_pos_mainprev=x_pos_main
        x_pos_main+=3
        if x_pos_main!=-1:
            stuff=pygame.draw.rect(win,(250,250,0),(x_pos_main+140,y_pos_main+150,60,20))
        if x_pos_main>500-125:
            x_pos_main=-200
        if y_pos_main<-145:
            y_pos_main=415
        if y_pos_main>500:
            y_pos_main=-140

    
    #Changing Gamestates
    elif gamestate=="Part 2":
        Run()
        block_state="Run"
        win.fill((0,0,200))
        ground=pygame.draw.rect(win,("White"),(0,400,500,50))
        x_pos_main=-125

        #Controls time and makes blocks
        timeblock=pygame.draw.rect(win,(250,250,250),(x_pos_tb,510,20,20))
        if x_pos_tb>0:
            veli=5
        else:
            veli=1.4
        x_pos_tb-=veli
        if x_pos_tb<-150:
            x_pos_tb=250
            second=second+1
        for i in range(0,25):
            if x_pos_tb<250:
                produce_blocks()
                black=pygame.draw.rect(win,(0,0,0),(180,400,100,200))
        
        print(second)
        if second>1:
            x_pos_main=50
            
        if second>4:
            block_state="Standing"
            x_pos_main=50
            vel_+=0.01
            y_pos_main-=vel_
        if y_pos_main<-180:
            y_pos_main=500
        if second>20:
            block_state="Dead"

        
            
        
        block_surf=pygame.transform.scale(block_surf,(173*2,90*2))
        win.blit(block_surf,(x_pos_main,y_pos_main))



        largerect=pygame.draw.rect(win,("Grey"),(xp,0,500,500))
        vel+=0.1
        xp+=vel
        if xp>500:
            xp=-500

        #player_gravity+=0.5
        #y_pos_main+=player_gravity
        #if y_pos_main>255:
            #y_pos_main=255
        #if y_pos_main>=255:   
         #   if event.type==pygame.KEYDOWN:
          #      if keys[pygame.K_UP]:
           #         player_gravity=-10
        
            
    
    
    pygame.display.update()
    clock.tick(60)