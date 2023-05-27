import matplotlib.pyplot as plt
import numpy as np
import biblioteca_ondas as ondas
from itertools import cycle

# ==================================================================================================================== #
# Classe HareOom
class HareOom(object):
    '''
    A classe HareOom encontra, a partir de seus parâmetros, a sequência de números inteiros (np.int32)
    que dizem respeito a 1 oscilação da frequência.
    '''
    def __init__(self, sample_rate: int, tipo: str, frequencia):
        self.sample_rate = sample_rate
        self.tipo = tipo
        self.frequencia = frequencia
        self.fundamental = self._get_fundamental()
    # ------------------------------------------ #
    # onda fundamental
    def _get_fundamental(self):
        fundamental = ondas.seletor(
            sample_rate=self.sample_rate,
            tipo=self.tipo,
            frequencia=self.frequencia
        )
        return fundamental
    # ------------------------------------- #
    # harmônico da fundamental
    def harmonico(self, num: int, tipo=None):
        num += 1
        if tipo == None:
            tipo = self.tipo
        frequencia = self.frequencia * num
        harmonico = ondas.seletor(
            sample_rate=self.sample_rate,
            tipo=tipo,
            frequencia=frequencia
        )
        return harmonico
# ==================================================================================================================== #
# HareSom
class HareSom(HareOom):
    ''' 
    A classe HareSom herda a classe HareOom e será a classe utilizada para definir cada nota das escalas musicais.
    Para utilizá-la devidamente, duas coisas são necessárias:
        1) definir o atributo 'paleta'. 
        É nele que estarão contidos os harmônicos possíveis dentro do limite estabelecido.
        2) definir o atributo 'timbre'.
        Para tanto, é preciso de uma lista de intensidades dos harmônicos (entre 0 e 1);
        e também de uma lista dos tipos de ondas dos harmônicos, se uma senóide, quadrada, etc.
    Com isso, conseguiremos uma onda resultante através do método '.get_onda()'
    '''
    def __init__(self, sample_rate: int, tipo: str, frequencia):
        super().__init__(sample_rate, tipo, frequencia)
        self.limite = None
        self.paleta = None
        self.timbre = None
    # ---------------------------------------------------------------- #
    # A paleta é uma lista com a frequência fundamental e os harmônicos.
    def set_paleta(self, limite=20000):
        self.limite = limite
        max_harm = 1
        f = self.frequencia * max_harm
        paleta = []
        while f < limite:
            paleta.append(f)
            max_harm += 1
            f = self.frequencia * max_harm
        self.paleta = paleta
        return None
    # ----------------------------------------- #
    # a lista de intensidades é uma lista de números entre 0 e 1
    # a lista de tipos é uma lista com os tipos de ondas dos harmônicos
    def set_timbre(self, intensidades: list, tipos: list):
        num_i = len(intensidades)
        timbre = []
        if (len(intensidades) - 1) == len(tipos):
            for i in range(num_i):
                onda = None
                if i == 0:                    
                    onda = self.fundamental * intensidades[i]
                else:
                    onda = self.harmonico(num=i, tipo=tipos[i - 1]) * intensidades[i]
                onda = np.round(onda)
                onda = onda.astype(np.int32)
                timbre.append(onda)
                # plt.plot(onda)
            self.timbre = timbre
            # plt.show()
        return None
    # -------------------------------------- #
    # Encontra os valores da onda resultante.
    def get_onda(self):
        controle = len(self.fundamental)
        harmonicos = [self.fundamental]
        multiplicador = 2
        # ajusta o tamanho dos arrays
        for i in range(1, len(self.timbre)):        
            onda = [self.timbre[i]] * multiplicador
            onda = np.concatenate(onda)
            num = len(onda)
            if num == controle:
                harmonicos.append(onda)
            else:  # adiciona ruído
                ruido = controle - num
                indices = np.random.choice(a=num, size=ruido, replace=False)
                for i in indices:
                    # r = ((onda[i - 1] + onda[i + 1]) / 2).astype(np.int32)
                    r = 0
                    onda = np.insert(onda, i, r)
                harmonicos.append(onda)
            multiplicador += 1
        self.timbre = harmonicos
        # soma os harmônicos
        onda_resultante = np.sum(harmonicos, axis=0)
        onda_resultante = (onda_resultante / len(harmonicos)).astype(np.int32)
        return onda_resultante
# ==================================================================================================================== #
# funções acessórias
def hz(chunk, duracao: float or int, sample_rate):
    ciclo = cycle(range(len(chunk)))
    num = int(sample_rate * duracao)
    hz = np.empty(0)
    while len(hz) != num:
        hz = np.append(hz, chunk[next(ciclo)])
    return hz.astype(np.int32)
def amp(chunk, num):
    nova_onda = chunk * num
    return nova_onda.astype(np.int32)
# ==================================================================================================================== #
# testes
# def tester(num: int):    
#     sample_rate = 48000
#     frequencia = 440
#     tipos = ['senoide', 'quadrada', 'serra', 'triangular']    
#     if num == 1:
#         for tipo in tipos:
#             oom = HareOom(sample_rate=sample_rate, frequencia=frequencia, tipo=tipo).fundamental
#             plt.plot(oom)
#     if num == 2:
#         som = HareSom(sample_rate=sample_rate, frequencia=frequencia, tipo='senoide')
#         som.set_paleta(limite=5000)
#         intensidades = [1, 0.1, 0.1, 0.1, 0.1, 0.5, 0.4, 0.3, 0.2, 0.1]
#         harm = [tipos[0], tipos[1], tipos[0], tipos[1], tipos[0], tipos[0], tipos[1], tipos[2], tipos[3]]
#         som.set_timbre(intensidades=intensidades, tipos=harm)
#         plt.plot(som.get_onda())
#     return plt.show()
# # ----------------------------- #
# tester(num=2)
# ==================================================================================================================== #
