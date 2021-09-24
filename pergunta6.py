# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 01:01:34 2021

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

df_estabelecimentos_1 = pd.read_csv("D:\cnpj\export1_estabelecimentos1.csv", sep=';')
df_estabelecimentos_1 = df_estabelecimentos_1.replace(0, np.nan)
df_empresas = pd.read_csv("D:cnpj\export_empresas.csv", sep=';') 
df_natjuridica = pd.read_csv("D:cnpj\export_natjuridica.csv", sep=';')

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


## filtrar a tabela de empresas pelos cnpjs que se mantém ativos no último ano:
df_pequena=df_empresas.loc[df_empresas['CNPJ'].isin(df_estabelecimentos_1['CNPJ'])]

## filtrar apenas empresas de pequeno porte
df_pequena = df_pequena.loc[df_pequena['Porte da Empresa'] == 3]

## transformando a coluna de capital social de string para float
df_pequena['Capital Social'] = df_pequena['Capital Social'].str.replace(',','.')
df_pequena['Capital Social'] = df_pequena['Capital Social'].astype(float)


# capitalnat = pd.DataFrame(columns=['ID_NJurídica','Capital'])
# capitalnat['ID_NJurídica'] = df_natjuridica['ID_NJurídica']

## agrupando por natureza jurídica e encontrando a média do capital social
capitalnat =df_pequena.groupby(['ID_NJurídica'], as_index=False)['Capital Social'].mean()

print("Salvando no banco de dados")
capitalnat.to_sql('capital_nat', con=conn, if_exists='replace', index=False)

print("Exportando planilha")
capitalnat.to_csv (r'export_capitalnat.csv', index = False, header=True, sep=';')


