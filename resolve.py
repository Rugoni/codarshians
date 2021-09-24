import pandas as pd 
import numpy as np
# import psycopg2
from sqlalchemy import create_engine

# Conectando com o banco local 
# 'postgresql://user:password@host/database' 
# conn_string = 'postgresql://user:password@host/database' # Substituir credenciais
# conn = psycopg2.connect(conn_string)
# cursor = conn.cursor() 

# ## Conectando ao banco
# db = create_engine(conn_string)
# conn = db.connect()

print("Lê arquivos CSV:")

path = 'src/docker/src/data_csv/'


# print("- Porte da Empresa")
# porte_empresa = {
#     "Porte da Empresa": [1, 2, 3, 5],
#     "Descrição Porte": ['Não informado', 'Micro empresa', 'Empresa de pequeno porte', 'Demais']
# }
# df_porte_empresa = pd.DataFrame(porte_empresa)
# df_porte_empresa.to_feather('data_feather/porte.ftr')

# print("- Matriz/Filial")
# matriz = {
#     "Identificador Matriz/Filial": [1, 2],
#     "Matriz/Filial": ['Matriz', 'Filial']
# }
# df_matriz = pd.DataFrame(matriz)
# df_matriz.to_feather('data_feather/matriz.ftr')

# print("- Situação")
# situacao = {
#     "Código da Situação Cadastral": [1, 2, 3, 4, 8],
#     "Situação Cadastral": ['Nula', 'Ativa', 'Suspensa', 'Inapta', 'Baixada']
# }
# df_situacao = pd.DataFrame(situacao)
# df_situacao.to_feather('data_feather/situacao.ftr')

# print("- CNAE")
# df_cnae = pd.read_csv(path+"/export_CNAE.csv", sep=';')
# df_cnae.to_feather('data_feather/cnae.ftr')

# print("- Municípios")
# df_municipios = pd.read_csv(path+"export_municipios.csv", sep=';')
# df_municipios.to_feather('data_feather/municipios.ftr')

# print("- Natureza Jurídica")
# df_nat_juridica = pd.read_csv(path+"export_natjuridica.csv", sep=';')
# df_nat_juridica.to_feather('data_feather/natjuridica.ftr')

# print("- Simples")
# df_simples = pd.read_csv(path+"export_simples.csv", sep=';')
# df_simples = df_simples.replace(0, np.nan)
# for col in df_simples.columns:
#     if 'Data' in col:
#         df_simples[col] = pd.to_datetime(df_simples[col].astype(str), exact=False, errors='ignore', format='%Y%m%d')
# df_simples.to_feather('data_feather/simples.ftr')

# print("- Empresas")
# df_empresas = pd.read_csv(path+"export_empresas.csv", sep=';')
# df_empresas.drop("Razão Social", axis=1, inplace=True)
# df_empresas.to_feather('data_feather/empresas.ftr')

print("- Estabelecimentos")
# Read CSV
n = 25000000
df_estabelecimentos_1 = pd.read_csv(path+"export_estabelecimentos.csv", sep=';', nrows=n)
print("Leu 1")
df_estabelecimentos_2 = pd.read_csv(path+"export_estabelecimentos.csv", sep=';', skiprows=n+1, names=list(df_estabelecimentos_1.columns) )
print("Leu 2")

# Drop unnecessary columns 
df_estabelecimentos_1.drop(['CNPJ Ordem', 'CNPJ DV', 'Nome Fantasia', 'CNAE Secundário'], axis=1, inplace=True)
print("Drop 1")
df_estabelecimentos_2.drop(['CNPJ Ordem', 'CNPJ DV', 'Nome Fantasia', 'CNAE Secundário'], axis=1, inplace=True)
print("Drop 2")

# Rename column 'CNAE Principal' to 'CNAE'
df_estabelecimentos_1.rename({'CNAE Principal': 'CNAE'}, axis=1, inplace=True)
df_estabelecimentos_2.rename({'CNAE Principal': 'CNAE'}, axis=1, inplace=True)
print('1', len(df_estabelecimentos_1))
print('2', len(df_estabelecimentos_2))

#Select only rows from type 1 = Matriz, and drop the column
df_estabelecimentos_1 = df_estabelecimentos_1.loc[df_estabelecimentos_1['Identificador Matriz/Filial'] == 1]
df_estabelecimentos_2 = df_estabelecimentos_2.loc[df_estabelecimentos_2['Identificador Matriz/Filial'] == 1]
df_estabelecimentos_1.drop(['Identificador Matriz/Filial'], axis=1, inplace=True)
df_estabelecimentos_2.drop(['Identificador Matriz/Filial'], axis=1, inplace=True)
print('1', len(df_estabelecimentos_1))
print('2', len(df_estabelecimentos_2))

# Replace 0 to Nan
df_estabelecimentos_1 = df_estabelecimentos_1.replace(0, np.nan)
df_estabelecimentos_2 = df_estabelecimentos_2.replace(0, np.nan)

# Change data type from int to datetime in date columns
for col in df_estabelecimentos_1.columns:
    if 'Data' in col:
        df_estabelecimentos_1[col] = pd.to_datetime(df_estabelecimentos_1[col].astype(str), exact=False, errors='ignore', format='%Y%m%d')
        df_estabelecimentos_2[col] = pd.to_datetime(df_estabelecimentos_2[col].astype(str), exact=False, errors='ignore', format='%Y%m%d')

df_estabelecimentos = df_estabelecimentos_1.append(df_estabelecimentos_2, ignore_index=True)
print(len(df_estabelecimentos))

df_estabelecimentos.to_feather('data_feather/estabelecimentos.ftr')
df_estabelecimentos.to_csv('data_feather/estabelecimentos.csv', index = False, header=True, sep=';')







print(" -------- END -------- ")
