import pandas as pd

def resolve_pergunta_2(df_municipios, df_estabelecimentos, df_simples):

    # Filtrar os CNPJs da tabela estabelecimento e que estão na tabela simples
    df_simples_selecao = df_estabelecimentos.loc[(df_estabelecimentos['CNPJ'].isin(df_simples['CNPJ']))]
    # Tira CNPJs do Exterior: ID_Município == 9707
    df_simples_selecao = df_simples_selecao.loc[~(df_simples_selecao["ID_Município"].isin([9707]))]
    
    # Filtrar os CNAEs que são comércio: comércio inicia com 45-47
    df_simples_usar = df_simples_selecao.loc[(df_simples_selecao['CNAE'] >= 4500000) & (df_simples_selecao['CNAE'] < 4800000)]                                         
    
    # Dataframe Simples filtrado
    df_simples_limpo =  df_simples.loc[df_simples['CNPJ'].isin(df_simples_usar['CNPJ'])]

    inativos_mei = pd.DataFrame(columns=['ID_Município','MEI_inativo', 'Data'])
    inativos_simples = pd.DataFrame(columns=['ID_Município','SIMPLES_inativo', 'Data'])

    datas = pd.date_range(start='01/01/2010', end='07/01/2021', freq='M')

    for date in datas:
        print(f"Entrou data {date}")

        aux_simples = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do simples']).month) == ((date).month))
                                            & ((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do simples']).year) == ((date).year))]
        mun_simples= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_simples['CNPJ'])]
        mun_simples_total=mun_simples.groupby(['ID_Município'], as_index=False).size()
        
        inativo_simples = mun_simples_total
        inativo_simples['Data'] = date
        inativo_simples.rename({'size':'SIMPLES_inativo'}, inplace=True, axis=1)

        aux_mei = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do MEI']).month) == ((date).month))
                                        & ((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do MEI']).year) == ((date).year))]
        mun_mei= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_mei['CNPJ'])]
        mun_mei_total=mun_mei.groupby(['ID_Município'], as_index=False).size()
        
        inativo_mei = mun_mei_total
        inativo_mei['Data'] = date
        inativo_mei.rename({'size':'MEI_inativo'}, inplace=True, axis=1)

        
        inativos_simples=inativos_simples.append(inativo_simples)
        inativos_mei=inativos_mei.append(inativo_mei)

    return inativos_simples, inativos_mei
        