import pygame
import sys



pygame.init()
#Ventana lol


Ancho = 600
Alto = 600

VENTANA = pygame.display.set_mode((Ancho,Alto))
icon=pygame.image.load("imagenes/el-cavi.png")
pygame.display.set_icon(icon)
pygame.display.set_caption('El cavi juego')

#Fokin fondo
background=pygame.image.load("imagenes/dlone.png")
VENTANA.blit(background,(0,0))

#Sprites

class Jugador(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(("imagenes/nave.png"))
        self.rect = self.image.get_rect()
        self.rect.center = (Ancho // 2, Alto // 2)



#Grupo sprites

jugador = Jugador()
sprites = pygame.sprite.Group()
sprites.add(jugador) 

#Refresh sprites

sprites.update()
sprites.draw(VENTANA)



def update(self):
    self.rect.x -=10
    if self.rect.right < 0:
        self.rect.left = Ancho


#Velocidad default
    self.velocidad_x = 0
#Teclas
teclas = pygame.key.get_pressed()

if teclas[pygame.K_a]:
    self.velocidad_x = -10

#Refresh
pygame.display.update()
#Bucle
terminado = False
while not terminado:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
            