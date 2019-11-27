import pygame
import mapaController
import spriteLoader as tiles
import random
import time
import os
import sys


class Player:
    def __init__(self):
        self.xp = 0
        self.nivel = 1
        self.sprite_atual = tiles.playerDict[pygame.K_s]
        # 24, 35 (final em cima)
        # 25, 34 (final esquerda)
        self.pos = (1, 1)
        self.maxHP = 100
        self.status = Stats(self.maxHP, 10, 10, 10, 10, 10)
        self.potions = 0
        self.weapon = Stats(0, 0, 0, 0, 0, 0)
        self.armor = Stats(0, 0, 0, 0, 0, 0)

    def adicionaXP(self, quantidade):
        self.xp += quantidade
        if(self.xp % 100 >= 1):
            while (self.xp > 100):
                if(self.xp % 100 >= 1):
                    self.nivel += 1
                    self.xp -= 100
                    self.maxHP += 50
                    self.status.vida = self.maxHP
                    self.status.acuracia += random.randint(0, 10) + self.nivel
                    self.status.critico += random.randint(0, 10) + self.nivel
                    self.status.defesa += random.randint(0, 10) + self.nivel
                    self.status.destreza += random.randint(0, 10) + self.nivel
                    self.status.forca += random.randint(0, 10) + self.nivel

    def mostraStats(self):
        textXP = basicfont.render(
            'XP: ' + str(self.xp), True, (0, 0, 0), (255, 255, 255))
        txtLVL = basicfont.render(
            'Nível: ' + str(self.nivel), True, (0, 0, 0), (255, 255, 255))
        txtArmorHP = " +" + str(self.armor.vida)
        txtWeaponHP = " +" + str(self.weapon.vida)
        txtHP = basicfont.render(
            'Vida: ' + str(self.status.vida) + txtArmorHP + txtWeaponHP, True, (0, 0, 0), (255, 255, 255))
        txtArmorF = " +" + str(self.armor.forca)
        txtWeaponF = " +" + str(self.weapon.forca)
        txtForca = basicfont.render(
            'Força: ' + str(self.status.forca) + txtArmorF + txtWeaponF, True, (0, 0, 0), (255, 255, 255))
        txtArmorD = " +" + str(self.armor.defesa)
        txtWeaponD = " +" + str(self.weapon.defesa)
        txtDefesa = basicfont.render(
            'Defesa: ' + str(self.status.defesa) + txtArmorD + txtWeaponD, True, (0, 0, 0), (255, 255, 255))
        txtArmorA = " +" + str(self.armor.acuracia)
        txtWeaponA = " +" + str(self.weapon.acuracia)
        txtAcura = basicfont.render(
            'Acurácia: ' + str(self.status.acuracia) + txtArmorA + txtWeaponA, True, (0, 0, 0), (255, 255, 255))
        txtArmorH = " +" + str(self.armor.destreza)
        txtWeaponH = " +" + str(self.weapon.destreza)
        txtDex = basicfont.render(
            'Destreza: ' + str(self.status.destreza) + txtArmorH + txtWeaponH, True, (0, 0, 0), (255, 255, 255))
        txtArmorC = " +" + str(self.armor.critico)
        txtWeaponC = " +" + str(self.weapon.critico)
        txtCrit = basicfont.render(
            'Crítico: ' + str(self.status.critico) + txtArmorC + txtWeaponC, True, (0, 0, 0), (255, 255, 255))
        textP = basicfont.render(
            'Poções: ' + str(self.potions), True, (0, 0, 0), (255, 255, 255))
        #  forca, critico, destreza, acuracia, defesa
        screen.blit(txtLVL, (5, 5))
        screen.blit(textXP, (100, 5))
        screen.blit(txtHP, (200, 5))
        screen.blit(txtForca, (650, 450))
        screen.blit(txtCrit, (650, 475))
        screen.blit(txtDex, (650, 500))
        screen.blit(txtDefesa, (650, 525))
        screen.blit(txtAcura, (650, 550))
        screen.blit(textP, (650, 575))

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


class Bau:
    def __init__(self, i, j):
        self.pos = (i, j)
        self.potions = 0
        self.arma = None
        self.armadura = None

    def printaBau(self, mapa, player):
        keyPress = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    keyPress = event.key

            text1 = basicfont.render(
                'Baú achado!', True, (0, 0, 0), (255, 255, 255))
            string = None
            if(self.arma):
                # vida, forca, critico, destreza, acuracia, defesa
                string = "Arma: +{} +{} +{} +{} +{} +{}".format(
                    self.arma.vida, self.arma.forca, self.arma.critico, self.arma.destreza, self.arma.acuracia, self.arma.defesa)
            else:
                string = "Armadura: +{} +{} +{} +{} +{} +{}".format(
                    self.armadura.vida, self.armadura.forca, self.armadura.critico, self.armadura.destreza, self.armadura.acuracia, self.armadura.defesa)
            text2 = basicfont.render(
                'C - Pegar itens', True, (0, 0, 0), (255, 255, 255))
            text3 = basicfont.render(
                'X - Deixar para depois...', True, (0, 0, 0), (255, 255, 255))
            conteudo = basicfont.render(
                string, True, (0, 0, 0), (255, 255, 255))
            pocoes = basicfont.render(
                "E " + str(self.potions) + " poções", True, (0, 0, 0), (255, 255, 255))

            screen.blit(text1, (10, 475))
            screen.blit(conteudo, (10, 500))
            screen.blit(pocoes, (10, 525))
            screen.blit(text2, (10, 550))
            screen.blit(text3, (10, 575))
            pygame.display.update()

            if(keyPress == pygame.K_c):
                mapa.matriz[self.pos[0]][self.pos[1]] = "0"
                if(self.arma):
                    player.weapon = self.arma
                else:
                    player.armor = self.armadura
                player.potions += self.potions
                return
            if(keyPress == pygame.K_x):
                return


class Mapa:
    def __init__(self, mapa):
        self.matriz = mapa
        self.fog = None
        self.level = 1
        self.baus = []

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
        text1 = basicfont.render(
            'Profundidade: ' + str(self.level), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text1, (975, 450))

    def contaBaus(self):
        qtdeBaus = 0
        for pos in self.matriz:
            if pos == "B":
                qtdeBaus += 1
        return qtdeBaus

    def geraItens(self, nivel, mapa):
        for i in range(0, len(self.matriz)):
            for j in range(0, len(self.matriz[i])):
                if(self.matriz[i][j] == "B"):
                    bau = Bau(i, j)
                    bau.potions = random.randint(1, 3*nivel)
                    self.vida = random.randint(5, 10*nivel)
                    self.forca = random.randint(5, 10*nivel)
                    self.critico = random.randint(5, 10*nivel)
                    self.destreza = random.randint(5, 10*nivel)
                    self.acuracia = random.randint(5, 10*nivel)
                    self.defesa = random.randint(5, 10*nivel)
                    self.status = Stats(self.vida, self.forca, self.critico,
                                        self.destreza, self.acuracia, self.defesa)
                    if(random.randint(1, 2) == 2):
                        bau.arma = self.status
                    else:
                        bau.armadura = self.status
                    mapa.baus.append(bau)

        # ao chegar num baú, executa essa função de gerar os itens
        # guarda a posição desse baú, ao executar, verifica se já existe
        # se não existir, gera mais itens
        # itens baseados no nível


class Stats:
    def __init__(self, vida, forca, critico, destreza, acuracia, defesa):
        self.vida = vida
        self.forca = forca
        self.critico = critico
        self.destreza = destreza
        self.acuracia = acuracia
        self.defesa = defesa


class Inimigo:
    def __init__(self, level, player):
        self.nivel = 1
        if(player.nivel > 0):
            self.nivel = player.nivel
        self.vida = random.randint(50, 90*level*self.nivel)
        forca = random.randint(8, 14*level*self.nivel)
        defesa = random.randint(8, 14*level*self.nivel)
        critico = random.randint(8, 14*level*self.nivel)
        destreza = random.randint(8, 14*level*self.nivel)
        acuracia = random.randint(8, 14*level*self.nivel)
        self.status = Stats(self.vida, forca, critico,
                            destreza, acuracia, defesa)


def printaControles():
    text1 = basicfont.render('W - Cima', True, (0, 0, 0), (255, 255, 255))
    text4 = basicfont.render('D - Direita', True, (0, 0, 0), (255, 255, 255))
    text2 = basicfont.render('S - Baixo', True, (0, 0, 0), (255, 255, 255))
    text3 = basicfont.render('A - Esquerda', True, (0, 0, 0), (255, 255, 255))

    screen.blit(text1, (875, 450))
    screen.blit(text2, (875, 475))
    screen.blit(text3, (875, 500))
    screen.blit(text4, (875, 525))


def batalhar(player, mapa):
    done = False
    keyPress = None

    inimigo = Inimigo(mapa.level, player)

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                keyPress = event.key

        screen.fill((255, 255, 255))  # fundo da tela
        screen.blit(tiles.modoDict['I'], (0, 0))
        printaControles()
        mapa.printMap()
        player.desenhaPlayer()
        player.mostraStats()

        text5 = basicfont.render(
            'Vida do Inimigo: ' + str(inimigo.status.vida), True, (0, 0, 0), (255, 255, 255))
        text6 = basicfont.render(
            'Força do Inimigo: ' + str(inimigo.status.forca), True, (0, 0, 0), (255, 255, 255))
        text7 = basicfont.render(
            'Defesa do Inimigo: ' + str(inimigo.status.defesa), True, (0, 0, 0), (255, 255, 255))

        screen.blit(text5, (10, 475))
        screen.blit(text6, (10, 500))
        screen.blit(text7, (10, 525))
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

        # se fugir
        if(keyPress == pygame.K_f):
            fugir = random.randint(0, player.status.destreza)
            if(fugir >= inimigo.status.destreza):
                text5 = basicfont.render(
                    'Você fugiu!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text5, (200, 200))
                return

            else:
                text5 = basicfont.render(
                    'Você não conseguiu fugir!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text5, (200, 150))

                dano_inimigo = ataquecritico(inimigo)

                if(random.randint(1, player.status.destreza) <= inimigo.status.acuracia):
                    player.status.vida = player.status.vida - dano_inimigo
                    text9 = basicfont.render(
                        'Dano de ' + str(dano_inimigo) + ' em você!', True, (0, 0, 0), (255, 255, 255))
                    screen.blit(text9, (10, 575))

                if (player.status.vida <= 0):
                    text10 = basicfont.render(
                        'Você morreu!', True, (0, 0, 0), (255, 255, 255))
                    screen.blit(text10, (200, 200))
                    player.mostraStats()
                    pygame.display.update()
                    time.sleep(0.5)
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                    return
            pygame.display.update()
            time.sleep(0.5)

        if(keyPress == pygame.K_b):
            dano = ataquecritico(player)

            text8 = basicfont.render(
                'Dano de ' + str(dano) + ' no inimigo!', True, (0, 0, 0), (255, 255, 255))
            screen.blit(text8, (10, 600))
            if(random.randint(1, inimigo.status.destreza) <= player.status.acuracia):
                inimigo.status.vida = inimigo.status.vida - dano
            else:
                text8 = basicfont.render(
                    'Você errou o ataque no inimigo!', True, (0, 0, 0), (255, 255, 255))
            screen.blit(text8, (10, 600))
            if (inimigo.status.vida < 0):
                text10 = basicfont.render(
                    'Você derrotou o inimigo!', True, (0, 0, 0), (255, 255, 255))
                player.adicionaXP(random.randint(
                    50, inimigo.vida if inimigo.vida > 50 else 100))
                screen.blit(text10, (200, 200))
                pygame.display.update()
                time.sleep(0.5)
                return

            dano_inimigo = ataquecritico(inimigo)

            if(random.randint(1, player.status.destreza) <= inimigo.status.acuracia):
                player.status.vida = player.status.vida - dano_inimigo
                text9 = basicfont.render(
                    'Dano de ' + str(dano_inimigo) + ' em você!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text9, (10, 575))
            else:
                text9 = basicfont.render(
                    'Inimigo erra ataque em você!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text9, (10, 575))

            if (player.status.vida <= 0):
                text10 = basicfont.render(
                    'Você morreu!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text10, (200, 200))
                player.mostraStats()
                pygame.display.update()
                time.sleep(0.5)
                # player.pos = (1, 1)
                # player.maxHP = 100
                # player.weapon = Stats(0, 0, 0, 0, 0, 0)
                # player.armor = Stats(0, 0, 0, 0, 0, 0)
                # player.xp = 0
                # player.status = Stats(100, 10, 10, 10, 10, 10)
                # mapaController.gera()
                # (map_bits) = mapaController.carregaMap("mapa.txt")
                # mapa.geraItens(player.nivel, mapa)
                # mapa.matriz = (map_bits)
                python = sys.executable
                os.execl(python, python, *sys.argv)
                return
            pygame.display.update()
            time.sleep(0.5)

        # se tomar poção
        if(keyPress == pygame.K_p):
            if (player.potions == 0):
                text11 = basicfont.render(
                    'Você não tem poções!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text11, (200, 200))
            elif (player.maxHP == player.status.vida):
                text11 = basicfont.render(
                    'Você está com a vida cheia!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text11, (200, 200))
            else:
                player.status.vida += 50*player.nivel
                player.potions -= 1
                if(player.status.vida > player.maxHP):
                    player.status.vida = player.maxHP

                dano_inimigo = ataquecritico(inimigo)

                if(random.randint(1, player.status.destreza) <= inimigo.status.acuracia):
                    player.status.vida -= dano_inimigo
                    text9 = basicfont.render(
                        'Dano de ' + str(dano_inimigo) + ' em você!', True, (0, 0, 0), (255, 255, 255))
                    screen.blit(text9, (10, 575))
                else:
                    text9 = basicfont.render(
                        'Inimigo erra ataque em você!', True, (0, 0, 0), (255, 255, 255))
                    screen.blit(text9, (10, 575))

                if (player.status.vida <= 0):
                    text10 = basicfont.render(
                        'Você morreu!', True, (0, 0, 0), (255, 255, 255))
                    screen.blit(text10, (200, 200))
                    player.mostraStats()
                    pygame.display.update()
                    time.sleep(0.5)
                    # player.pos = (1, 1)
                    # player.maxHP = 100
                    # player.nivel = 0
                    # player.weapon = Stats(0, 0, 0, 0, 0, 0)
                    # player.armor = Stats(0, 0, 0, 0, 0, 0)
                    # player.xp = 0
                    # player.status = Stats(100, 10, 10, 10, 10, 10)
                    # mapaController.gera()
                    # (map_bits) = mapaController.carregaMap("mapa.txt")
                    # mapa.geraItens(player.nivel, mapa)
                    # mapa.matriz = (map_bits)
                    python = sys.executable
                    os.execl(python, python, *sys.argv)
                    return

            pygame.display.update()
            time.sleep(0.5)

        player.mostraStats()
        keyPress = None
        pygame.display.update()
        clock.tick(100)


def ataquecritico(personagem):
    critico = random.randint(0, personagem.status.critico)
    if(critico == personagem.status.critico):
        ataque = personagem.status.forca * 2
    else:
        ataque = personagem.status.forca
    return ataque


if __name__ == '__main__':
    pygame.init()
    screen = pygame.display.set_mode((1235, 625))
    clock = pygame.time.Clock()
    done = False
    mapaController.gera()
    (map_bits) = mapaController.carregaMap("mapa.txt")
    mapa = Mapa(map_bits)
    player = Player()
    mapa.geraItens(player.nivel, mapa)
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
        posAntes = player.pos
        screen.blit(tiles.modoDict[' '], (0, 0))
        player.mostraStats()
        player.desenhaPlayer()
        if(mapa.matriz[player.pos[0]][player.pos[1]] == "B"):
            screen.blit(tiles.modoDict['B'], (0, 0))
            for conteudo in mapa.baus:
                if(conteudo.pos == player.pos):
                    conteudo.printaBau(mapa, player)

        if(mapa.matriz[player.pos[0]][player.pos[1]] == "S"):
            player.pos = (1, 1)
            mapaController.gera()
            (map_bits) = mapaController.carregaMap("mapa.txt")
            mapa = Mapa(map_bits)
            mapa.level += 1
            mapa.geraItens(player.nivel, mapa)

        player.andar(keyPress, mapa.matriz)
        keyPress = None
        posDepois = player.pos
        posicao = mapa.matriz[player.pos[0]][player.pos[1]]
        if(posAntes != posDepois and posicao != "S" and posicao != "B"):
            batalha = random.randint(0, 10)
            if(batalha == 10):
                batalhar(player, mapa)
        pygame.display.update()
        clock.tick(60)
