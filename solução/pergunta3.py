import pandas as pd

def resolve_pergunta_3(df_municipios, df_estabelecimentos, df_simples):

    # Filtrar os CNPJs da tabela estabelecimento e que estão na tabela simples
    df_simples_selecao = df_estabelecimentos.loc[(df_estabelecimentos['CNPJ'].isin(df_simples['CNPJ']))]
    # Tira CNPJs do Exterior: ID_Município == 9707
    df_simples_usar = df_simples_selecao.loc[~(df_simples_selecao["ID_Município"].isin([9707]))]

    df_simples_limpo =  df_simples.loc[df_simples['CNPJ'].isin(df_simples_usar['CNPJ'])]
    
    novos_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_novo'])
    novos_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_novo'])

    datas = pd.date_range(start='01/01/2010', end='07/01/2021', freq='M')

    for date in datas:
        print(f"Entrou data {date}")
        novo_mei = pd.DataFrame(columns=['Data', 'ID_Município','MEI_novo'])
        novo_simples = pd.DataFrame(columns=['Data', 'ID_Município','SIMPLES_novo'])
        
        aux_simples = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de opção pelo simples']).year) == ((date).year))
                                            & ((pd.DatetimeIndex(df_simples_limpo['Data de opção pelo simples']).month) == ((date).month))]
        mun_simples= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_simples['CNPJ'])]
        mun_simples_total=mun_simples.groupby('ID_Município').size()
        novo_simples['ID_Município'] = df_municipios['ID_Município']
        novo_simples['Data']=date
        novo_simples['SIMPLES_novo']=mun_simples_total

        aux_mei = df_simples_limpo.loc[((pd.DatetimeIndex(df_simples_limpo['Data de opção pelo MEI']).year) == ((date).year))
                                        & ((pd.DatetimeIndex(df_simples_limpo['Data de opção pelo MEI']).month) == ((date).month))]
        mun_mei= df_simples_usar.loc[df_simples_usar['CNPJ'].isin(aux_mei['CNPJ'])]
        mun_mei_total=mun_mei.groupby('ID_Município').size()
        novo_mei['ID_Município'] = df_municipios['ID_Município']
        novo_mei['Data']=date
        novo_mei['MEI_novo']=mun_mei_total
        
        novos_simples=novos_simples.append(novo_simples)
        novos_mei=novos_mei.append(novo_mei)

    return novos_simples, novos_mei