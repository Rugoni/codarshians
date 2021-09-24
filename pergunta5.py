# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 01:01:34 2021

@author: prb
"""

import numpy as np
import psycopg2
from sqlalchemy import create_engine
import pandas as pd


# ## Conectando com o banco local   'postgresql://user:password@host/database' 
conn_string = 'postgresql://postgres:prb@localhost/hackathon' 
conn = psycopg2.connect(conn_string)
cursor = conn.cursor() 

## Conectando ao banco
db = create_engine(conn_string)
conn = db.connect()


df_estabelecimentos_1 = pd.read_csv("D:\cnpj\export1_estabelecimentos1.csv", sep=';')
df_estabelecimentos_1 = df_estabelecimentos_1.replace(0, np.nan)
df_empresas = pd.read_csv("D:cnpj\export_empresas.csv", sep=';') 
# df_CNAE = pd.read_csv("D:cnpj\export_CNAE.csv", sep=';') #####
# print(df_estabelecimentos_1)

datas = '01-01-2021'
datas= pd.to_datetime(datas)


## filtrar os cnpjs que fora criado até 2020
df_estabelecimentos_1 = df_estabelecimentos_1.loc[(pd.to_datetime(df_estabelecimentos_1['Data de Início atividade'],
                                                                  errors ='coerce') < (datas))]

## retira os cnpjs que foram alterado (baixado, suspenso ou inapto) antes de 2020:
datas = '01-01-2020'
datas= pd.to_datetime(datas)

df_cnpj_excluir = df_estabelecimentos_1.loc[((df_estabelecimentos_1['Situação Cadastral'].isin([1,3,4,8])) & 
                       ((pd.to_datetime(df_estabelecimentos_1['Data Situação Cadastral'], errors ='coerce')) < datas))]

df_estabelecimentos_1 = df_estabelecimentos_1.loc[~df_estabelecimentos_1['CNPJ'].isin(df_cnpj_excluir['CNPJ'])]
df_capital=df_empresas.loc[df_empresas['CNPJ'].isin(df_estabelecimentos_1['CNPJ'])]

#incluir a coluna de CNAE apenas para os campos comuns de CNPJ
df_capital=(pd.merge(df_capital, df_estabelecimentos_1, how='inner', on='CNPJ'))
df_capital=df_capital.drop(columns=(['Situação Cadastral','Data Situação Cadastral','Data de Início atividade','UF','ID_Município']))

## transformando a coluna de CNAE para classe de CNAE
df_capital['CNAE'] = df_capital['CNAE'].apply(lambda x: x//100)

## transformando a coluna de capital social de string para float
df_capital['Capital Social'] = df_capital['Capital Social'].str.replace(',','.')
df_capital['Capital Social'] = df_capital['Capital Social'].astype(float)

capital =df_capital.groupby(['CNAE'], as_index=False)['Capital Social'].mean()


print("Salvando no banco de dados")
capital.to_sql('capital', con=conn, if_exists='replace', index=False)

print("Exportando planilha")
capital.to_csv (r'export_capital.csv', index = False, header=True, sep=';')


