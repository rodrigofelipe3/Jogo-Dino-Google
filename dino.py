import pygame
from pygame.locals import *
from sys import exit
import os
from random import randrange

diretorio_principal = os.path.dirname(__file__)
diretorio_imagens = os.path.join(diretorio_principal, "imagens")
diretorio_sons = os.path.join(diretorio_principal, "sons")

pygame.init()

'''DEFININDO O CLOCK DO JOGO'''
clock = pygame.time.Clock()
largura = 640
altura = 480

BRANCO = (255, 255, 255)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Dino")


sprite_sheet = pygame.image.load(os.path.join(diretorio_imagens, "dinoSpritesheet.png")).convert_alpha()

class Dino(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imagens_dinossauros = []
        for i in range (3):         
            img = sprite_sheet.subsurface((i*32,0), (32, 32))
            img = pygame.transform.scale(img, (32*3, 32*3))
            self.imagens_dinossauros.append(img)
        self.index_lista = 0
        self.image = self.imagens_dinossauros[self.index_lista]
        self.rect = self.image.get_rect()
        self.rect.center = (100, altura-90)

    def update(self):
        if self.index_lista > 2:
            self.index_lista = 0
        self.index_lista += 0.25
        self.image = self.imagens_dinossauros[int(self.index_lista)]

class Nuvens(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = sprite_sheet.subsurface((7*32,0), ( 32,32))
        self.image = pygame.transform.scale(self.image, (32*3, 32*3))
        self.rect = self.image.get_rect()
        self.rect.y = randrange(50, 200, 50)
        self.rect.x = largura - randrange(30, 300, 90)
    def update(self):
        if self.rect.topright[0] < 0:
            self.rect.x = largura
        self.rect.x -= 10



dino = Dino()

todas_as_sprites = pygame.sprite.Group()
todas_as_sprites.add(dino)

for i in range (4):
    nuvens = Nuvens()
    todas_as_sprites.add(nuvens)

while True:
    clock.tick(60)
    tela.fill(BRANCO)
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()
