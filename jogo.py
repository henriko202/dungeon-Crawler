import pygame
import mapaController
import spriteLoader as tiles
import random


class Player:
    def __init__(self):
        self.xp = 0
        self.nivel = 0
        self.sprite_atual = tiles.playerDict[pygame.K_s]
        self.pos = (1, 1)

    def mostraStats(self):
        textf = basicfont.render(
            'Força:     11', True, (0, 0, 0), (255, 255, 255))
        textd = basicfont.render(
            'Defesa:    21', True, (0, 0, 0), (255, 255, 255))
        texta = basicfont.render(
            'Acurácia:  5', True, (0, 0, 0), (255, 255, 255))
        texth = basicfont.render(
            'Destreza:  1', True, (0, 0, 0), (255, 255, 255))
        textc = basicfont.render(
            'Crítico:   3', True, (0, 0, 0), (255, 255, 255))

        screen.blit(textf, (650, 475))
        screen.blit(textd, (650, 500))
        screen.blit(texta, (650, 525))
        screen.blit(texth, (650, 550))
        screen.blit(textc, (650, 575))

    def andar(self, direcao, mapa):
        x = self.pos[0]
        y = self.pos[1]
        pos = (x, y)

        if direcao == pygame.K_w:
            pos = (x - 1, y)
            self.sprite_atual = tiles.playerDict[direcao]

        if direcao == pygame.K_a:
            pos = (x, y - 1)
            self.sprite_atual = tiles.playerDict[direcao]

        if direcao == pygame.K_s:
            pos = (x + 1, y)
            self.sprite_atual = tiles.playerDict[direcao]

        if direcao == pygame.K_d:
            pos = (x, y + 1)
            self.sprite_atual = tiles.playerDict[direcao]

        if(mapa[pos[0]][pos[1]] != "1"):
            self.pos = pos

    def desenhaPlayer(self):
        screen.blit(self.sprite_atual,
                    (640+self.pos[1]*16, self.pos[0]*16))


class Mapa:
    def __init__(self, mapa):
        self.matriz = mapa
        self.fog = None

    def printMap(self):
        for i in range(0, len(self.matriz)):
            for j in range(0, len(self.matriz[i])):
                screen.blit(
                    tiles.mapDict["0"], (640+j*16, i*16))
                if(self.matriz[i][j] == "E" or "S"):
                    screen.blit(
                        tiles.mapDict[self.matriz[i][j]], (640+j*16, i*16))
                else:
                    screen.blit(
                        tiles.mapDict[self.matriz[i][j]], (640+j*16, i*16))


class Stats:
    def __init__(self, lf, pw, cr, ds, ac, de):
        self.vida = lf
        self.power = pw
        self.critico = cr
        self.destreza = ds
        self.acuracia = ac
        self.defesa = de


def printaControles():
    text1 = basicfont.render('W - Cima', True, (0, 0, 0), (255, 255, 255))
    text4 = basicfont.render('D - Direita', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('S - Baixo', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('A - Esquerda', True, (0, 0, 0), (255, 255, 255))

    screen.blit(text1, (50, 475))
    screen.blit(text2, (50, 500))
    screen.blit(text3, (50, 525))
    screen.blit(text4, (50, 550))


def printaBau():
    # baút
    text1 = basicfont.render(
        'Baú achado!', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render(
        'C - Pegar itens', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render(
        'X - Deixar para depois...', True, (0, 0, 0), (255, 255, 255))

    screen.blit(text1, (200, 475))
    screen.blit(text2, (200, 500))
    screen.blit(text3, (200, 525))


def batalhar():
    done = False
    keyPress = None

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                keyPress = event.key

        screen.blit(tiles.modoDict['I'], (0, 0))
        text1 = basicfont.render(
            'É hora do du-du-du-duelo!', True, (0, 0, 0), (255, 255, 255))
        text2 = basicfont.render(
            'B - Atacar', True, (0, 0, 0), (255, 255, 255))
        text3 = basicfont.render(
            'P - Tomar uma poção', True, (0, 0, 0), (255, 255, 255))
        text4 = basicfont.render(
            'F - fujir', True, (0, 0, 0), (255, 255, 255))

        screen.blit(text1, (200, 475))
        screen.blit(text2, (200, 500))
        screen.blit(text3, (200, 525))
        screen.blit(text4, (200, 550))
        if(keyPress == pygame.K_f):
            return
        if(keyPress == pygame.K_b):
            return
        if(keyPress == pygame.K_p):
            return
        keyPress = None
        pygame.display.update()
        clock.tick(100)


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1280, 640))
    clock = pygame.time.Clock()
    done = False
    mapaController.gera()
    (map_bits) = mapaController.carregaMap("mapa.txt")
    mapa = Mapa(map_bits)
    player = Player()
    basicfont = pygame.font.SysFont(None, 25)
    keyPress = None
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                keyPress = event.key

        screen.fill((255, 255, 255))  # fundo da tela
        printaControles()
        mapa.printMap()
        player.mostraStats()
        posAntes = player.pos
        screen.blit(tiles.modoDict[' '], (0, 0))

        if(mapa.matriz[player.pos[0]][player.pos[1]] == "B"):
            screen.blit(tiles.modoDict['B'], (0, 0))
            printaBau()
        if(mapa.matriz[player.pos[0]][player.pos[1]] == "S"):
            player.pos = (1, 1)
            mapaController.gera()
            (map_bits) = mapaController.carregaMap("mapa.txt")
            mapa = Mapa(map_bits)

        player.andar(keyPress, mapa.matriz)
        player.desenhaPlayer()
        keyPress = None
        posDepois = player.pos
        posicao = mapa.matriz[player.pos[0]][player.pos[1]]
        if(posAntes != posDepois and posicao != "S" and posicao != "B"):
            batalha = random.randint(0, 69)
            if(batalha == 69):
                batalhar()
        pygame.display.update()
        clock.tick(60)
