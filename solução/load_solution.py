
from pergunta3 import resolve_pergunta_3
from pergunta2 import resolve_pergunta_2
import pandas as pd
from pergunta1 import resolve_pergunta_1
from pergunta4 import resolve_pergunta_4
from pergunta5 import resolve_pergunta_5
from pergunta6 import resolve_pergunta_6

path = '/home/atr/codarshians/codarshians/data_feather/'

municipios = pd.read_feather(path+'municipios.ftr')
simples = pd.read_feather(path+'simples.ftr')
empresas = pd.read_feather(path+'empresas.ftr')
estabelecimentos = pd.read_csv(path+'estabelecimentos.csv', sep = ';')
estabelecimentos['Data Situação Cadastral'] = pd.to_datetime(estabelecimentos['Data Situação Cadastral'], exact=False, format='%Y-%m-%d')
# #estabelecimentos['Data de Início atividade'] = pd.to_datetime(estabelecimentos['Data de Início atividade'], exact=False, format='%YYYY-%mm-%dd %HH:%MM:%SS')
# print(type(estabelecimentos['Data Situação Cadastral'][0]))
# print(type(estabelecimentos['Data de Início atividade'][0]))

# print("- Solucionando 1")
# industrias_ativas_simples, industrias_ativas_mei = resolve_pergunta_1(municipios, estabelecimentos, simples)

# print("- Solucionando 2")
# comercios_inativos_simples, comercios_inativos_mei = resolve_pergunta_2(municipios, estabelecimentos, simples)

# print("- Solucionando 3")
# novos_simples, novos_mei = resolve_pergunta_3(municipios, estabelecimentos, simples)

# print("- Solucionando 4")
# novos_ed_superior = resolve_pergunta_4(estabelecimentos)

# print("- Solucionando 5")
# capital_social_médio = resolve_pergunta_5(estabelecimentos, empresas)

print("- Solucionando 6")
capital_nat_juridica = resolve_pergunta_6(estabelecimentos, empresas)
