from biblioteca_classes import HareOom, HareSom, hz, amp
from classe_Escalator import Escalator
import sounddevice as sd
import matplotlib.pyplot as plt
import time

# =========================================================================== #
sample_rate = 48000
# =========================================================================== #
def funcionar(frequencia):
    # timbre-matt-lead-1 ------------------ #
    intensidades = [0.8, 0.4, 0.6, 0.1, 0.05]
    harmonicos = ['quadrada', 'quadrada', 'triangular', 'serra']
    # --------------------------------------------------------- #
    soom = HareSom(
        sample_rate=sample_rate, 
        tipo='serra',
        frequencia=frequencia
    )
    soom.set_paleta(limite=16000)
    soom.set_timbre(intensidades=intensidades, tipos=harmonicos)
    soom = soom.get_onda()
    som = amp(soom, 0.5)
    return som
# --------------------------------------------------------------------------- #
def bassgor(frequencia):
    # timbre-bass-1 ---------------------------- #
    intensidades = [1, 0.5, 0.6, 1, 0.3, 0.5, 0.3]
    harmonicos = ['senoide', 'quadrada', 'senoide', 'serra', 'senoide', 'serra']
    # --------------------------------------------------------- #
    soom = HareSom(
        sample_rate=sample_rate, 
        tipo='quadrada',
        frequencia=frequencia
    )
    soom.set_paleta(limite=16000)
    soom.set_timbre(intensidades=intensidades, tipos=harmonicos)
    soom = soom.get_onda()
    som = amp(soom, 0.5)
    return som
# =========================================================================== #
# def tester(num: int):
#     if num == 1:
#         f = 55
#         escalator = Escalator()
#         la_natural = [f * nota for nota in escalator.natural]
#         la_temperada = [f * nota for nota in escalator.temperada]
#         la_pitagorica = [f * nota for nota in escalator.pitagorica]
#         lista_sons = [bassgor(f)]
#         escalas = [la_natural, la_temperada, la_pitagorica]
#         for escala in escalas:
#             for nota in escala:
#                 som = bassgor(nota)
#                 lista_sons.append(som)
#         print('###')
#         for som in lista_sons:
#             sd.play(data=som, samplerate=sample_rate, loop=True)
#             time.sleep(0.2)
#             sd.stop()
#     if num == 2:
#         notas = [funcionar(frequencia) for frequencia in Escalator().piano()]
#         # notas = notas[2:18]
#         for nota in notas:
#             sd.play(data=nota, samplerate=sample_rate, loop=True)
#             time.sleep(0.2)
#             sd.stop()
#         notas.reverse()
#         for nota in notas:
#             sd.play(data=nota, samplerate=sample_rate, loop=True)
#             time.sleep(0.01)
#             sd.stop()
# # # ------------------------------------------------------------ #
# tester(2)
# =========================================================================== #




