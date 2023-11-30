import pandas as pd

dados = pd.read_csv("usuariosmicrosysmg.csv",sep=',', encoding="ISO-8859-1")
print(dados.columns)
dados['USU_NOME'] = dados['USU_NOME'].str.replace(';','')

print(dados)