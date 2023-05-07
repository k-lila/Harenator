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
        self.cromatica = self._get_cromatica()
    # -------------------------------------- #
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
        return [c, d, e, f, g, a, b, c * 2]  # escala natural
    # ----------------------------------------------------- #
    def _get_cromatica(self):
        semitom = (2 ** (1/12))
        return [semitom ** x for x in range(13)]
    # ----------------------------------------- #
    # def get_temperada(self):
    #     temperada = [self.cromatica[i] for i in range(len(self.cromatica)) if i not in {1, 3, 6, 8, 10}]
    #     return temperada
# ==================================================================================================================== #
# testes
def tester(num=1):
    classe = Escalator(diapasao=1)
    # -------------------------- #
    # escala natural
    if num == 1:
        escala_la = [classe.diapasao * num for num in classe.natural]        
        x = list(range(len(escala_la)))
        labels_x = ['Tônica', 'segunda', 'III', 'quarta', 'V', 'sexta', 'VII', 'Tônica']
        plt.bar(x=x, height=escala_la, tick_label=labels_x)
        plt.show()
    # --------------------------------------------------- #
    # escala cromática
    if num == 2:
        escala_la = [classe.diapasao * num for num in classe.cromatica]
        x = list(range(len(escala_la)))
        labels_x = ['T', 'b#', 'ii', 'b#', 'iii', 'IV', 'trit', 'V', 'b#', 'vi', 'b#', 'vii', 'T']
        plt.bar(x=x, height=escala_la, tick_label=labels_x)
        plt.show()
    # --------------------------------------------------- #
    if num == 3:
        for i in range(len(classe.natural)):
            print(i, classe.natural[i])
        print('#' * 10)
        for i in range(len(classe.cromatica)):
            print(i, classe.cromatica[i])
    # -------------------------------------- #
    if num == 4:
        plt.plot(classe.natural)
        plt.show()
# ---------------------------- #
tester(num=1)
# ==================================================================================================================== #
