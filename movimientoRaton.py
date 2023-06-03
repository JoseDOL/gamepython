import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()
ventana = pygame.display.set_mode((500,500))
pygame.display.set_caption("Vomimiento raton")
coloFondo = (118,119,118)
colorFiguras = (255,255,255)
#variables
velocidad = 10
direccion = True
posX, posY = randint(1,400), randint(1,300)
lado = 40
while True:
    ventana.fill(coloFondo)
    pygame.draw.rect(ventana, colorFiguras, (posX,posY,lado,lado))
    #movimiento con el raton 
    posX, posY = pygame.mouse.get_pos()
    posX = posX- (lado/2)
    posY = posY-(lado/2)
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit
    pygame.display.update()
