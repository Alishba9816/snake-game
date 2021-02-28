import pygame
from pygame.locals import *
pygame.init()

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
screen= pygame.display.set_mode((450,250))
pygame.display.set_caption('snake-game')
gameStart = True
movex=0
movey=0
clock=pygame.time.Clock()
x=100
y=100
while gameStart:
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      gameStart = False
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
        '''
    if event.type == pygame.KEYUP:
      if event.key == pygame.K_LEFT or event.key==pygame.K_RIGHT:
        movex=0
        '''
  x= x+ movex
  y= y+ movey
  clock.tick(10)
  screen.fill(white)
  pygame.draw.rect(screen, black,[x,y,5,5])
  #x= x + movex

  pygame.display.update()
pygame.quit
