
import pygame
from source.biblioteca_sons import get_sounds
from source.biblioteca_sons import funcionar, bassgor
import source.biblioteca_auxiliar as bib_aux

# =========================================================================== #
teclas = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'}
sample_rate = 48000
oitava = 2
intensidade = 0.6
tipo_escala = 'temperada'
diapasao = 440
timbre = funcionar
# =========================================================================== #
def atualiza_sons():
    return get_sounds(
        timbre=timbre, 
        sample_rate=sample_rate, 
        tipo=tipo_escala, 
        diapasao=diapasao)
# ---------------------------------------- #
# coloca as notas a soar
def tocador(tecla_pressionada, intensidade):
    sound = None
    if tecla_pressionada == 'a':
        sound = teclado[oitava][0]
    if tecla_pressionada == 's':
        sound = teclado[oitava][1]
    if tecla_pressionada == 'd':
        sound = teclado[oitava][2]
    if tecla_pressionada == 'f':
        sound = teclado[oitava][3]
    if tecla_pressionada == 'g':
        sound = teclado[oitava][4]
    if tecla_pressionada == 'h':
        sound = teclado[oitava][5]
    if tecla_pressionada == 'j':
        sound = teclado[oitava][6]
    if tecla_pressionada == 'k':
        sound = teclado[oitava][7]
    sound.set_volume(intensidade)
    return sound.play(loops=-1)
# ------------------------------- #
# coloca as notas em silêncio
def silenciador(tecla_levantada):
    if tecla_levantada == 'a':
        teclado[oitava][0].fadeout(1)
    if tecla_levantada == 's':
        teclado[oitava][1].fadeout(1)
    if tecla_levantada == 'd':
        teclado[oitava][2].fadeout(1)
    if tecla_levantada == 'f':
        teclado[oitava][3].fadeout(1)
    if tecla_levantada == 'g':
        teclado[oitava][4].fadeout(1)
    if tecla_levantada == 'h':
        teclado[oitava][5].fadeout(1)
    if tecla_levantada == 'j':
        teclado[oitava][6].fadeout(1)
    if tecla_levantada == 'k':
        teclado[oitava][7].fadeout(1)
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
height = 400
screen = pygame.display.set_mode((width, height))
# =========================================================================== #
# loop
run = True
while run:
    for event in pygame.event.get():
        # ------------------------- #
        # quit
        if event.type == pygame.QUIT:
            run = False
        # ----------------------------------- #
        # teclado
        if event.type == pygame.KEYDOWN:
            pressionada = event.dict['unicode']
            pressionada_key = event.dict['key']
            # teclado musical
            if pressionada in teclas:
                tocador(pressionada, intensidade)
            # Para todos os sons
            if pressionada == '\x1b':
                pygame.mixer.stop()
            # timbres básicos
            if pressionada in {'1', '2'}:
                if pressionada == '1':
                    timbre = funcionar
                if pressionada == '2':
                    timbre = bassgor
                atualiza_sons()
                teclado = bib_aux.get_playable()
            # tipos de escalas
            if pressionada in {'z', 'x', 'c'}:
                if pressionada == 'z':
                    tipo_escala = 'natural'
                if pressionada == 'x':
                    tipo_escala = 'temperada'
                if pressionada == 'c':
                    tipo_escala = 'pitagorica'
                atualiza_sons()
                teclado = bib_aux.get_playable()
            # seleciona a oitava
            if pressionada_key in {1073741903, 1073741904}:
                oitava = bib_aux.set_oitava(pressionada_key, oitava)
            # Aumenta/diminui a intensidade
            if pressionada_key in {1073741905, 1073741906}:
                intensidade = bib_aux.set_intensidade(intensidade, pressionada_key)
        # ----------------------------------------------------------------------- #
        if event.type == pygame.KEYUP:
            despressionada = event.dict['unicode']
            # silencia os sons
            if despressionada in teclas:
                silenciador(despressionada)
        # ------------------------------------- #
pygame.quit()
# =========================================================================== #

