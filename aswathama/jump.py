import pygame
import math
import random
import time

pygame.init()


#### colors ####

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

finalExit = False


display_width  = 600 
display_height = 550



screen = pygame.display.set_mode((display_width,display_height))
clock = pygame.time.Clock()

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

obs1 = pygame.image.load('obstacle1.jpg')
obs2 = pygame.image.load('lion.png')
coin1 = pygame.image.load('dollar.png')


class obstacle:
	def __init__(self,x,y,width,height,speed = 10):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.speed = speed

	





class player:
	def __init__(self,x,y,width,height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.left = False
		self.right = False
		self.walkCount = 0
		self.jumpCount = 10
		self.isJump = False
		self.velocity = 7

	def draw(self,screen):
		
		if(self.walkCount+1 >= 27):
			self.walkCount = 0

		if(self.left):
			screen.blit(walkLeft[self.walkCount//3],(self.x,self.y))
			self.walkCount += 1
		elif(self.right):
			screen.blit(walkRight[self.walkCount//3],(self.x,self.y))
			self.walkCount += 1
		else:
			screen.blit(char,(self.x,self.y))
			#self.walkCount = 0
		pygame.display.update()


def displayMessage(text):
    fonts = pygame.font.Font('freesansbold.ttf',60)
    textSurface = fonts.render(text,True,gray)
    textRect = textSurface.get_rect()
    textRect.center = ((display_width/2),(display_height/4))
    screen.blit(textSurface,textRect)
    pygame.display.update()
    time.sleep(2)
    game_loop()



def crash():
    text = """Sorry,You Crashed!"""
    displayMessage(text)



def print_score(score):
    font = pygame.font.SysFont(None, 30)
    text = font.render("Score: "+str(score), True, (0,0,0))
    screen.blit(text,(0,0)) 



def redrawWindow():
	screen.blit(bg,(0,0))
	man.draw(screen)
	screen.blit(obs1,(obstacle1.x,obstacle1.y))
	screen.blit(obs2,(obstacle2.x,obstacle2.y))
	screen.blit(coin1,(dollar1.x,dollar1.y))
	pygame.display.update()


 

####### mainLOOP machanism  #########
man = player(50,420,40,40)
obstacle1 = obstacle(random.randrange(600,700),420,31,45,8)
obstacle2 = obstacle(random.randrange(700,1000),400,150,100,6)
dollar1 = obstacle(random.randrange(550,580),420,52,72,13) 
def game_loop():
	    # speed is dafault argument
	gameExit = False
	lion_score = 0
	obs_score = 0
	lion_status = 0
	dollar_status = 0	
	while not gameExit:
		clock.tick(40)

		for event in pygame.event.get():
			if(event.type == pygame.QUIT):
				gameExit = True
		keys = pygame.key.get_pressed()
		
		if(keys[pygame.K_LEFT]  and man.x > man.velocity-15):
			man.left = True
			man.right = False
			man.x = man.x - man.velocity
		elif(keys[pygame.K_RIGHT] and man.x < display_width - man.width - man.velocity ):
			man.right = True
			man.left  = False
			man.x = man.x + man.velocity	
		else:
			man.right = False
			man.left = False
			man.walkCount = 0			

		if not(man.isJump):
			if(keys[pygame.K_UP] and man.y > man.velocity - 10):
				man.y -= man.velocity
				man.walkCount = 0
			if(keys[pygame.K_DOWN] and man.y <  (display_height - man.height - man.velocity)):
				man.y += man.velocity	
				man.walkCount = 0	
			if(keys[pygame.K_SPACE]):
				man.isJump = True
				man.left = False
				man.right = False
				man.walkCount = 0
		else:
			if(man.jumpCount >= -10):
				neg = 1
				if(man.jumpCount < 0):
					neg = -1	
				man.y  = man.y - (man.jumpCount**2)*0.5*neg
				man.jumpCount -= 1	
			else:
				man.isJump = False
				man.jumpCount = 10	

	
		redrawWindow()
		#screen.blit(obs1,(obstacle1.x,obstacle1.y))
		obstacle1.x = obstacle1.x - obstacle1.speed
		obstacle2.x = obstacle2.x - obstacle2.speed
		dollar1.x = dollar1.x  - dollar1.speed

		print_score(lion_score + obs_score)
		print(" obstacle1.x ",obstacle1.x,obstacle1.y)
		pygame.display.update()
		if(obstacle1.x < 0):
			obstacle1.x = random.randrange(700,900)
			obstacle1.y = 420
			obs_score = obs_score + 2
			lion_status += 1
		if(obstacle2.x < -100 and lion_status==4):
			obstacle2.x = random.randrange(800,1000)
			obstacle2.y = 400	
			lion_score += 5	
			lion_status = 0
			dollar_status += 1
		if(dollar1.x < -10 and dollar_status > 3):
			dollar1.x = random.randrange(500,580)
			dollar1.y = 420
			dollar_status = 0	

		'''if(man.x < obstacle1.x + obstacle1.width):
			print('x crossover')

			if(man.y<obstacle1.y+obstacle1.height):
				print('y crossover')
				crash()'''


	#pygame.display.update()
	
	
	
	
	
        

if(finalExit == False):
    game_loop()
else:    
    pygame.quit()
    quit()


