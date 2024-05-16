
import numpy as np

# ==================================================================================================================== #
# Sintetizador de ondas
''' 
Uma pequena biblioteca de funções que retornam arrays do numpy,
cada array representa um tipo de onda.
'''
# senoide ----------------------------
def synth_sen(sample_rate, frequencia):
    espaco_x = np.linspace(start=0, stop=1, num=int(sample_rate / frequencia), endpoint=False)
    num = 2 ** 31
    senoide = np.sin(2 * np.pi * espaco_x)
    senoide = np.clip(a=(senoide * num), a_max=num - 1, a_min=-num)
    senoide = senoide.astype(np.int32)
    return senoide
# quadrada-----------------------------
def synth_quad(sample_rate, frequencia):
    num = 2 ** 31
    n = int(sample_rate / frequencia)
    positivo = int(n / 2)
    negativo = n - positivo
    quadrada = np.concatenate((np.full(positivo, num - 1), np.full(negativo, -num)), dtype='int32')
    return quadrada
# serra -------------------------------
def synth_serr(sample_rate, frequencia):
    num = (2 ** 31)
    espaco_x = np.linspace(start=(num - 1), stop=-num, num=int(sample_rate / frequencia))
    espaco_x = espaco_x.astype(np.int32)
    return espaco_x
# triangular -------------------------
def synth_tri(sample_rate, frequencia):
    num, n = (2 ** 31), int(sample_rate / frequencia)
    menor = n // 2
    maior = n - menor
    array_a = np.linspace(start=-num, stop=(num - 1), num=maior)
    array_b = np.linspace(start=(num - 1), stop=-num, num=(menor + 1), endpoint=False)[1:]
    triangular = np.concatenate((array_a, array_b))
    return triangular
# ==================================================================================================================== #
# seletor de ondas -----------------------
def seletor(sample_rate, tipo, frequencia):
    if tipo == 'senoide':
        return synth_sen(sample_rate=sample_rate, frequencia=frequencia)
    if tipo == 'quadrada':
        return synth_quad(sample_rate=sample_rate, frequencia=frequencia)
    if tipo == 'serra':
        return synth_serr(sample_rate=sample_rate, frequencia=frequencia)
    if tipo == 'triangular':
        return synth_tri(sample_rate=sample_rate, frequencia=frequencia)
# ==================================================================================================================== #
