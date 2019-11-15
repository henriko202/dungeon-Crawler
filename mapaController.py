from random import shuffle, randrange
import random


def geraMapa(w=16, h=8):
    vis = [[0] * w + [1] for _ in range(h)] + [[1] * (w + 1)]
    ver = [["10"] * w + ['1'] for _ in range(h)] + [[]]
    hor = [["11"] * w + ['1'] for _ in range(h + 1)]

    def walk(x, y):
        vis[y][x] = 1

        d = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        shuffle(d)
        for (xx, yy) in d:
            if vis[yy][xx]:
                continue
            if xx == x:
                hor[max(y, yy)][x] = "10"
            if yy == y:
                ver[y][max(x, xx)] = "00"
            walk(xx, yy)

    walk(randrange(w), randrange(h))

    s = ""
    for (a, b) in zip(hor, ver):
        s += ''.join(a + ['\n'] + b + ['\n'])
    return s


def carregaMap(arq):
    mapa = list()
    arquivo = open(arq, 'r')
    for i in arquivo.readlines():
        linha = list()
        caracteres = i.split('\n')

        for j in caracteres[0]:
            linha.append(j)
        mapa.append(linha.copy())
        linha.clear()
    arquivo.close()

    return (mapa)


def gera():
    arq = open("mapa.txt", "w+")
    mapa = geraMapa(18,13)
    i = j = baus = 0
    for char in mapa:
        j += 1
        if(char == "\n"):
            i += 1
            j = 0
        if(i == 1 and j == 2):
            char = "E"
        if(i == 25 and j == 36):
            char = "S"
        if(char == "0"):
            if(random.randint(0, 100) == 0 and baus <= 2):
                baus += 1
                char = "B"
        arq.write(char)

    arq.close()

if __name__ == '__main__':
    arq = open("mapa.txt", "w+")
    mapa = geraMapa(18,13)
    i = j = baus = 0
    for char in mapa:
        j += 1
        if(char == "\n"):
            i += 1
            j = 0
        if(i == 1 and j == 2):
            char = "E"
        if(i == 25 and j == 36):
            char = "S"
        if(char == "0"):
            if(random.randint(0, 100) == 0 and baus <= 2):
                baus += 1
                char = "B"
        arq.write(char)

    arq.close()
