
import numpy as np
import wave
import pygame
from itertools import cycle
from src.classe_Escalator import Escalator

# =========================================================================== #
"""
    A biblioteca auxiliar contém um conjunto de funções auxiliares. As funções
acessórias são funções úteis para a manipulação dos arrays de som. 
"""
# funções acessórias --------------------------- #
# retorna 1hz a partir do array -----------------
def hz(chunk, duracao: float or int, sample_rate):
    ciclo = cycle(range(len(chunk)))
    num = int(sample_rate * duracao)
    hz = np.empty(0)
    while len(hz) != num:
        hz = np.append(hz, chunk[next(ciclo)])
    return hz.astype(np.int32)
# ------------------------------------------ #
# modifica a amplitude(intensidade) do array
def amp(chunk, num):
    nova_onda = chunk * num
    return nova_onda.astype(np.int32)
# =========================================================================== #
"""
Funções que permitem o teclado do pygame funcionar adequadamente.
"""
# lista com listas que contém as frequências das notas separadas por oitavas
def get_teclado(diapasao=440, tipo='natural'):
    escalator = Escalator()
    fundamental = (diapasao / escalator.temperada[5]) / (2 ** 4)
    lista_teclado = []
    for oitava in range(8):
        if tipo == 'natural':
            _escala = [(fundamental * i) * (2 ** oitava) 
                        for i in escalator.natural]
            lista_teclado.append(_escala)
        if tipo == 'temperada':
            _escala = [(fundamental * i) * (2 ** oitava) 
                        for i in escalator.temperada]
            lista_teclado.append(_escala)
        if tipo == 'pitagorica':
            _escala = [(fundamental * i) * (2 ** oitava)  
                        for i in escalator.pitagorica]
            lista_teclado.append(_escala)
    return lista_teclado
# ---------------------------------------------------- #
# cria um arquivo wave ---------------
def get_wave(chunk, sample_rate, path):
    file = wave.open(path, mode='w')
    file.setnchannels(1)
    file.setsampwidth(4)
    file.setframerate(sample_rate)
    file.writeframes(chunk)
    return file.close()
# --------------------------- #
# define a oitava a ser tocada
def set_oitava(num, oitava):
    up_key = 1073741903
    down_key = 1073741904
    if num == up_key:
        if oitava < 7:
            oitava += 1
    if num == down_key:
        if oitava > 0:
            oitava -= 1
    return oitava
# ----------------------------------------------- #
# define os arquivos usados pelo teclado do pygame
def get_playable():
    teclado = []
    for i in range(8):
        temp = []
        for ii in range(8):
            som = pygame.mixer.Sound(f'./src/wav/{i}{ii}.wav')
            temp.append(som)
        teclado.append(temp)
    return teclado
# ---------------------------------- #
# define a intensidade (volume) -----
def set_intensidade(intensidade, key):
    passo = 1 / 12
    up_vol = 1073741906
    down_vol = 1073741905
    if key == up_vol:
        intensidade += passo
    if key == down_vol:
        intensidade -= passo
    if intensidade > 1:
        intensidade = 1
    if intensidade < 0:
        intensidade = 0
    return intensidade
# =========================================================================== #
