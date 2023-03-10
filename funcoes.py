import pandas as pd
import numpy as np

## Todos os caracteres de troca
letras = list('abcdefghijklmnopqrstuvxwyz')
numeros = list('0123456789')
especial = list('.-_@()')
numeros_repre = list(map(str, range(1, 1 + len(numeros))))
letras_repre = list(map(str, range(11, 11 + len(letras))))
especial_repre = ['111', '222', '333', '444', '555', '666']
dicionario = dict(zip(letras, letras_repre))
dicionario.update(zip(numeros, numeros_repre))
dicionario.update(zip(especial, especial_repre))

## tabela de troca
tabela = str.maketrans(dicionario)

def modelar_data(tabela, df=None, string=None, maximos=None, minimos=None):
    if df is not None:
        df['dados_trans'] = df['dados'].map(lambda x: float(x.translate(tabela)))
        df['iniciais'] = df['dados'].map(lambda x: x[0:4])
        df['iniciais'] = df['iniciais'].map(lambda x: float(x.translate(tabela)))
        df['finais'] = df['dados'].map(lambda x: x[-3:])
        df['finais'] = df['finais'].map(lambda x: float(x.translate(tabela)))
        df['2_primeiros'] = df['dados'].map(lambda x: x[0:2])
        df['2_primeiros'] = df['2_primeiros'].map(lambda x: float(x.translate(tabela)))
        df['tamanho'] = df['dados'].map(lambda x: len(x))
        if maximos is not None and minimos is not None:
            colunas = df.drop(columns=['dados']).columns
            for coluna in colunas:
                df[coluna] = df[coluna].apply(lambda x: (x - minimos[coluna]) / (maximos[coluna] - minimos[coluna]))
        return df
    elif string is not None:
        df_test = pd.DataFrame({'dados': string}, index=[0])
        df_test['dados_trans'] = df_test['dados'].map(lambda x: float(x.translate(tabela)))
        df_test['iniciais'] = df_test['dados'].map(lambda x: x[0:4])
        df_test['iniciais'] = df_test['iniciais'].map(lambda x: float(x.translate(tabela)))
        df_test['finais'] = df_test['dados'].map(lambda x: x[-3:])
        df_test['finais'] = df_test['finais'].map(lambda x: float(x.translate(tabela)))
        df_test['2_primeiros'] = df_test['dados'].map(lambda x: x[0:2])
        df_test['2_primeiros'] = df_test['2_primeiros'].map(lambda x: float(x.translate(tabela)))
        df_test['tamanho'] = df_test['dados'].map(lambda x: len(x))
        if maximos is not None and minimos is not None:
            colunas = df_test.drop(columns=['dados']).columns
            for coluna in colunas:
                df_test[coluna] = df_test[coluna].apply(lambda x: (x - minimos[coluna]) / (maximos[coluna] - minimos[coluna]))
        return np.array(df_test.drop(columns=['dados']))