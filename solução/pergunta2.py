import pandas as pd

def resolve_pergunta_2(df_municipios, df_estabelecimentos, df_simples):

    # Filtrar os CNPJs da tabela estabelecimento e que estão na tabela simples
    df_simples_selecao = df_estabelecimentos.loc[(df_estabelecimentos['CNPJ'].isin(df_simples['CNPJ']))]

    # Filtrar os CNAEs que são comércio: comércio inicia com 45-47
    df_simples_usar = df_simples_selecao.loc[(df_simples_selecao['CNAE'] >= 4500000) & (df_simples_selecao['CNAE'] < 4800000)]                                         
    
    # Dataframe Simples filtrado
    df_simples_limpo =  df_simples.loc[df_simples['CNPJ'].isin(df_simples_usar['CNPJ'])]

    inativos_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_inativo'])
    inativos_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_inativo' ])

    datas = pd.date_range(start='01/01/2010', end='07/01/2021', freq='M')

    for date in datas:
        print(f"Entrou data {date}")
        inativo_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_inativo'])
        inativo_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_inativo'])

        aux_simples = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do simples']).month) == ((date).month))
                                            & ((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do simples']).year) == ((date).year))]
        mun_simples= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_simples['CNPJ'])]
        mun_simples_total=mun_simples.groupby('ID_Município').size()
        inativo_simples['ID_Município'] = df_municipios['ID_Município']
        inativo_simples['Data']=date
        inativo_simples['SIMPLES_inativo']=mun_simples_total

        aux_mei = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do MEI']).month) == ((date).month))
                                        & ((pd.DatetimeIndex(df_simples_limpo['Data de exclusão do MEI']).year) == ((date).year))]
        mun_mei= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_mei['CNPJ'])]
        mun_mei_total=mun_mei.groupby('ID_Município').size()
        inativo_mei['ID_Município'] = df_municipios['ID_Município']
        inativo_mei['Data']=date
        inativo_mei['MEI_inativo']=mun_mei_total
        
        inativos_simples=inativos_simples.append(inativo_simples)
        inativos_mei=inativos_mei.append(inativo_mei)

    return inativos_simples, inativos_mei
        