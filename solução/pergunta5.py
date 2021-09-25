import pandas as pd

def resolve_pergunta_5(df_estabelecimentos, df_empresas):

    datas = '01-01-2021'
    datas= pd.to_datetime(datas)

    # Filtrar os CNPJs que foram criados até 2020
    df_estabelecimentos = df_estabelecimentos.loc[(pd.to_datetime(df_estabelecimentos['Data de Início atividade'],
                                                                    errors ='coerce') < (datas))]

    # Retira os CNPJs que foram alterados (baixado, suspenso ou inapto) antes de 2020:
    datas = '01-01-2020'
    datas= pd.to_datetime(datas)

    df_cnpj_excluir = df_estabelecimentos.loc[((df_estabelecimentos['Situação Cadastral'].isin([1,3,4,8])) & 
                        ((pd.to_datetime(df_estabelecimentos['Data Situação Cadastral'], errors ='coerce')) < datas))]

    df_estabelecimentos = df_estabelecimentos.loc[~(df_estabelecimentos['CNPJ'].isin(df_cnpj_excluir['CNPJ']))]
    df_capital=df_empresas.loc[df_empresas['CNPJ'].isin(df_estabelecimentos['CNPJ'])]

    #incluir a coluna de CNAE apenas para os campos comuns de CNPJ
    df_capital=(pd.merge(df_capital, df_estabelecimentos, how='inner', on='CNPJ'))
    df_capital=df_capital.drop(columns=(['Situação Cadastral','Data Situação Cadastral','Data de Início atividade','UF','ID_Município']))

    ## transformando a coluna de CNAE para classe de CNAE
    df_capital['CNAE'] = df_capital['CNAE'].apply(lambda x: x//100)

    ## transformando a coluna de capital social de string para float
    df_capital['Capital Social'] = df_capital['Capital Social'].str.replace(',','.')
    df_capital['Capital Social'] = df_capital['Capital Social'].astype(float)

    capital = df_capital.groupby(['CNAE'], as_index=False)['Capital Social'].mean()

    return capital



