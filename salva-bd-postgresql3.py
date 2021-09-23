# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import psycopg2
from sqlalchemy import create_engine
import pandas as pd
# ## Conectando com o banco local   'postgresql://user:password@host/database' 
conn_string = postgresql://user:password@host/database
conn = psycopg2.connect(conn_string)
cursor = conn.cursor() 

## Conectando ao banco
db = create_engine(conn_string)
conn = db.connect()


# ## ler csv motivo e salvar no banco
# print("Criando dataframe - motivo")
# motivo = pd.read_csv(r"D:\cnpj\motivo.csv", delimiter=(";"), names=['ID_Motivo','Motivo'])
# print("Salvando motivo no banco")
# motivo.to_sql('motivo', con=conn, if_exists="replace", index=False)

# print("Criando dataframe - CNAE")
# CNAE = pd.read_csv(r"D:\cnpj\CNAE.csv", delimiter=(";"), names=['CNAE','Descrição CNAE'])
# print("Salvando CNAE no banco")
# CNAE.to_sql('CNAE', con=conn, if_exists='replace', index=False)

# print("Criando dataframe - municipios")
# municipios = pd.read_csv(r"D:\cnpj\municipios.csv", delimiter=(";"), names=['ID_Município','Município'])
# print("Salvando municipios no banco")
# municipios.to_sql('municipios', con=conn, if_exists='replace', index=False)

# print("Criando dataframe - natjuridica")
# natjuridica = pd.read_csv(r"D:\cnpj\natjuridica.csv", delimiter=(";"), names=['ID_NJurídica','Natureza Jurídica'])
# print("Salvando natjuridica no banco")
# natjuridica.to_sql('natjuridica', con=conn, if_exists='replace', index=False)

# print("Criando dataframe - simples")
# simples = pd.read_csv(r"D:\cnpj\simples.csv", delimiter=(";"), names=['CNPJ', 'Opção pelo Simples', 'Data de opção pelo simples', 'Data de exclusão do simples', 'Opção pelo MEI', 'Data de opção pelo MEI', 'Data de exclusão do MEI'])
# print("transformando os dados de inteiros para string")
# simples['Data de opção pelo simples'] = simples['Data de opção pelo simples'].astype(str)
# simples['Data de exclusão do simples'] = simples['Data de exclusão do simples'].astype(str)
# simples['Data de opção pelo MEI'] = simples['Data de opção pelo MEI'].astype(str)
# simples['Data de exclusão do MEI'] = simples['Data de exclusão do MEI'].astype(str)
# print("transformar dados para datetime")
# simples['Data de opção pelo simples']=pd.to_datetime(simples['Data de opção pelo simples'], dayfirst=True, errors='coerce' )
# simples['Data de exclusão do simples']=pd.to_datetime(simples['Data de exclusão do simples'], dayfirst=True,errors='coerce' )
# simples['Data de opção pelo MEI']=pd.to_datetime(simples['Data de opção pelo MEI'], dayfirst=True, errors='coerce' )
# simples['Data de exclusão do MEI']=pd.to_datetime(simples['Data de exclusão do MEI'], dayfirst=True,errors='coerce' )
# print("Salvando simples no banco - parte 1")
# simples2=simples.iloc[int(len(simples)/3):2*int(len(simples)/3)]
# simples3=simples.iloc[2*int(len(simples)/3):len(simples)]
# simples=simples.iloc[0:int(len(simples)/3)]
# simples.to_sql('simples', con=conn, if_exists='replace', index=False)
# print("Salvando simples no banco - parte 2")
# simples2.to_sql('simples', con=conn, if_exists='append', index=False)
# print("Salvando simples no banco - parte 3")
# simples3.to_sql('simples', con=conn, if_exists='append', index=False)

####### Empresas #############
# print("Criando dataframe - empresas0")
# empresas = pd.read_csv(r"D:\cnpj\empresas0.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas0 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='replace', index=False)

# print("Criando dataframe - empresas1")
# empresas = pd.read_csv(r"D:\cnpj\empresas1.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas1 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False)                                                                                               

# print("Criando dataframe - empresas2")
# empresas = pd.read_csv(r"D:\cnpj\empresas2.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas2 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False)                                                                          

# print("Criando dataframe - empresas3")
# empresas = pd.read_csv(r"D:\cnpj\empresas3.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas3 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False) 

# print("Criando dataframe - empresas4")
# empresas = pd.read_csv(r"D:\cnpj\empresas4.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas4 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - empresas5")
# empresas = pd.read_csv(r"D:\cnpj\empresas5.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas5 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False) 

# print("Criando dataframe - empresas6")
# empresas = pd.read_csv(r"D:\cnpj\empresas6.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas6 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - empresas7")
# empresas = pd.read_csv(r"D:\cnpj\empresas7.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas7 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False) 

# print("Criando dataframe - empresas8")
# empresas = pd.read_csv(r"D:\cnpj\empresas8.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas8 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False) 

# print("Criando dataframe - empresas9")
# empresas = pd.read_csv(r"D:\cnpj\empresas9.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,3,6])
# empresas.columns = ['CNPJ','ID_NJurídica', 'Capital Social', 'Porte da Empresa']
# print("Salvando empresas9 no banco")
# empresas.to_sql('empresas', con=conn, if_exists='append', index=False)  

########################

#### Estabelecimentos ############
# print("Criando dataframe - estabelecimento0")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento0.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento0 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='replace', index=False)

# print("Criando dataframe - empresas1")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento1.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento1 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)                                                                                                 

# print("Criando dataframe - estabelecimento2")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento2.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento2 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)                                                                           

# print("Criando dataframe - estabelecimento3")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento3.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento3 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - estabelecimento4")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento4.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento4 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - estabelecimento5")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento5.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento5 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - estabelecimento6")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento6.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento6 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - estabelecimento7")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento7.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento7 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - estabelecimento8")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento8.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento8 no banco")
# estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

# print("Criando dataframe - estabelecimento9")
# estabelecimentos = pd.read_csv(r"D:\cnpj\estabelecimento9.csv", delimiter=(';'), header= None, encoding='latin-1').drop(columns=[1,2,4,7,8,9,12,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])
# estabelecimentos.columns = ['CNPJ', 'Identificador Matriz/Filial', 'Situação Cadastral', 'Data Situação Cadastral', 'Data de Início atividade', 'CNAE', 'UF', 'ID_Município']
# print("transformando os dados de inteiros para string")
# estabelecimentos['Data Situação Cadastral'] = estabelecimentos['Data Situação Cadastral'].astype(str)
# estabelecimentos['Data de Início atividade'] = estabelecimentos['Data de Início atividade'].astype(str)
# print("corrigir data de situação cadastral")
# estabelecimentos['Data Situação Cadastral']=pd.to_datetime(estabelecimentos['Data Situação Cadastral'], dayfirst=True, errors='coerce' )
# print("corrigir data de início")
# estabelecimentos['Data de Início atividade']=pd.to_datetime(estabelecimentos['Data de Início atividade'], dayfirst=True,errors='coerce' )
# print("Salvando estabelecimento9 no banco")
#estabelecimentos.to_sql('estabelecimentos', con=conn, if_exists='append', index=False)  

######################

print('Criando os dataframes complementares')
print('Porte da empresa')
porte = pd.DataFrame(np.array([[1, 'Não informado'],
                               [2, 'Micro empresa'],
                               [3, 'Empresa de pequeno porte'],
                               [5,'Demais']]), columns=['Porte da Empresa', 'Descrição Porte'])
print('Salvando tabela porte no banco')
porte.to_sql('porte', con=conn, if_exists='replace', index=False) 


print('Matriz/Filial')
matrizfilial = pd.DataFrame(np.array([[1, 'Matriz'],
                                      [2, 'Filial']]), columns=['Identificador Matriz/Filial', 'Matriz/Filial'])
print('Salvando tabela matriz/filial no banco')
matrizfilial.to_sql('matrizfilial', con=conn, if_exists='replace', index=False) 


print('Situação cadastral')
situacao = pd.DataFrame(np.array([[1, 'Nula'],
                                  [2, 'Ativa'],
                                  [3,'Suspensa'],
                                  [4, 'Inapta'],
                                  [8,'Baixada']]), columns=['Situação Cadastral', 'Descrição Situação Cadastral'])
print('Salvando tabela situação cadastral no banco')
situacao.to_sql('situacao', con=conn, if_exists='replace', index=False) 

# ## Encerrar a comunicação no banco
cursor.close()
conn.close






########### Outras formas de fazer #############

# ## Conectar ao banco
# conn_string = """
#              host ='localhost'
#              dbname='hackathon'
#              user='postgres'
#              password='prb'
#              port='5432'
#              """
# try: 
#     conn = psycopg2.connect(conn_string)
#     cursor = conn.cursor() 
#     print ('Conectado!\n')
# except psycopg2.Error as e:
#     print('\nFalha de conexão!\n%s' % (e))


# ## Criando a tabela no banco
# cursor.execute(table_create_sql)
# cursor.execute('TRUNCATE TABLE motivo') #Truncate se já houver dados

# ## Transformando o dataframe em csv
# motivo.to_csv('export2_motivo.csv', index=False, header=False)


# ## executando 
# cursor.execute(sql)


# ## Fazer as alterações no banco
# conn.commit()


# ###################################

# ## transformar o dataframe em sql
# motivo.to_sql('motivo', con=conn, if_exists='replace', index=False,)

# ## Comandos no banco, igual SQL
# cursor.execute("CREATE TABLE test (id serial PRIMARY KEY, num integer, data varchar);")
# cursor.execute("INSERT INTO empresas(id_njuridica, capital_social) VALUES (01,100);")

# ## Fazer as alterações no banco
# conn.commit()

# ## Encerrar a comunicação no banco
# cursor.close()
# conn.close
