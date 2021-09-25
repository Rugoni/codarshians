import pandas as pd
from pergunta1 import resolve_pergunta_1
from pergunta2 import resolve_pergunta_2
from pergunta3 import resolve_pergunta_3
from pergunta4 import resolve_pergunta_4
from pergunta5 import resolve_pergunta_5
from pergunta6 import resolve_pergunta_6

path = '/home/atr/codarshians/codarshians/data_feather/'
path_save = '/home/atr/codarshians/codarshians/respostas/'


municipios = pd.read_feather(path+'municipios.ftr')
simples = pd.read_feather(path+'simples.ftr')
empresas = pd.read_feather(path+'empresas.ftr')
estabelecimentos = pd.read_csv(path+'estabelecimentos.csv', sep = ';')
estabelecimentos['Data Situação Cadastral'] = pd.to_datetime(estabelecimentos['Data Situação Cadastral'], exact=False, format='%Y-%m-%d')

print("- Solucionando 4")
novos_ed_superior = resolve_pergunta_4(estabelecimentos)
novos_ed_superior.to_csv(path_save+'novos_ed_superior.csv', index=False, header=True, sep=';')
print("Pergunta 4 - OK!")

print("- Solucionando 5")
capital_social_médio = resolve_pergunta_5(estabelecimentos, empresas)
capital_social_médio.to_csv(path_save+'capital_social_médio.csv', index=False, header=True, sep=';')
print("Pergunta 5 - OK!")

print("- Solucionando 6")
capital_nat_juridica = resolve_pergunta_6(estabelecimentos, empresas)
capital_nat_juridica.to_csv(path_save+'capital_nat_juridica.csv', index=False, header=True, sep=';')
print("Pergunta 6 - OK!")


print("- Solucionando 3")
novos_simples, novos_mei = resolve_pergunta_3(municipios, estabelecimentos, simples)
novos_simples.to_csv(path_save+'novos_simples.csv', index=False, header=True, sep=';')
novos_mei.to_csv(path_save+'novos_mei.csv', index=False, header=True, sep=';')
print("Pergunta 3 - OK!")


print("- Solucionando 2")
comercios_inativos_simples, comercios_inativos_mei = resolve_pergunta_2(municipios, estabelecimentos, simples)
comercios_inativos_simples.to_csv(path_save+'comercios_inativos_simples.csv', index=False, header=True, sep=';')
comercios_inativos_mei.to_csvS(path_save+'comercios_inativos_mei.csv', index=False, header=True, sep=';')
print("Pergunta 2 - OK!")


print("- Solucionando 1")
industrias_ativas_simples, industrias_ativas_mei = resolve_pergunta_1(municipios, estabelecimentos, simples)
industrias_ativas_simples.to_csv(path_save+'industrias_ativas_simples.csv', index=False, header=True, sep=';')
industrias_ativas_mei.to_csv(path_save+'industrias_ativas_mei.csv', index=False, header=True, sep=';')
print("Pergunta 1 - OK!")
