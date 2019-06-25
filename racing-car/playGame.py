import pygame
import time
import random

pygame.init()


finalExit = False

display_width = 1200
display_height = 700




black = (0,0,0)
white = (255,255,255)
green = (51,144,11)
red = (255,0,0)
gray = (128,117,140)
teal = (0,128,128)
maroon = (128,0,0)
cyan = (0,255,255)
olive = (128,128,0)
aqua_marin = (127,255,212)
violet = (138,43,226)
brown = (188,143,143)
orange = (255,180,30)

color_list = [black,white,red,gray,teal,maroon,cyan,olive,aqua_marin,violet,brown]
    

car_width = 60

gameDisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('A bit Racey')
clock = pygame.time.Clock()
#bg = pygame.image.load('adult.jpg')   # you can add any background image 
policeCar = pygame.image.load('sportscar.jpg')
policeCar1 = pygame.image.load('police.jpg')

enemy = [policeCar,policeCar1] 


carImg = pygame.image.load('raceCar.png')

def obstacle(thingX,thingY,policeCar):

    gameDisplay.blit(policeCar,(thingX,thingY))
    #gameDisplay.blit(policeCar1,( 1 + random.randrange(0,500),1 + random.randrange(-600,-200)))
    #pygame.draw.rect(gameDisplay,color,[thingX,thingY,thing_width,thing_height])


def car(x,y):
    gameDisplay.blit(carImg,(x,y))

def displayMessage(text):
    fonts = pygame.font.Font('freesansbold.ttf',60)
    textSurface = fonts.render(text,True,gray)
    textRect = textSurface.get_rect()
    textRect.center = ((display_width/2),(display_height/4))
    gameDisplay.blit(textSurface,textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()



def crash():
    text = """Sorry,You Crashed!"""
    displayMessage(text)  
 


def things_dodged(count,rewards,speed):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: "+str(count), True, black)
    gameDisplay.blit(text,(0,0)) 
    text1 = font.render("Rewards($): "+str(rewards), True, black)
    gameDisplay.blit(text1,(0,14))
    if(speed > 5):
        if(speed > 6.3):
            text2 = text2 = font.render("Speed(critical): "+str(round(speed*100.007,2))+"m/s", True, red)
            gameDisplay.blit(text2,(0,28))
        else:
            text2 = text2 = font.render("Speed(danger): "+str(round(speed*100.007,2))+"m/s", True, orange)
            gameDisplay.blit(text2,(0,28))  

    else:    
        text2 = font.render("Speed(safe): "+str(round(speed*100.003 + 0.003,2))+"m/s", True, green)
        gameDisplay.blit(text2,(0,28))




def game_loop():
    print(" its game_loop ")
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    thingX = random.randrange(0,display_width)
    thingY = -600
    thing_speed = 1.01
    thing_width = 70
    thing_height = 80
    SCORE = 0
    rewards = 0.0
    thing2X = random.randrange(0,display_width)
    thing2Y = -300
    thing2_speed = 5
    thing2_width = 20
    thing2_height = 40


    x_change = 0
    y_change = 0

    gameExit = False

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    x_change = -6
                if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    x_change = 6.3
                if event.key == pygame.K_UP:
                   # thing_speed += 0.7
                    y_change = y_change - 3
                if event.key == pygame.K_DOWN:
                    #thing_speed -= 1 
                    y_change = y_change + 1  
                if(event.key == pygame.K_w):
                    thing_speed += 0.5
                if(event.key == pygame.K_s):
                    thing2_speed -= 1        
                if event.key ==  pygame.K_x:
                    pygame.quit()
                    quit()
                    
                      
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0   
                if( event.key == pygame.K_UP or event.key == pygame.K_DOWN):
                    y_change = 0     


                    

       # SCORE = SCORE + thing_speed*100
        x += x_change
        y += y_change
        gameDisplay.fill((255,255,255))
        #gameDisplay.blit(bg, (0,0))


        obstacle(thingX,thingY,policeCar)
        obstacle(thing2X,thing2Y,policeCar1)
        thing2Y += thing_speed
        thingY += thing_speed
        car(x,y)
        thing_speed = round(thing_speed,2)
        things_dodged(round(SCORE,2),rewards,thing_speed)

        if x > display_width - car_width or x < 0:
            crash()

        if thingY > display_height:
            thingX = random.randrange(0,display_width)
            thingY = 0 - thing_height*2
            #obstacle(thingX,thingY,t
            #thing_speed += 0.3
            SCORE += 10
            rewards = rewards + (SCORE+0.075)*1.2  # random scale to predict rewards along with score
            rewards = round(rewards,2)
            if(thing_speed > 5):
                thing_speed = thing_speed + 0.019
            else:
                thing_speed = thing_speed + 0.35
                thingY *= thing_speed

        if y < thingY+thing_height:
            print('y crossover')

            if (x > thingX and x < thingX + thing_width or x+car_width > thingX and x + car_width < thingX+thing_width):
                print('x crossover')
                crash()    


         ## second enemy car
        if x > display_width - car_width or x < 0:
            crash()

        if thing2Y > display_height:
            thing2X = random.randrange(0,display_width)
            thing2Y = 0 - thing2_height*2
            #obstacle(thingX,thingY,t
            #thing_speed += 0.3
            SCORE += 3.77
            rewards = rewards + (5)*1.1  # random scale to predict rewards along with score
            rewards = round(rewards,2)
            thing2Y = thing_speed

        if y < thing2Y+thing2_height:
            print('y crossover')

            if (x > thing2X and x < thing2X + thing2_width or x+car_width > thing2X and x + car_width < thing2X+thing2_width):
                print('x crossover')
                crash()        
    
            
        
        pygame.display.update()
        clock.tick(150)




if(finalExit == False):
    game_loop()
else:    
    pygame.quit()
    quit()
