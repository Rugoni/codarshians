# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 21:53:22 2021

@author: prb
"""

# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:48:41 2021

@author: prb
"""

import numpy as np
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime
# ## Conectando com o banco local   'postgresql://user:password@host/database' 
conn_string = 'postgresql://postgres:prb@localhost/hackathon' 
conn = psycopg2.connect(conn_string)
cursor = conn.cursor() 

## Conectando ao banco
db = create_engine(conn_string)
conn = db.connect()


print("- Simples")
df_simples = pd.read_csv("D:cnpj\export_simples.csv", sep=';')
df_simples = df_simples.replace(0, np.nan)
for col in df_simples.columns:
    if 'Data' in col:
        df_simples[col] = pd.to_datetime(df_simples[col].astype(str), exact=False, errors='ignore', format='%Y%m%d')
# print(df_simples["Data de opção pelo simples"])
# print(df_simples["Data de exclusão do simples"])
print(df_simples)

df_estabelecimentos_1 = pd.read_csv("D:\cnpj\export_estabelecimentos.csv", sep=';')
df_estabelecimentos_1.drop(['CNPJ Ordem', 'CNPJ DV', 'Nome Fantasia', 'CNAE Secundário'], axis=1, inplace=True)
df_estabelecimentos_1.rename({'CNAE Principal': 'CNAE'}, axis=1, inplace=True)
df_estabelecimentos_1 = df_estabelecimentos_1.loc[df_estabelecimentos_1['Identificador Matriz/Filial'] == 1]
df_estabelecimentos_1.drop(['Identificador Matriz/Filial'], axis=1, inplace=True)
df_estabelecimentos_1 = df_estabelecimentos_1.replace(0, np.nan)
for col in df_estabelecimentos_1.columns:
    if 'Data' in col:
        df_estabelecimentos_1[col] = pd.to_datetime(df_estabelecimentos_1[col].astype(str), exact=False, errors='ignore', format='%Y%m%d')
# df_estabelecimentos_1.to_csv (r'export1_estabelecimentos1.csv', index = False, header=True, sep=';')

# print(df_estabelecimentos_1)

datas = pd.date_range(start='01/01/2010', end='01/01/2021', freq='M')
date=0

# Se 4, vamos tirar da análise
# Se 8, tirar
# Se 3, filtrar pela data da situação
# Se 1, tirar

novos_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_novo'])
novos_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_novo' ])

df_municipios = pd.read_csv("D:\cnpj\export_municipios.csv", sep=';')
mun=0


## filtrar os cnpjs da tabela estabelecimento que não estão na tabela simples
df_simples_selecao = df_estabelecimentos_1.loc[(df_estabelecimentos_1['CNPJ'].isin(df_simples['CNPJ']))]


## desconsiderar as situações cadastrais 1, 4 por serem incosistentes 
df_simples_usar = df_simples_selecao.loc[df_simples_selecao['Situação Cadastral'].isin([2,3,8])]
df_simples_limpo =  df_simples.loc[df_simples['CNPJ'].isin(df_simples_usar['CNPJ'])]


for date in datas:
    print(f"Entrou data {date}")
    novo_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_novo'])
    novo_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_novo'])
    
    aux_simples = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de opção pelo simples']).year) == ((date).year))
                                       & (df_simples_limpo['Data de opção pelo simples'] != df_simples_limpo['Data de opção pelo MEI'])]
    mun_simples= df_estabelecimentos_1.loc[df_estabelecimentos_1['CNPJ'].isin(aux_simples['CNPJ'])]
    mun_simples_total=mun_simples.groupby('ID_Município').size()
    novo_simples['ID_Município'] = df_municipios['ID_Município']
    novo_simples['Data']=date
    novo_simples['SIMPLES_novo']=mun_simples_total

    aux_mei = df_simples_limpo.loc[(((df_simples_limpo['Data de opção pelo MEI']).year) == ((date).year))
                                   & (df_simples_limpo['Data de opção pelo simples'] != df_simples_limpo['Data de opção pelo MEI'])]
    mun_mei= df_estabelecimentos_1.loc[df_estabelecimentos_1['CNPJ'].isin(aux_mei['CNPJ'])]
    mun_mei_total=mun_mei.groupby('ID_Município').size()
    novo_mei['ID_Município'] = df_municipios['ID_Município']
    novo_mei['Data']=date
    novo_mei['MEI_novo']=mun_mei_total
    
    novos_simples=novos_simples.append(novo_simples)
    novos_mei=novos_mei.append(novo_mei)
    

print("Salvando no banco de dados")
novos_mei.to_sql('novos_mei', con=conn, if_exists='replace', index=False)
novos_simples.to_sql('novos_simples', con=conn, if_exists='replace', index=False)

print("Exportando planilha")
novos_mei.to_csv (r'export_novos_mei.csv', index = False, header=True, sep=';')
novos_simples.to_csv (r'export_novos_simples.csv', index = False, header=True, sep=';')