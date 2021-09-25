import numpy as np
import pandas as pd

def resolve_pergunta_1(df_municipios, df_estabelecimentos, df_simples):
    
    # Filtrar os CNPJs da tabela estabelecimento e que estão na tabela simples
    df_simples_selecao = df_estabelecimentos.loc[(df_estabelecimentos['CNPJ'].isin(df_simples['CNPJ']))]
    # Tira CNPJs do Exterior: ID_Município == 9707
    df_simples_selecao = df_simples_selecao.loc[~(df_simples_selecao["ID_Município"].isin([9707]))]

    # Filtrar os CNAEs que são indústria: indústria inicia com 05-33
    df_simples_usar = df_simples_selecao.loc[(df_simples_selecao['CNAE'] >= 500000) & (df_simples_selecao['CNAE'] < 3400000)]
    
    # Dataframe Simples filtrado
    df_simples_limpo =  df_simples.loc[(df_simples['CNPJ'].isin(df_simples_usar['CNPJ']))]
    
    ativos_mei = pd.DataFrame(columns=['ID_Município','MEI_ativo', 'Data'])
    ativos_simples = pd.DataFrame(columns=['ID_Município','SIMPLES_ativo', 'Data' ])

    datas = pd.date_range(start='01/01/2010', end='07/01/2021', freq='M')

    for date in datas:
        print(f"Entrou data {date}")

        aux_simples = df_simples_limpo.loc[df_simples_limpo['Data de opção pelo simples'] <= date]
        aux_simples = aux_simples.loc[(aux_simples['Data de exclusão do simples'] > date) | (aux_simples['Data de exclusão do simples'] == np.nan)] ## pode ser que nao tenha data de exclusão
        mun_simples = df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_simples['CNPJ'])]
        mun_simples_total = mun_simples.groupby(['ID_Município'], as_index=False).size()

        ativo_simples = mun_simples_total
        ativo_simples['Data'] = date
        ativo_simples.rename({'size':'SIMPLES_ativo'}, inplace=True, axis=1)

        aux_mei = df_simples_limpo.loc[df_simples_limpo['Data de opção pelo MEI'] <= date]
        aux_mei = aux_mei.loc[(aux_mei['Data de exclusão do MEI'] > date) | (aux_simples['Data de exclusão do MEI'] == np.nan)]
        mun_mei= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_mei['CNPJ'])]
        mun_mei_total=mun_mei.groupby(['ID_Município'], as_index=False).size()
        
        ativo_mei = mun_mei_total
        ativo_mei['Data'] = date
        ativo_mei.rename({'size':'MEI_ativo'}, inplace=True, axis=1)
        
        ativos_simples=ativos_simples.append(ativo_simples)
        ativos_mei=ativos_mei.append(ativo_mei)

    return ativos_simples, ativos_mei