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
x=5
y=5
while gameStart:
  screen.fill(white)
  screen.fill(black, rect=[200,100,x,y])
  for event in pygame.event.get():
    if event.type== pygame.QUIT:
      gameStart = False
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_LEFT:
        movex += 5
      ` x= x + movex

  pygame.display.update()
pygame.quit
