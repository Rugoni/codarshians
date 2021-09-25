import pandas as pd


def resolve_pergunta_4(df_estabelecimentos):

    # Filtrar os CNAEs que são grupo de educação superior: inicia com 853
    df_novo_selecao = df_estabelecimentos.loc[(df_estabelecimentos['CNAE'] >= 8530000) & (df_estabelecimentos['CNAE'] < 8540000)]

    novos_educa = pd.DataFrame()

    datas = pd.date_range(start='01/01/2015', end='07/01/2021', freq='Y') 

    for date in datas:
        print(f"Entrou data {date}")

        novo_educa = pd.DataFrame(columns=['Data', 'UF','Educa'])

        aux_educa = df_novo_selecao.loc[((pd.DatetimeIndex(df_novo_selecao['Data de Início atividade']).year) == ((date).year))]
        uf_total = aux_educa.groupby('UF', as_index=False).size()
        novo_educa = uf_total
        novo_educa['Data']=date
        
        novos_educa = novos_educa.append(novo_educa)

    novos_educa.rename({'size': 'Educa'}, axis=1, inplace=True)
    
    return novos_educa

