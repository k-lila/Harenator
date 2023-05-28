
from source.classe_hareOomSom import HareOom, HareSom
from source.biblioteca_auxiliar import amp, get_teclado, get_wave

# =========================================================================== #
'''
A biblioteca de sons contém duas funções que, juntas, fornecem os sons ao
teclado. Além disso, contém também dois timbres iniciais, que servem de
exemplo de como organizar o dicionário necessário para as funções descritas
acima funcionarem.
'''
funcionar = {
    'intensidades': [0.8, 0.4, 0.6, 0.1, 0.05],
    'ondas': ['serra', 'quadrada', 'quadrada', 'triangular', 'serra'] 
}
bassgor = {
    'intensidades': [1, 0.5, 0.6, 1, 0.3, 0.5, 0.3],
    'ondas': ['quadrada', 'senoide', 'quadrada', 
                'senoide', 'serra', 'senoide', 'serra']
}
# =========================================================================== #
# define o numpy array para cada nota
def get_timbre(timbre: dict, frequencia, sample_rate):
    intensidades = timbre['intensidades']
    tipos = timbre['ondas']
    soom = HareSom(
        sample_rate=sample_rate, 
        tipo=tipos[0],
        frequencia=frequencia
    )
    soom.set_paleta(limite=16000)
    soom.set_timbre(intensidades=intensidades, tipos=tipos[1:])
    soom = soom.get_onda()
    som = amp(soom, 0.5)
    return som
# ---------------------------------------------------------------------- #
# cria os arquivos .wav
def get_sounds(timbre: dict, sample_rate, tipo='temperada', diapasao=440):
    escala = get_teclado(diapasao=diapasao, tipo=tipo)
    for oitava_index in range(len(escala)):
        for nota_index in range(len(escala[oitava_index])):
            som = get_timbre(timbre=timbre, 
                            frequencia=escala[oitava_index][nota_index],
                            sample_rate=sample_rate)
            get_wave(
                chunk=som,
                sample_rate=sample_rate,
                path=f'./source/wav/{oitava_index}{nota_index}.wav'
            )
# =========================================================================== #
