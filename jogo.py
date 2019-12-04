import pygame
import mapaController
import cheater
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
        if(quantidade >= 100):
            self.xp += 101
        else:
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
        textStatus = basicfont.render(
            'Status +Armadura +Arma', True, (0, 0, 0), (255, 255, 255))
        screen.blit(txtLVL, (5, 5))
        screen.blit(textXP, (100, 5))
        screen.blit(txtHP, (200, 5))
        screen.blit(textStatus, (650, 450))
        screen.blit(txtForca, (650, 475))
        screen.blit(txtCrit, (650, 500))
        screen.blit(txtDex, (650, 525))
        screen.blit(txtDefesa, (650, 550))
        screen.blit(txtAcura, (650, 575))
        screen.blit(textP, (650, 600))

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
        teclaApertada = None
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                elif event.type == pygame.KEYDOWN:
                    teclaApertada = event.key

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

            if(teclaApertada == pygame.K_c):
                verify = False
                mapa.matriz[self.pos[0]][self.pos[1]] = "0"
                if(self.arma):
                    player.weapon = self.arma
                else:
                    player.armor = self.armadura
                player.potions += self.potions
                return
            if(teclaApertada == pygame.K_x):
                return False


class Mapa:
    def __init__(self, mapa):
        self.matriz = mapa
        self.fog = mapaController.carregaMap("mapa.txt")
        self.level = 1
        self.baus = []

    def iniciaFog(self):
        fog = self.fog
        for i in range(0, len(fog)):
            for j in range(0, len(fog[i])):
                fog[i][j] = 0
        self.fog = fog

    def controlaFog(self, player):
        esquerda = player.pos[1] - 3 if player.pos[1] - 3 > 0 else 0
        cima = player.pos[0] - 3 if player.pos[0] - 3 > 0 else 0
        baixo = player.pos[0] + 4 if player.pos[0] + 4 < 27 else 27
        direita = player.pos[1] + 4 if player.pos[1] + 4 < 37 else 37
        for i in range(esquerda, direita):
            for j in range(cima,  baixo):
                self.fog[j][i] = 1
        return

    def printFog(self):
        for i in range(0, len(self.fog)):
            for j in range(0, len(self.fog[i])):
                if(self.fog[i][j] == 0):
                    screen.blit(
                        tiles.mapDict["F"], (640+j*16, i*16))

    def printMap(self):
        for i in range(0, len(self.matriz)):
            for j in range(0, len(self.matriz[i])):
                screen.blit(
                    tiles.mapDict["0"], (640+j*16, i*16))
                screen.blit(
                    tiles.mapDict[self.matriz[i][j]], (640+j*16, i*16))
        text1 = basicfont.render(
            'Profundidade: ' + str(self.level), True, (0, 0, 0), (255, 255, 255))
        screen.blit(text1, (975, 450))

    def printMapCheater(self, matriz):
        for i in range(0, len(matriz)):
            for j in range(0, len(matriz[i])):
                if(matriz[i][j] == -1):
                    screen.blit(
                        tiles.mapDict["1"], (640+j*16, i*16))
                if(matriz[i][j] != -1):
                    screen.blit(
                        tiles.mapDict[self.matriz[i][j]], (640+j*16, i*16))

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
        if(player.nivel > 1):
            self.nivel = int(player.nivel/2)
            if(self.nivel) <= 0:
                self.nivel = 1
        self.vida = random.randint(50, 75*level*self.nivel)
        forca = random.randint(8, 12*level*self.nivel)
        defesa = random.randint(8, 12*level*self.nivel)
        critico = random.randint(8, 12*level*self.nivel)
        destreza = random.randint(8, 12*level*self.nivel)
        acuracia = random.randint(8, 12*level*self.nivel)
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
    terminado = False
    teclaApertada = None

    inimigo = Inimigo(mapa.level, player)

    while not terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            elif event.type == pygame.KEYDOWN:
                teclaApertada = event.key

        screen.fill((255, 255, 255))  # fundo da tela
        screen.blit(tiles.modoDict['I'], (0, 0))
        printaControles()
        mapa.printMap()
        mapa.printFog()
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
        if(teclaApertada == pygame.K_f):
            fugir = random.randint(
                0, player.status.destreza + player.armor.destreza + player.weapon.destreza)
            if(fugir >= inimigo.status.destreza):
                text5 = basicfont.render(
                    'Você fugiu!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text5, (200, 200))
                return

            else:
                text5 = basicfont.render(
                    'Você não conseguiu fugir!', True, (0, 0, 0), (255, 255, 255))
                screen.blit(text5, (200, 150))

                dano_inimigo = ataquecritico_inimigo(inimigo)

                if(random.randint(1, player.status.destreza + player.armor.destreza + player.weapon.destreza) <= inimigo.status.acuracia):
                    player.status.vida = (
                        player.status.vida + player.armor.vida + player.weapon.vida) - dano_inimigo
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

        if(teclaApertada == pygame.K_b):
            dano = ataquecritico_player(player)

            text8 = basicfont.render(
                'Dano de ' + str(dano) + ' no inimigo!', True, (0, 0, 0), (255, 255, 255))
            screen.blit(text8, (10, 600))
            if(random.randint(1, inimigo.status.destreza) <= player.status.acuracia + player.armor.acuracia + player.weapon.acuracia):
                inimigo.status.vida = inimigo.status.vida - dano
            else:
                text8 = basicfont.render(
                    'Você errou o ataque no inimigo!', True, (0, 0, 0), (255, 255, 255))
            screen.blit(text8, (10, 600))
            if (inimigo.status.vida <= 0):
                text10 = basicfont.render(
                    'Você derrotou o inimigo!', True, (0, 0, 0), (255, 255, 255))
                player.adicionaXP(random.randint(
                    50, inimigo.vida if inimigo.vida > 50 and inimigo.vida < 200 else 65))
                screen.blit(text10, (200, 200))
                pygame.display.update()
                time.sleep(0.5)
                return

            dano_inimigo = ataquecritico_inimigo(inimigo)

            if(random.randint(1, player.status.destreza + player.armor.destreza + player.weapon.destreza) <= inimigo.status.acuracia):
                player.status.vida = (
                    player.status.vida + player.armor.vida + player.weapon.vida) - dano_inimigo
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
        if(teclaApertada == pygame.K_p):
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

                dano_inimigo = ataquecritico_inimigo(inimigo)

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
        teclaApertada = None
        pygame.display.update()
        clock.tick(100)


def ataquecritico_player(personagem):
    critico_personagem = personagem.status.critico + \
        personagem.armor.critico + personagem.weapon.critico
    critico = random.randint(0, critico_personagem*2)
    forca = personagem.status.forca + personagem.armor.forca + personagem.weapon.forca
    if(critico >= critico_personagem):
        ataque = forca * 2
    else:
        ataque = forca
    return ataque


def ataquecritico_inimigo(personagem):
    critico = random.randint(0, personagem.status.critico*2)
    if(critico >= personagem.status.critico):
        ataque = personagem.status.forca * 2
    else:
        ataque = personagem.status.forca
    return ataque


if __name__ == '__main__':
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pygame.init()
    pygame.display.set_caption(
        'JogoFDP (First Dungeon Penetration, claramente)')
    screen = pygame.display.set_mode((1235, 625))
    clock = pygame.time.Clock()
    terminado = False
    mapaController.gera()
    (map_bits) = mapaController.carregaMap("mapa.txt")
    mapa = Mapa(map_bits)
    mapa.iniciaFog()
    player = Player()
    mapa.geraItens(player.nivel, mapa)
    basicfont = pygame.font.SysFont(None, 25)
    teclaApertada = None
    cheat = False
    while not terminado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                terminado = True
            elif event.type == pygame.KEYDOWN:
                teclaApertada = event.key
                if event.key == pygame.K_k:
                    cheat = True
            # while key pressed down?
            # if key pressed down?
            # i'm giving up....
                # if event.key == pygame.K_LEFT:        # left arrow turns left
                #     pressed_left = True
                # elif event.key == pygame.K_RIGHT:     # right arrow turns right
                #     pressed_right = True
                # elif event.key == pygame.K_UP:        # up arrow goes up
                #     pressed_up = True
                # elif event.key == pygame.K_DOWN:     # down arrow goes down
                #     pressed_down = True
            elif event.type == pygame.KEYUP:            # check for key releases
                if event.key == pygame.K_k:
                    cheat = False
                # if event.key == pygame.K_LEFT:        # left arrow turns left
                #     pressed_left = False
                # elif event.key == pygame.K_RIGHT:     # right arrow turns right
                #     pressed_right = False
                # elif event.key == pygame.K_UP:        # up arrow goes up
                #     pressed_up = False
                # elif event.key == pygame.K_DOWN:     # down arrow goes down
                #     pressed_down = False

        screen.fill((255, 255, 255))  # fundo da tela
        printaControles()
        mapa.printMap()
        mapa.controlaFog(player)
        mapa.printFog()
        posAntes = player.pos
        screen.blit(tiles.modoDict[' '], (0, 0))
        player.mostraStats()
        player.desenhaPlayer()
        player.andar(teclaApertada, mapa.matriz)
        teclaApertada = None
        depois = True
        posDepois = player.pos

        if(cheat):
            mapa.printMapCheater(cheater.achaSaida(player.pos))
            mapa.printFog()
            player.desenhaPlayer()
            pygame.display.update()

        if(mapa.matriz[player.pos[0]][player.pos[1]] == "S"):
            player.pos = (1, 1)
            mapaController.gera()
            level = mapa.level + 1
            (map_bits) = mapaController.carregaMap("mapa.txt")
            mapa = Mapa(map_bits)
            mapa.level = level
            mapa.geraItens(player.nivel, mapa)
            mapa.iniciaFog()
            mapa.printFog()
            pygame.display.update()

        if(mapa.matriz[player.pos[0]][player.pos[1]] == "B"):
            for conteudo in mapa.baus:
                if(conteudo.pos == player.pos and (posAntes != posDepois) and depois != False):
                    mapa.printFog()
                    pygame.display.update()
                    screen.blit(tiles.modoDict['B'], (0, 0))
                    mapa.printMap()
                    mapa.printFog()
                    player.desenhaPlayer()
                    pygame.display.update()
                    depois = conteudo.printaBau(mapa, player)

        posicao = mapa.matriz[player.pos[0]][player.pos[1]]
        if(posAntes != posDepois and posicao != "S" and posicao != "B"):
            depois = True
            batalha = random.randint(0, 20)
            if(batalha == 20):
                mapa.printFog()
                pygame.display.update()
                batalhar(player, mapa)

        pygame.display.update()
        clock.tick(60)
