import pandas as pd
# import numpy as np
# import psycopg2
# from sqlalchemy import create_engine


# # ## Conectando com o banco local   'postgresql://user:password@host/database' 
# conn_string = 'postgresql://postgres:prb@localhost/hackathon' 
# conn = psycopg2.connect(conn_string)
# cursor = conn.cursor() 

# ## Conectando ao banco
# db = create_engine(conn_string)
# conn = db.connect()


# df_municipios = pd.read_csv("src/docker/src/data_csv/export_municipios.csv", sep=';')
# print(df_municipios)

# df_municipios.to_feather(path='municipios.ftr')

# mun = pd.read_feather('municipios.ftr')
# print(mun)

df_estabelecimentos_1 = pd.read_csv("src/docker/src/data_csv/export_estabelecimentos.csv", sep=';')
df_estabelecimentos_1.to_feather('estabelecimentos.ftr')
# n = 25000000
# df_estabelecimentos_1 = pd.read_csv("src/docker/src/data_csv/export_estabelecimentos.csv", sep=';', nrows=n)
# print(df_estabelecimentos_1.columns)
# df_estabelecimentos_2 = pd.read_csv("src/docker/src/data_csv/export_estabelecimentos.csv", sep=';', skiprows=n+1, names=list(df_estabelecimentos_1.columns))

# df_estabelecimentos_1.drop(['CNPJ', 'CNPJ Ordem', 'CNPJ DV', 'Identificador Matriz/Filial',
#        'Nome Fantasia', 'Situação Cadastral', 'Data Situação Cadastral',
#        'Data de Início atividade', 'CNAE Principal', 'CNAE Secundário'], axis=1, inplace=True)
# df_estabelecimentos_1.drop_duplicates(subset='ID_Município', inplace=True)

# df_estabelecimentos_2.drop(['CNPJ', 'CNPJ Ordem', 'CNPJ DV', 'Identificador Matriz/Filial',
#        'Nome Fantasia', 'Situação Cadastral', 'Data Situação Cadastral',
#        'Data de Início atividade', 'CNAE Principal', 'CNAE Secundário'], axis=1, inplace=True)
# df_estabelecimentos_2.drop_duplicates(subset='ID_Município', inplace=True)

# municipios = df_estabelecimentos_1.append(df_estabelecimentos_2)

# municipios.drop_duplicates(subset='ID_Município', inplace=True)
# print(municipios)

# print("Salvando no banco de dados")
# municipios.to_sql('capital', con=conn, if_exists='replace', index=False)

# print("Exportando planilha")
# municipios.to_csv (r'export_municipios_UF.csv', index = False, header=True, sep=';')