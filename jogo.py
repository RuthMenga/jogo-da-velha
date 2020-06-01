import pygame
from random import randint as rd
pygame.init()
janela = pygame.display.set_mode((450,480))#457
pygame.display.set_caption("jogo da velha")
clock = pygame.time.Clock()
tamanho = 20
fundo = pygame.image.load("jogo da velha.png")
x_img = pygame.image.load('x.png')
x_mov = [41,366]
o_img = pygame.image.load('o.png')
o_mov = [340,225]
tab = [0, 0, 0, 0, 0, 0, 0, 0, 0]
pos = [[86,41],[86,190],[86,340],[225,41],[225,190],[225,340],[366,41],[357,190],[357,340]]
#coordenadas = {'x':[41, 190, 340], 'y':[86, 225, 366]}
#   0        1         2
#  86,41   86,190    86,340
#   3        4         5
# 225,41  225,190   225,340
#   6        7         8
# 366,41  357,190   357,340
lista = [[2, 4, 6],[0, 4, 8],[6, 7, 8],[3, 4, 5], [0, 1 , 2], [0 , 3, 6], [1, 4, 7], [2, 5, 8]]
vez = ['x', 'o'][rd(0,1)]# vez quem começa

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            break
    teclado = pygame.key.get_pressed()
    if teclado[pygame.K_1]:
        tab[0] = vez

    for c in range(len(tab)):
        if tab[c] == 0:
            pass
        if tab[c] == 'x':
            janela.blit(x_img, pos[c])
        if tab[c] == 'o':
            janela.blit(o_img, pos[c])

    janela.fill((0,0,0))
    janela.blit(fundo,(0,23))
    pygame.display.update()
    clock.tick(50)
    print(x_mov)

for i in range(3):
    for j in range(3):
        font = pygame.font.SysFont("comicsans, 100")

        x = j * tamanho
        y = i * tamanho

        text = font.render('image[i][j]', (120,0,0))
        janela.blit(text, ((x + 75), (y + 75)))

def redraw_window(win):
    win.fill((255, 255, 255))
# comando = pygame.key.get_pressed()
    # if comando[pygame.K_d]:
    #     x_mov[0] += 1
    # if comando[pygame.K_a]:
    #     x_mov[0] -= 1
    # if comando[pygame.K_w]:
    #     x_mov[1] += 1
    # if comando[pygame.K_s]:
    #     x_mov[1] -= 1

jogador = 0
ganhador = verificaGanhador(janela)