import pandas as pd

def resolve_pergunta_6(df_estabelecimentos_1, df_empresas):

    datas = '01-01-2021'
    datas= pd.to_datetime(datas)

    ## filtrar os cnpjs que fora criado até 2020
    df_estabelecimentos_1 = df_estabelecimentos_1.loc[(pd.to_datetime(df_estabelecimentos_1['Data de Início atividade'],
                                                                    errors ='coerce') < (datas))]

    ## retira os cnpjs que foram alterado (baixado, suspenso ou inapto) antes de 2020:
    datas = '01-01-2020'
    datas= pd.to_datetime(datas)

    df_cnpj_excluir = df_estabelecimentos_1.loc[((df_estabelecimentos_1['Situação Cadastral'].isin([1,3,4,8])) & 
                        ((pd.to_datetime(df_estabelecimentos_1['Data Situação Cadastral'], errors ='coerce')) < datas))]

    df_estabelecimentos_1 = df_estabelecimentos_1.loc[~df_estabelecimentos_1['CNPJ'].isin(df_cnpj_excluir['CNPJ'])]


    ## filtrar a tabela de empresas pelos cnpjs que se mantém ativos no último ano:
    df_pequena=df_empresas.loc[df_empresas['CNPJ'].isin(df_estabelecimentos_1['CNPJ'])]

    ## filtrar apenas empresas de pequeno porte
    df_pequena = df_pequena.loc[df_pequena['Porte da Empresa'] == 3]

    ## transformando a coluna de capital social de string para float
    df_pequena['Capital Social'] = df_pequena['Capital Social'].str.replace(',','.')
    df_pequena['Capital Social'] = df_pequena['Capital Social'].astype(float)

    ## agrupando por natureza jurídica e encontrando a média do capital social
    capitalnat =df_pequena.groupby(['ID_NJurídica'], as_index=False)['Capital Social'].mean()

    return capitalnat



