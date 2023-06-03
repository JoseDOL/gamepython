import pygame,sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((700,500))
pygame.display.set_caption("Titulo Ventana")
coloFondo = (118,119,118)
colorFiguras = (205,0,155)
#carga de imagenes
imagen = pygame.image.load("imagenes/pygame.png")
#posiciones
posX, posY = (10,40)
while True:
    ventana.fill(coloFondo)
    #ventana.blit(imagen,(posX,posY))
    for i in range(5):
        posX, posY = randint(1,700), randint(1,500)
        pygame.draw.rect(ventana,colorFiguras, (posX,posY,50,80))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit
    pygame.display.update()
