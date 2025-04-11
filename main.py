import pandas as pd
from src.extractTransform import requestApiBcb
from src.load import salvarCsv

"""
    Salva um DataFrame em formato CSV.

    Parâmetros:
    - df (DataFrame): Os dados que serão salvos.
    - nome_arquivo (str): Nome do arquivo CSV a ser gerado.

    O arquivo será salvo com codificação UTF-8 e separador de vírgula.
    """
dadosBcb = requestApiBcb('20191')
salvarCsv(dadosBcb,"src/datasets/meiosPagamentosTri.csv", ";", ".")

