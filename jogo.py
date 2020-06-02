import pygame
from random import randint as rd
pygame.init()
janela = pygame.display.set_mode((450,480))#457
fonte = pygame.font.SysFont('calibri', 30)
pygame.display.set_caption("jogo da velha")
clock = pygame.time.Clock()
tamanho = 20
fundo = pygame.image.load("jogo da velha.png")
x_img = pygame.image.load('x.png')
x_mov = [41,366]
x_pto = 0
o_img = pygame.image.load('o.png')
o_mov = [340,225]
o_pto = 0
coord = {'x':(41, 190, 347),
         'y':(70, 220, 366)}
tab = [   0,      0,       0,       0,        0,       0,      0,        0,        0]
pos = [[coord['x'][0],coord['y'][0]],  [coord['x'][1],coord['y'][0]],  [coord['x'][2],coord['y'][0]],
       [coord['x'][0],coord['y'][1]],  [coord['x'][1],coord['y'][1]],  [coord['x'][2],coord['y'][1]],
       [coord['x'][0],coord['y'][2]],  [coord['x'][1],coord['y'][2]],  [coord['x'][2],coord['y'][2]]]

#   0        1         2
#  41,70   190,70    347,70
#   3        4         5
# 41,220  190,220   347,220
#   6        7         8
# 41,366  190,366   347,366
win = [[2, 4, 6],[0, 4, 8],[6, 7, 8],[3, 4, 5], [0, 1 , 2], [0 , 3, 6], [1, 4, 7], [2, 5, 8]]
vez = ['x', 'o'][rd(0,1)]# vez quem começa
jogador = 0
ganhador = False
zero_count = 0
pl=[0,0]
tela = True
while True:
    teclado = pygame.key.get_pressed()
    if tela:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                break

        if teclado[pygame.K_1]:
            if tab[0] == 0:
                tab[0] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_2]:
            if tab[1] == 0:
                tab[1] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_3]:
            if tab[2] == 0:
                tab[2] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_4]:
            if tab[3] == 0:
                tab[3] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_5]:
            if tab[4] == 0:
                tab[4] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_6]:
            if tab[5] == 0:
                tab[5] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_7]:
            if tab[6] == 0:
                tab[6] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_8]:
            if tab[7] == 0:
                tab[7] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'
        if teclado[pygame.K_9]:
            if tab[8] == 0:
                tab[8] = vez
                if vez == 'x':
                    vez = 'o'
                else:
                    vez = 'x'

        comando = pygame.key.get_pressed()
        if comando[pygame.K_d]:
            pl[0] += 1
        if comando[pygame.K_a]:
            pl[0] -= 1
        if comando[pygame.K_s]:
            pl[1] += 1
        if comando[pygame.K_w]:
            pl[1] -= 1

        for c in win:
            if tab[c[0]] == tab[c[1]] == tab[c[2]] and tab[c[0]] != 0 and tab[c[1]] != 0 and tab[c[2]] != 0:
                winner = tab[c[0]]
                exec(f'{tab[c[0]]}_pto += 1')
                print(f'Ganhador: {winner}', pl)
                tab = [0,0,0,0,0,0,0,0,0]
                tela = False


        for c in range(len(tab)):
            if tab[c] == 0:
                pass
            if tab[c] == 'x':
                janela.blit(x_img, pos[c])
            if tab[c] == 'o':
                janela.blit(o_img, pos[c])

        placar = fonte.render(f'X: {x_pto}      O: {o_pto}', False, (255,255,255))
        janela.blit(placar, (149, 0))
        janela.blit(fundo,(0,23))
        pygame.display.update()
        janela.fill((0,0,0))
        clock.tick(50)
    else:
        if teclado[pygame.K_0]:
            tela = True
        placar = fonte.render(f'Para continuar pressione Q', False, (255,255,255))
        janela.blit(placar, (50, 230))
        pygame.display.update()
        janela.fill((0,0,0))
        clock.tick(50)
