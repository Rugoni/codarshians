# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:48:41 2021

@author: prb
"""

import numpy as np
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# ## Conectando com o banco local   'postgresql://user:password@host/database' 
conn_string = 'postgresql://user:password@host/database' 
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

ativos_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_ativo'])
ativos_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_ativo' ])

df_municipios = pd.read_csv("D:\cnpj\export_municipios.csv", sep=';')
mun=0


## filtrar os cnpjs da tabela estabelecimento que não estão na tabela simples
df_simples_selecao = df_estabelecimentos_1.loc[(df_estabelecimentos_1['CNPJ'].isin(df_simples['CNPJ']))]

## filtrar os cnpjs que não são indústria: indústria inicia com 05-33
df_simples_selecao = df_simples_selecao.loc[(df_simples_selecao['CNAE'] >= 5000000) & (df_simples_selecao['CNAE'] < 34000000)]                                         

## desconsiderar as situações cadastrais 1, 4 e 8 por serem incosistentes 
df_simples_usar = df_simples_selecao.loc[df_simples_selecao['Situação Cadastral'].isin([2,3])]
df_simples_limpo =  df_simples.loc[df_simples['CNPJ'].isin(df_simples_usar['CNPJ'])]


for date in datas:
    print(f"Entrou data {date}")
    ativo_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_ativo'])
    ativo_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_ativo'])
    aux_excluir = df_simples_usar.loc[
        (df_simples_usar['Situação Cadastral'] == 3) & (df_simples_usar['Data Situação Cadastral'] < date)]

    
    simples_usar = df_simples_limpo.loc[~df_simples_limpo['CNPJ'].isin(aux_excluir['CNPJ'])]


    aux_simples = simples_usar.loc[simples_usar['Data de opção pelo simples'] <= date]
    aux_simples = aux_simples.loc[(aux_simples['Data de exclusão do simples'] > date) | (aux_simples['Data de exclusão do simples'] == np.nan)] ## pode ser que nao tenha data de exclusão
    mun_simples= df_estabelecimentos_1.loc[df_estabelecimentos_1['CNPJ'].isin(aux_simples['CNPJ'])]
    mun_simples_total=mun_simples.groupby('ID_Município').size()
    ativo_simples['ID_Município'] = df_municipios['ID_Município']
    ativo_simples['Data']=date
    ativo_simples['SIMPLES_ativo']=mun_simples_total

    aux_mei = simples_usar.loc[simples_usar['Data de opção pelo MEI'] <= date]
    aux_mei = aux_mei.loc[(aux_mei['Data de exclusão do MEI'] > date) | (aux_simples['Data de exclusão do MEI'] == np.nan)]
    mun_mei= df_estabelecimentos_1.loc[df_estabelecimentos_1['CNPJ'].isin(aux_mei['CNPJ'])]
    mun_mei_total=mun_mei.groupby('ID_Município').size()
    ativo_mei['ID_Município'] = df_municipios['ID_Município']
    ativo_mei['Data']=date
    ativo_mei['MEI_ativo']=mun_mei_total
    
    ativos_simples=ativos_simples.append(ativo_simples)
    ativos_mei=ativos_mei.append(ativo_mei)
    
    # for mun in (df_municipios['ID_Município']):
    #     print(f"Entrou no municipio {mun}")
    #     mun_mei = len(df_estabelecimentos_1.loc[((df_estabelecimentos_1['ID_Município'] == mun) & (df_estabelecimentos_1['CNPJ'].isin(aux_mei['CNPJ'])))])
    #     mun_simples = len(df_estabelecimentos_1.loc[((df_estabelecimentos_1['ID_Município'] == mun) & (df_estabelecimentos_1['CNPJ'].isin(aux_simples['CNPJ'])))])
    #     print("Atualizou o dataframe")
    #     ativo=pd.DataFrame({'Data': [date], 'MEI_ativo': [mun_mei],'SIMPLES_ativo': [mun_simples], 'ID_Município': [mun]})
    #     ativos=ativos.append(ativo)



print("Salvando no banco de dados")
ativos_mei.to_sql('ativos_mei', con=conn, if_exists='replace', index=False)
ativos_simples.to_sql('ativos_simples', con=conn, if_exists='replace', index=False)

print("Exportando planilha")
ativos_mei.to_csv (r'export_ativos1_mei.csv', index = False, header=True, sep=';')
ativos_simples.to_csv (r'export_ativos_simples1.csv', index = False, header=True, sep=';')