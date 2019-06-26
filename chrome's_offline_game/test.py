import pygame
import random
import time

pygame.init()

display_width =  1000
display_height = 300

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('testing__')
clock = pygame.time.Clock()

gameExit = False
thing_speed = 10
thingY = display_height - 71
thingX =  random.randrange((display_width+100),(display_width+500))
thing2X = random.randrange((display_width+100),(display_width+500))
thing2Y = display_height - 71


dino = pygame.image.load('dino.jpg')
cectus = pygame.image.load('cectus.jpg')
cectus1 = pygame.image.load('cectus1.jpg')
cloud  = pygame.image.load('cloud.jpg')

SCORE = 0

dinoX = 50
dinoY = (150+80)
dino_width = 80
dino_height = 80
dinoY_change = 0
dinoX_change = 0

cloudX = 500
cloudY = 60

isJump = False
velocity = 5
jumpCount = 10

def Dino(dinoX,dinoY):
    screen.blit(dino,(dinoX,dinoY))



def obstacle(thing,thingX,thingY):
    #pygame.draw.rect(screen,color,[thingX,thingY,thing_width,thing_height])
    screen.blit(thing,(thingX,thingY))



def score_display(score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(score), True, (0,0,0))
    screen.blit(text,(600,150))    

while not gameExit:

    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN):
            if( event.key == pygame.K_x ):
                pygame.quit()
                quit()
    keys = pygame.key.get_pressed()
        
    if(keys[pygame.K_LEFT] and dinoX > velocity):
        dinoX = dinoX - velocity
    if(keys[pygame.K_RIGHT] and dinoX < display_width - dino_width - velocity ):
        dinoX = dinoX + velocity        

    if not(isJump):
        if(keys[pygame.K_UP] and dinoY > velocity):
            dinoY -= velocity
        if(keys[pygame.K_DOWN] and dinoY <  (display_height - dino_width - velocity)):
            dinoY += velocity       
        if(keys[pygame.K_SPACE]):
                isJump = True
    else:
        if(jumpCount >= -10):
            neg = 1
            if(jumpCount < 0):
                neg = -1    
            dinoY = dinoY - (jumpCount**2)*0.5*neg
            jumpCount -= 1  
        else:
            isJump = False
            jumpCount = 10  
            


    
    screen.fill((255,255,255))
    obstacle(cectus,thingX,thingY) 
    obstacle(cectus1,thing2X,thing2Y) 
    screen.blit(cloud,(cloudX,cloudY))   
   # thing_speed += 4
    thingX -= thing_speed
    thing2X -= thing_speed
    Dino(dinoX,dinoY)
    score_display(SCORE)
    pygame.display.update()    
    clock.tick(50)

    if thingX < 0 :
            thingX = random.randrange(display_width+ 100,display_width + 500)
            thingY = display_height - 71
            SCORE += 5
    if thing2X < 0 :
            thing2X = random.randrange(display_width+ 100,display_width + 500)
            thing2Y = display_height - 100  
            SCORE += 5      



pygame.quit()
quit()