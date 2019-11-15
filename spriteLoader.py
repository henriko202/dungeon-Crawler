import pygame
# pylint: disable=no-member
# pylint: disable-msg=too-many-function-args
playerDict = {
    pygame.K_s: pygame.image.load('tileset/personagem.png'),
    pygame.K_w: pygame.image.load('tileset/personagem.png'),
    pygame.K_a: pygame.image.load('tileset/personagem.png'),
    pygame.K_d: pygame.image.load('tileset/personagem.png'),
}
mapDict = {
    'B': pygame.image.load('tileset/chest/chest_full_open_anim_f2.png'),
    '1': pygame.image.load('tileset/wall/wall_mid.png'),
    '0': pygame.image.load('tileset/floor/floor_1.png'),
    'S': pygame.image.load('tileset/floor/floor_ladder.png'),
    'E': pygame.image.load('tileset/floor/floor_2.png'),
}
modoDict = {
    ' ': pygame.image.load('./tileset/corredor.png'),
    'B': pygame.image.load('./tileset/corredorBau.png'),
    'I': pygame.image.load('./tileset/corredorInimigo.png'),
}