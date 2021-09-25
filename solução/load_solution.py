
from pergunta3 import resolve_pergunta_3
from pergunta2 import resolve_pergunta_2
import pandas as pd
from pergunta1 import resolve_pergunta_1

path = '/home/atr/codarshians/codarshians/data_feather/'
municipios = pd.read_feather(path+'municipios.ftr')
simples = pd.read_feather(path+'simples.ftr')
estabelecimentos = pd.read_csv(path+'estabelecimentos.csv', sep = ';')
estabelecimentos['Data Situação Cadastral'] = pd.to_datetime(estabelecimentos['Data Situação Cadastral'], exact=False, format='%Y-%m-%d')

# print("- Solucionando 1")
# industrias_ativas_simples, industrias_ativas_mei = resolve_pergunta_1(municipios, estabelecimentos, simples)

# print("- Solucionando 2")
# comercios_inativos_simples, comercios_inativos_mei = resolve_pergunta_2(municipios, estabelecimentos, simples)

print("- Solucionando 3")
novos_simples, novos_mei = resolve_pergunta_3(municipios, estabelecimentos, simples)



