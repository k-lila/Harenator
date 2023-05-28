
import pygame
from source.biblioteca_sons import get_sounds
from source.biblioteca_sons import funcionar, bassgor, senoide, quadrada, serra, triangular
import source.biblioteca_auxiliar as bib_aux

# =========================================================================== #
teclas_keys = {97, 115, 100, 102, 103, 104, 106, 107, 108, 231, 1073741824, 93}
teclas_timbres = {'1', '2', '3', '4', '0', '9'}
sample_rate = 48000
oitava = 2
intensidade = 0.6
tipo_escala = 'temperada'
diapasao = 440
timbre = funcionar
# =========================================================================== #
titulo = 'harenator'
text_list = [
    'teclas:',
    'oitavas:',
    'volume:',
    'escalas:',
    'timbres:',
    ]
text_list2 = [
    'a, s, d, f, g, h, j, k, l, ç, ~, ]',
    'esquerda / direita',
    'cima / baixo',
    'z, x, c',
    '1, 2, 3, 4, 0, 9,'
]
# =========================================================================== #
def draw_text(text, font, text_color, x, y):
    img = font.render(text, True, text_color)
    screen.blit(img, (x, y))
# --------------------------- #
def atualiza_sons():
    return get_sounds(
        timbre=timbre, 
        sample_rate=sample_rate, 
        tipo=tipo_escala, 
        diapasao=diapasao)
# -------------------------------------- #
# coloca as notas a soar ----------------
def tocador(key_pressionada, intensidade):
    sound = None
    if key_pressionada == 97:
        sound = teclado[oitava][0]
    if key_pressionada == 115:
        sound = teclado[oitava][1]
    if key_pressionada == 100:
        sound = teclado[oitava][2]
    if key_pressionada == 102:
        sound = teclado[oitava][3]
    if key_pressionada == 103:
        sound = teclado[oitava][4]
    if key_pressionada == 104:
        sound = teclado[oitava][5]
    if key_pressionada == 106:
        sound = teclado[oitava][6]
    if key_pressionada == 107:
        sound = teclado[oitava][7]
    if key_pressionada == 108:
        if oitava > 6:
            sound = teclado[oitava][1]
        else: 
            sound = teclado[oitava + 1][1]
    if key_pressionada == 231:
        if oitava > 6:
            sound = teclado[oitava][2]
        else: 
            sound = teclado[oitava + 1][2]
    if key_pressionada == 1073741824:
        if oitava > 6:
            sound = teclado[oitava][3]
        else: 
            sound = teclado[oitava + 1][3]
    if key_pressionada == 93:
        if oitava > 6:
            sound = teclado[oitava][4]
        else: 
            sound = teclado[oitava + 1][4]
    sound.set_volume(intensidade)
    return sound.play(loops=-1)
# ----------------------------- #
# coloca as notas em silêncio
def silenciador(key_levantada):
    if key_levantada == 97:
        teclado[oitava][0].fadeout(1)
    if key_levantada == 115:
        teclado[oitava][1].fadeout(1)
    if key_levantada == 100:
        teclado[oitava][2].fadeout(1)
    if key_levantada == 102:
        teclado[oitava][3].fadeout(1)
    if key_levantada == 103:
        teclado[oitava][4].fadeout(1)
    if key_levantada == 104:
        teclado[oitava][5].fadeout(1)
    if key_levantada == 106:
        teclado[oitava][6].fadeout(1)
    if key_levantada == 107:
        teclado[oitava][7].fadeout(1)
    if key_levantada == 108:
        if oitava > 6:
            teclado[oitava][1].fadeout(1)
        else:
            teclado[oitava + 1][1].fadeout(1)
    if key_levantada == 231:
        if oitava > 6:
            teclado[oitava][2].fadeout(1)
        else:
            teclado[oitava + 1][2].fadeout(1)
    if key_levantada == 1073741824:
        if oitava > 6:
            teclado[oitava][3].fadeout(1)
        else:
            teclado[oitava + 1][3].fadeout(1)
    if key_levantada == 93:
        if oitava > 6:
            teclado[oitava][4].fadeout(1)
        else:
            teclado[oitava + 1][4].fadeout(1)
    return None
# =========================================================================== #
# Inicia o pygame
pygame.init()
pygame.mixer.pre_init(
    frequency=sample_rate, 
    size=32, 
    buffer=1024)
pygame.mixer.init()
# ---------------------- #
# organiza o sintetizador
atualiza_sons()
teclado = bib_aux.get_playable()
# ---------------------------- #
width = 600
height = 320
screen = pygame.display.set_mode((width, height))
text_font = pygame.font.SysFont(None, 30)
titulo_font = pygame.font.SysFont(None, 40)
# =========================================================================== #
# loop
run = True
while run:
    screen.fill((0, 0, 0))
    cor = (255, 255, 255)
    draw_text(titulo, titulo_font, cor, 40, 40)
    teste = [t for t in range(100, 241, 35)]
    for index in range(len(text_list)):
        draw_text(text_list[index], text_font, cor, 100, teste[index])
        draw_text(text_list2[index], text_font, cor, 250, teste[index])
# ------------------------------------------------------------------- #
    for event in pygame.event.get():
        # ------------------------- #
        # quit ---------------------
        if event.type == pygame.QUIT:
            run = False
# ------------------------------------ #
# KEYDOWN -----------------------------
        if event.type == pygame.KEYDOWN:
            pressionada = event.dict['unicode']
            pressionada_key = event.dict['key']
            # Interrompe todos os sons -> esc
            if pressionada == '\x1b':
                pygame.mixer.stop()
            # teclado musical ---------------
            if pressionada_key in teclas_keys:
                tocador(pressionada_key, intensidade)
            # timbres básicos-----------------------
            if pressionada in teclas_timbres:
                if pressionada == '1':
                    timbre = senoide
                    intensidade = 0.6
                if pressionada  == '2':
                    timbre = quadrada
                    intensidade = 0.2
                if pressionada == '3':
                    timbre = serra
                    intensidade = 0.3
                if pressionada == '4':
                    timbre = triangular
                    intensidade = 0.6
                # -------------------
                if pressionada == '0':
                    timbre = funcionar
                    intensidade = 0.6
                if pressionada == '9':
                    timbre = bassgor
                    intensidade = 0.6
                # -------------------
                atualiza_sons()
                teclado = bib_aux.get_playable()
            # tipos de escalas ----------------
            if pressionada in {'z', 'x', 'c'}:
                if pressionada == 'z':
                    tipo_escala = 'natural'
                if pressionada == 'x':
                    tipo_escala = 'temperada'
                if pressionada == 'c':
                    tipo_escala = 'pitagorica'
                atualiza_sons()
                teclado = bib_aux.get_playable()
            # seleciona a oitava -------------------------
            if pressionada_key in {1073741903, 1073741904}:
                oitava = bib_aux.set_oitava(pressionada_key, oitava)
            # Aumenta/diminui a intensidade -----------------------
            if pressionada_key in {1073741905, 1073741906}:
                intensidade = bib_aux.set_intensidade(intensidade, 
                                                    pressionada_key)
# ---------------------------------------------------------------- #
# KEYUP -----------------------------
        if event.type == pygame.KEYUP:
            despressionada = event.dict['unicode']
            despressionada_key = event.dict['key']
            # silencia os sons ------------------
            if despressionada_key in teclas_keys:
                silenciador(despressionada_key)
    pygame.display.flip()
# =========================================================================== #
pygame.quit()                                                                 #
# =========================================================================== #
