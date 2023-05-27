import pygame

from source.biblioteca_sons import get_sounds
from source.biblioteca_sons import funcionar, bassgor
import source.biblioteca_auxiliar as bib_aux
# ========================================================= #
teclas = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'}
sample_rate = 48000
oitava = 2
intensidade = 0.6
tipo_escala = 'temperada'
diapasao = 440
timbre = funcionar
# ========================================================= #
def atualiza_sons():
    return get_sounds(
        timbre=timbre, 
        sample_rate=sample_rate, 
        tipo=tipo_escala, 
        diapasao=diapasao
    )
# ========================================================= #
pygame.init()
pygame.mixer.pre_init(
    frequency=sample_rate, 
    size=32, 
    buffer=4096)
pygame.mixer.init()
# --------------- #
atualiza_sons()
teclado = bib_aux.get_playable()
# -------------------- #
width = 600
height = 400
screen = pygame.display.set_mode((width, height))
# ========================================================= #
run = True
while run:
    for event in pygame.event.get():
        # ------------------------- #
        if event.type == pygame.QUIT:
            run = False
        # -------------------------------- #
        if event.type == pygame.KEYDOWN:
            pressionada = event.dict['unicode']
            pressionada_key = event.dict['key']
            # Para todos os sons com 'esc'
            if pressionada == '\x1b':
                pygame.mixer.stop()
            # Banco de sons
            if pressionada in {'1', '2'}:
                if pressionada == '1':
                    timbre = funcionar
                    atualiza_sons()
                    teclado = bib_aux.get_playable()
                if pressionada == '2':
                    timbre = bassgor
                    atualiza_sons()
                    teclado = bib_aux.get_playable()
            # Seleciona a oitava
            if pressionada_key in {1073741903, 1073741904}:
                oitava = bib_aux.set_oitava(pressionada_key, oitava)
            # Aumenta/diminui a intensidade
            if pressionada_key in {1073741905, 1073741906}:
                intensidade = bib_aux.set_intensidade(intensidade, pressionada_key)
            # Teclado
            if pressionada in teclas:
                if pressionada == 'a':
                    sound = teclado[oitava][0]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 's':
                    sound = teclado[oitava][1]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 'd':
                    sound = teclado[oitava][2]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 'f':
                    sound = teclado[oitava][3]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 'g':
                    sound = teclado[oitava][4]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 'h':
                    sound = teclado[oitava][5]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 'j':
                    sound = teclado[oitava][6]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
                if pressionada == 'k':
                    sound = teclado[oitava][7]
                    sound.set_volume(intensidade)
                    sound.play(loops=-1)
        # -------------------------------- #
        if event.type == pygame.KEYUP:
            despressionada = event.dict['unicode']
            if despressionada in teclas:
                if despressionada == 'a':
                    teclado[oitava][0].fadeout(1)
                if despressionada == 's':
                    teclado[oitava][1].fadeout(1)
                if despressionada == 'd':
                    teclado[oitava][2].fadeout(1)
                if despressionada == 'f':
                    teclado[oitava][3].fadeout(1)
                if despressionada == 'g':
                    teclado[oitava][4].fadeout(1)
                if despressionada == 'h':
                    teclado[oitava][5].fadeout(1)
                if despressionada == 'j':
                    teclado[oitava][6].fadeout(1)
                if despressionada == 'k':
                    teclado[oitava][7].fadeout(1)
        # -------------------------------- #
pygame.quit()
# ========================================================= #

