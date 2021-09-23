# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 20:02:36 2021

@author: prb
"""

import pandas as pd
# import numpy as np

## Rotinas de leitura de csv, com especificação de cabeçalho
motivo = pd.read_csv('motivo.csv', header=None, delimiter=(';'), names=["ID_Motivo","Motivo"])
CNAE = pd.read_csv('CNAE.csv', delimiter=(';'), header= None, encoding='latin-1', names=["CNAE","Descrição CNAE"])
municipios = pd.read_csv('municipios.csv', header= None, delimiter=(';'), names=["ID_Município","Município"])
natjuridica = pd.read_csv('natjuridica.csv', header= None,  delimiter=(';'), encoding='latin-1', names=["ID_NJurídica","Natureza Jurídica"])
simples = pd.read_csv('simples.csv', delimiter=(';'), header= None,  encoding='latin-1', names=["CNPJ", "Opção pelo Simples", "Data de opção pelo simples", "Data de exclusão do simples", "Opção pelo MEI", "Data de opção pelo MEI", "Data de exclusão do MEI"])

## Rotina de leitura de csv, seguido de concatenação e eleminação das colunas que não serão itulizadas
empresas = pd.concat([pd.read_csv('empresas0.csv', delimiter=(';'), header= None,  encoding='latin-1'),
                      pd.read_csv('empresas1.csv', delimiter=(';'), header= None, encoding='latin-1'),
                      pd.read_csv('empresas2.csv', delimiter=(';'),header= None,  encoding='latin-1'),
                      pd.read_csv('empresas3.csv', delimiter=(';'), header= None,  encoding='latin-1'),
                      pd.read_csv('empresas4.csv', delimiter=(';'), header= None, encoding='latin-1'),
                      pd.read_csv('empresas5.csv', delimiter=(';'), header= None,  encoding='latin-1'),
                      pd.read_csv('empresas6.csv', delimiter=(';'), header= None, encoding='latin-1'),
                      pd.read_csv('empresas7.csv', delimiter=(';'), header= None, encoding='latin-1'),
                      pd.read_csv('empresas8.csv', delimiter=(';'), header= None, encoding='latin-1'),
                      pd.read_csv('empresas9.csv', delimiter=(';'), header= None, encoding='latin-1')]).drop(columns=[3,6])
estabelecimentos = pd.concat([pd.read_csv('estabelecimento0.csv', header= None,delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento1.csv', header= None, delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento2.csv', header= None,  delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento3.csv', header= None,  delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento4.csv', header= None,  delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento5.csv', header= None, delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento6.csv', header= None, delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento7.csv', header= None, delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento8.csv', header= None, delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29]),
                             pd.read_csv('estabelecimento9.csv', header= None,  delimiter=(';'), encoding='latin-1').drop(columns=[7,8,9,13,14,15,16,17,18,21,22,23,24,25,26,27,28,29])])

## Definção dos cabeçalhos dos dataframe concatenados
empresas.columns = ["CNPJ","Razão Social", "ID_NJurídica", "Capital Social", "Porte da Empresa"]
estabelecimentos.columns = ["CNPJ", "CNPJ Ordem", "CNPJ DV", "Identificador Matriz/Filial", "Nome Fantasia", "Situação Cadastral", "Data Situação Cadastral", "Data de Início atividade", "CNAE Principal", "CNAE Secundário", "UF", "ID_Município"]


## Exportação dos dados gerados em csv
empresas.to_csv (r'export_empresas.csv', index = False, header=True, sep=';')
estabelecimentos.to_csv (r'export_estabelecimentos.csv', index = False, header=True, sep=';')
motivo.to_csv (r'export_motivo.csv', index = False, header=True, sep=';')
CNAE.to_csv (r'export_CNAE.csv', index = False, header=True, sep=';')
municipios.to_csv (r'export_municipios.csv', index = False, header=True, sep=';')
natjuridica.to_csv (r'export_natjuridica.csv', index = False, header=True, sep=';')
simples.to_csv (r'export_simples.csv', index = False, header=True, sep=';')
