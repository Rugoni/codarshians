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

inativos_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_inativo'])
inativos_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_inativo' ])

df_municipios = pd.read_csv("D:\cnpj\export_municipios.csv", sep=';')
mun=0


## filtrar os cnpjs da tabela estabelecimento que não estão na tabela simples
df_simples_selecao = df_estabelecimentos_1.loc[(df_estabelecimentos_1['CNPJ'].isin(df_simples['CNPJ']))]

## filtrar os cnpjs que são comércio: comércio inicia com 45-47
df_simples_selecao = df_simples_selecao.loc[(df_simples_selecao['CNAE'] >= 4500000) & (df_simples_selecao['CNAE'] < 4800000)]                                         

## desconsiderar as situações cadastrais 1, 4 por serem incosistentes 
df_simples_usar = df_simples_selecao.loc[df_simples_selecao['Situação Cadastral'].isin([2,3,8])]
df_simples_limpo =  df_simples.loc[df_simples['CNPJ'].isin(df_simples_usar['CNPJ'])]



for date in datas:
    print(f"Entrou data {date}")
    inativo_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_inativo'])
    inativo_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_inativo'])
    # aux_inativo = df_simples_usar.loc[
    #     (df_simples_usar['Situação Cadastral'] == 3) & (df_simples_usar['Data Situação Cadastral'] < date)]

    
    # simples_usar = df_simples_limpo.loc[~df_simples_limpo['CNPJ'].isin(aux_excluir['CNPJ'])]


    aux_simples = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do simples']).month) == ((date).month))
                                        & ((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do simples']).year) == ((date).year))
                                        & (df_simples_limpo['Data de exclusão do simples'] != df_simples_limpo['Data de exclusão do MEI'])] ## dado desconsiderado
    mun_simples= df_estabelecimentos_1.loc[df_estabelecimentos_1['CNPJ'].isin(aux_simples['CNPJ'])]
    mun_simples_total=mun_simples.groupby('ID_Município').size()
    inativo_simples['ID_Município'] = df_municipios['ID_Município']
    inativo_simples['Data']=date
    inativo_simples['SIMPLES_inativo']=mun_simples_total

    aux_mei = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do MEI']).month) == ((date).month))
                                      & ((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do MEI']).year) == ((date).year))
                                    & ((df_simples_limpo['Data de exclusão do simples']) != (df_simples_limpo['Data de exclusão do MEI']))] ## dado desconsiderado
    mun_mei= df_estabelecimentos_1.loc[df_estabelecimentos_1['CNPJ'].isin(aux_mei['CNPJ'])]
    mun_mei_total=mun_mei.groupby('ID_Município').size()
    inativo_mei['ID_Município'] = df_municipios['ID_Município']
    inativo_mei['Data']=date
    inativo_mei['MEI_inativo']=mun_mei_total
    
    inativos_simples=inativos_simples.append(inativo_simples)
    inativos_mei=inativos_mei.append(inativo_mei)
    

print("Salvando no banco de dados")
inativos_mei.to_sql('inativos_mei', con=conn, if_exists='replace', index=False)
inativos_simples.to_sql('inativos_simples', con=conn, if_exists='replace', index=False)

print("Exportando planilha")
inativos_mei.to_csv (r'export_inativos_mei.csv', index = False, header=True, sep=';')
inativos_simples.to_csv (r'export_inativos_simples.csv', index = False, header=True, sep=';')



