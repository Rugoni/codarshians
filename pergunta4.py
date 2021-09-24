# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 22:05:23 2021

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

datas = pd.date_range(start='01/01/2015', end='01/01/2021', freq='Y') 
date=0

# Se 4, vamos tirar da análise
# Se 8, tirar
# Se 3, filtrar pela data da situação
# Se 1, tirar

novos_educa = pd.DataFrame(columns=['Data', 'UF','Educa'])



## filtrar os cnpjs que são grupo de educação superior: inicia com 853
df_novo_selecao = df_estabelecimentos_1.loc[(df_estabelecimentos_1['CNAE'] >= 8530000) & (df_estabelecimentos_1['CNAE'] < 8540000)]                                         


for date in datas:
    print(f"Entrou data {date}")

    novo_educa = pd.DataFrame(columns=['Data', 'UF','Educa'])
    
    aux_educa = df_novo_selecao.loc[((pd.DatetimeIndex(df_novo_selecao['Data de entrada']).year) == ((date).year))]
    uf_total=aux_educa.groupby('UF').size()
    novo_educa['UF'] = np.unique(df_estabelecimentos_1['UF'].values)
    novo_educa['Data']=date
    novo_educa['Educa']=uf_total
    
    novos_educa=novos_educa.append(novo_educa)
    

print("Salvando no banco de dados")
novos_educa.to_sql('novos_educa', con=conn, if_exists='replace', index=False)

print("Exportando planilha")
novos_educa.to_csv (r'export_novo_educa.csv', index = False, header=True, sep=';')
