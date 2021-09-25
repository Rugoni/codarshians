
import pandas as pd
import numpy as np
import sqlalchemy
from sqlalchemy.orm import sessionmaker

print(" -------- START -------- ")

engine = sqlalchemy.create_engine("postgresql://admin:root@postgres_container:5432/cnpj_base")
con = engine.connect()

print("Lê arquivos CSV:")

path = './data_csv/'

# ----------------------- Parte 1 -----------------------
print("- Porte da Empresa")
porte_empresa = {
    "Porte da Empresa": [1, 2, 3, 5],
    "Descrição Porte": ['Não informado', 'Micro empresa', 'Empresa de pequeno porte', 'Demais']
}
df_porte_empresa = pd.DataFrame(porte_empresa)

print("- Matriz/Filial")
matriz = {
    "Identificador Matriz/Filial": [1, 2],
    "Matriz/Filial": ['Matriz', 'Filial']
}
df_matriz = pd.DataFrame(matriz)

print("- Situação")
situacao = {
    "Código da Situação Cadastral": [1, 2, 3, 4, 8],
    "Situação Cadastral": ['Nula', 'Ativa', 'Suspensa', 'Inapta', 'Baixada']
}
df_situacao = pd.DataFrame(situacao)

print("- CNAE")
df_cnae = pd.read_csv(path+"export_CNAE.csv", sep=';')

print("- Municípios")
df_municipios = pd.read_csv(path+"export_municipios.csv", sep=';')

print("- Natureza Jurídica")
df_nat_juridica = pd.read_csv(path+"export_natjuridica.csv", sep=';')

print("Deploy no Banco da Dados:")

print("- Porte da Empresa")
df_porte_empresa.to_sql('porte', con=engine, if_exists='replace', index=False)

print("- Matriz/Filial")
df_matriz.to_sql('matrizfilial', con=engine, if_exists='replace', index=False)

print("- Situação")
df_situacao.to_sql('situacao', con=engine, if_exists='replace', index=False)

print("- CNAE")
df_cnae.to_sql('cnae', con=engine, if_exists='replace', index=False)

print("- Municípios")
df_municipios.to_sql('municipios', con=engine, if_exists='replace', index=False)

print("- Natureza Jurídica")
df_nat_juridica.to_sql('natjuridica', con=engine, if_exists='replace', index=False)


# ----------------------- Parte 2 -----------------------

print("- Simples")
df_simples = pd.read_csv(path+"export_simples.csv", sep=';')
df_simples = df_simples.replace(0, np.nan)
for col in df_simples.columns:
    if 'Data' in col:
        df_simples[col] = pd.to_datetime(df_simples[col].astype(str), exact=False, errors='ignore', format='%Y%m%d')

print("Deploy no Banco da Dados:")
print("- Simples")
lines = len(df_simples)
print(lines)
interval = int(lines/100)
for i in range(100):
    print(f"Loop {i}")
    df_aux = df_simples.iloc[i*interval:(i+1)*interval]
    df_aux.to_sql('simples', con=engine, if_exists='append', chunksize=10000, method='multi', index=False)

# ----------------------- Parte 3 -----------------------

print("- Empresas")
df_empresas = pd.read_csv(path+"export_empresas.csv", sep=';')
df_empresas.drop("Razão Social", axis=1, inplace=True)
lines = len(df_empresas)
print(lines)

interval = int(lines/100)

for i in range(101):
    print(f"Loop {i}")
    df_aux = df_empresas.iloc[i*interval:(i+1)*interval]
    df_aux.to_sql('empresas', con=engine, if_exists='append', chunksize=10000, method='multi', index=False)

# ----------------------- Parte 4  -----------------------
print("- Estabelecimentos")
# Read CSV
n = 25000000
df_estabelecimentos_1 = pd.read_csv("./data_csv/export_estabelecimentos.csv", sep=';', nrows=n)
print("Leu 1")
df_estabelecimentos_2 = pd.read_csv("./data_csv/export_estabelecimentos.csv", sep=';', skiprows=n+1, names=list(df_estabelecimentos_1.columns) )
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

print(df_estabelecimentos_1.columns)

lines = len(df_estabelecimentos_1)
interval = int(lines/100)

for i in range(101):
    print(f"Loop {i}")
    df_aux_1 = df_estabelecimentos_1.iloc[i*interval:(i+1)*interval]
    df_aux_1.to_sql('estabelecimentos', con=engine, if_exists='append', chunksize=10000, method='multi', index=False)

    df_aux_2 = df_estabelecimentos_2.iloc[i*interval:(i+1)*interval]
    df_aux_2.to_sql('estabelecimentos', con=engine, if_exists='append', chunksize=10000, method='multi', index=False)


print(engine.table_names())
print(" -------- END -------- ")