
import pandas as pd
from perguntaa1 import resolve_pergunta_1

path = '/home/atr/codarshians/codarshians/data_feather/'
municipios = pd.read_feather(path+'municipios.ftr')
simples = pd.read_feather(path+'simples.ftr')
estabelecimentos = pd.read_csv(path+'estabelecimentos.csv', sep = ';')

resposta = resolve_pergunta_1(municipios, estabelecimentos, simples)
print(resposta)

