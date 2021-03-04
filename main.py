import pygame
from pygame.locals import *
import time
pygame.init()
#Variables
white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
screenWidth=400
screenHeight=250
fps=15
screen= pygame.display.set_mode((screenWidth,screenHeight))
pygame.display.set_caption('snake-game')
clock=pygame.time.Clock()
font=pygame.font.Font(None, 25)
def gameOver_message(msg, textcolor):
  text= font.render(msg, True, textcolor)
  screen.blit(text, [10, screenHeight/2])
def gameloop(): 
  gameStart = True
  gameOver=False
  movex=0
  movey=0
  x=100
  y=100
  block_size=5
  while gameStart:
    #controlling game Over
    while gameOver==True:
      screen.fill(white)
      gameOver_message("Game Over! press c to continue and q to quit", red)
      pygame.display.update()
      for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
            print('quit')
            gameOver=False
            gameStart=False
          elif event.key == pygame.K_c:
            print('game running')
            gameloop()
        
    #controling Quit
    for event in pygame.event.get():
      if event.type== pygame.QUIT:
        gameStart = False
        #controling basic snake movement 
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
          movey=0
          movex = -5
        elif event.key == pygame.K_RIGHT:
          movey=0
          movex = +5
      if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
          movex= 0
          movey = -5
        elif event.key == pygame.K_DOWN:
          movex= 0
          movey = +5
      #defining borders
      


      '''
      if event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
          movex=0
      '''
    x= x+ movex
    y= y+ movey
    if x>screenWidth-block_size or x<0 or y<0 or y>screenHeight-block_size:
      gameOver = True
    #controlling fps
    clock.tick(fps)
    screen.fill(white)
    pygame.draw.rect(screen, black,[x,y,block_size,block_size])
    pygame.display.update()
  pygame.quit
    #x= x + movex
gameloop()

