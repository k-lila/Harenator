import pygame
import wave
from classe_Escalator import Escalator
from biblioteca_sons import funcionar, bassgor
# ========================================================= #
sample_rate = 48000
# ========================================================= #
def get_teclado(diapasao=440):
    escalator = Escalator()
    fundamental = (diapasao / escalator.temperada[5]) / (2 ** 4)
    lista_teclado = []
    for oitava in range(8):
        _escala = [(fundamental * i) * (2 ** oitava) for i in escalator.natural]
        lista_teclado.append(_escala)
    return lista_teclado
# -------------------------------------------------------- #
def get_waves(chunk, path):
    file = wave.open(path, mode='w')
    file.setnchannels(1)
    file.setsampwidth(4)
    file.setframerate(sample_rate)
    file.writeframes(chunk)
    return file.close()
# ----------------------------------------------------- #
def get_sounds(num):
    escala = get_teclado(diapasao=440)
    if num == 1:
        for oitava_index in range(len(escala)):
            for nota_index in range(len(escala[oitava_index])):
                nota = funcionar(escala[oitava_index][nota_index])
                get_waves(chunk=nota, 
                    path=f'./wav/{oitava_index}{nota_index}.wav')
    if num == 2:
        for oitava_index in range(len(escala)):
            for nota_index in range(len(escala[oitava_index])):
                nota = bassgor(escala[oitava_index][nota_index])
                get_waves(chunk=nota, 
                    path=f'./wav/{oitava_index}{nota_index}.wav')
    return None
# ----------------------------------------------------- #
def get_playable():
    teclado = []
    for i in range(8):
        temp = []
        for ii in range(8):
            som = pygame.mixer.Sound(f'./wav/{i}{ii}.wav')
            temp.append(som)
        teclado.append(temp)
    return teclado
# ----------------------------------------------------- #
oitava = 2
def set_oitava(num, oitava):
    up_key = 1073741906
    down_key = 1073741905
    if num == up_key:
        if oitava < 7:
            oitava += 1
    if num == down_key:
        if oitava > 0:
            oitava -= 1
    return oitava
# ========================================================= #
pygame.init()
pygame.mixer.pre_init(
    frequency=sample_rate, 
    size=32, 
    buffer=4096)
pygame.mixer.init()
# --------------- #
get_sounds(1)
teclado = get_playable()
# ----------------------------------------- #
width = 1000
height = 600
screen = pygame.display.set_mode((width, height))
# ========================================================= #
teclas = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k'}
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
            if pressionada in {'1', '2'}:
                if pressionada == '1':
                    get_sounds(1)
                    teclado = get_playable()
                if pressionada == '2':
                    get_sounds(2)
                    teclado = get_playable()
            if pressionada_key in {1073741905, 1073741906}:
                oitava = set_oitava(pressionada_key, oitava)
            if pressionada in teclas:
                if pressionada == 'a':
                    teclado[oitava][0].play(loops=-1)
                if pressionada == 's':
                    teclado[oitava][1].play(loops=-1)
                if pressionada == 'd':
                    teclado[oitava][2].play(loops=-1)
                if pressionada == 'f':
                    teclado[oitava][3].play(loops=-1)
                if pressionada == 'g':
                    teclado[oitava][4].play(loops=-1)
                if pressionada == 'h':
                    teclado[oitava][5].play(loops=-1)
                if pressionada == 'j':
                    teclado[oitava][6].play(loops=-1)
                if pressionada == 'k':
                    teclado[oitava][7].play(loops=-1)
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
# # ========================================================= #

