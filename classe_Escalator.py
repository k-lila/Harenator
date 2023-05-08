import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================================================================================== #
# Escalator
class Escalator(object):
    ''' 
    A classe Escalator contém os cálculos das escalas musicais.
    Os atributos retornam valores entre 1 e 2 que, ao serem
    multiplicados pela frequência (diapasão), retornam
    a frequência relativa à nota desejada.
    '''
    def __init__(self, diapasao):
        self.diapasao = diapasao
        self.natural = self._get_natural()
        self.pitagorica = self._get_pitagorica()
        self.cromatica = self._get_cromatica()
        self.temperada = self._get_temperada()
    # ------------------------------------------------ #
    # escala natural - contruída a partir dos harmônicos
    def _get_natural(self):
        # Primeiras relações:
        c = 1  #           Tônica  | Nota/frequência fundamental.
        g = c * 3  #       Quinta  | 2º harmônico da fundamental
        e = c * 5  #       terça   | 5º harmônico da fundamental.
        f = c / 3  #       Quarta  | Aqui, a fundamental é considerada o segundo harmônico.
        # Relações secundárias:
        d = g * 3  #       segunda | 2º harmônico do quinto grau da fundamental.
        e = c * 5  #       terça   | 5º harmônico da fundamental.
        a = f * 5  #       sexta   | 5º harmônico se a fundamental fosse, ela mesma, o quinto harmônico de outra nota.
        b = g * 5  #       sétima  | 5º harmônico do quinto grau da fundamental.
        # Ajuste de oitavas
        g, e, d, b, f = g / 2, e / 4, d / 8, b / 8, f * 4
        return [c, d, e, f, g, a, b, c * 2]
    # --------------------------------------------------------- #
    # escala pitagórica, construída a partir de quintas e oitavas
    def _get_pitagorica(self):
        quintas = [1 * (3 ** num) for num in range(8)]
        pitagorica = []
        for nota in quintas:
            temp = nota
            while 1 <= temp >= 2.15:
                temp = temp / 2
            pitagorica.append(temp)
        pitagorica = sorted(pitagorica)
        return pitagorica
    # ------------------------------------------------------- #
    # escala cromática - construída a partir de semitons exatos
    def _get_cromatica(self):
        semitom = (2 ** (1/12))
        return [semitom ** x for x in range(13)]
    # -------------------------------------------------------- #
    # escala temperada - construída a partir da escala cromática
    def _get_temperada(self):
        temperada = [self.cromatica[i] for i in range(len(self.cromatica)) if i in {0, 2, 4, 5, 7, 9, 11, 12}]
        return temperada
    # ------------------------------------------------------------------------------------------------ #
    # comas - 
    # def get_comas(self):
# ==================================================================================================================== #
# testes
def tester(num=1):
    classe = Escalator(diapasao=1)
    # -------------------------- #
    # escala natural
    if num == 1:
        escala_teste = [classe.diapasao * num for num in classe.natural]        
        x = list(range(len(escala_teste)))
        labels_x = ['Tônica', 'segunda', 'III', 'quarta', 'V', 'sexta', 'VII', 'Tônica']
        plt.bar(x=x, height=escala_teste, tick_label=labels_x)
        plt.show()
    # --------------------------------------------------- #
    # escala pitagórica
    if num == 2:
        escala_teste = classe.pitagorica
        x = list(range(len(escala_teste)))
        labels_x = ['Tônica', 'segunda', 'III', 'quarta', 'V', 'sexta', 'VII', 'Tônica']
        plt.bar(x=x, height=escala_teste, tick_label=labels_x)
        plt.show()
    # --------------------------------------------------- #
    # escala cromática
    if num == 3:
        escala_teste = [classe.diapasao * num for num in classe.cromatica]
        x = list(range(len(escala_teste)))
        labels_x = ['T', 'b#', 'ii', 'b#', 'iii', 'IV', 'trit', 'V', 'b#', 'vi', 'b#', 'vii', 'T']
        plt.bar(x=x, height=escala_teste, tick_label=labels_x)
        plt.show()
    # --------------------------------------------------- #
    # escala temperada
    if num == 4:
        escala_teste = [classe.diapasao * num for num in classe.temperada]
        x = list(range(len(escala_teste)))
        labels_x = ['Tônica', 'segunda', 'III', 'quarta', 'V', 'sexta', 'VII', 'Tônica']
        plt.bar(x=x, height=escala_teste, tick_label=labels_x)
        plt.show()
    # --------------------------------------------------- #
    if num == 5:
        plt.plot(classe.natural)
        plt.plot(classe.pitagorica)
        plt.plot(classe.temperada)
        plt.show()
# ---------------------------- #
tester(num=5)
# ==================================================================================================================== #
