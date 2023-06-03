import pygame,sys
from pygame.locals import *

pygame.init()
ventana = pygame.display.set_mode((800,800))
pygame.display.set_caption("Titulo Ventana")
#colores
coloFondo = (118,119,118)
colorLinea = (255,0,0)
colorCirculo = (255,128,0)
colorFiguras = (205,0,155)

while True:
    ventana.fill(coloFondo)
    #lineas
    pygame.draw.line(ventana,colorLinea,(60,90),(200,100),40)
    pygame.draw.line(ventana,colorLinea,(80,190),(100,150),20)
    pygame.draw.line(ventana,colorLinea,(10,30),(250,190),40)
    #circulos
    pygame.draw.circle(ventana, colorCirculo,(450,100),100,30)
    pygame.draw.circle(ventana, colorCirculo,(590,250),40,20)
    #figras
    pygame.draw.rect(ventana, colorFiguras,(100,200,120,250))
    pygame.draw.polygon(ventana,colorFiguras,((400,400),(500,400),(500,500),(400,500)))
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit
        pygame.display.update()
