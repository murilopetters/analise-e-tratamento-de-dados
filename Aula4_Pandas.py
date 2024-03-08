# Importando a biblioteca
import pandas as pd

# Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

# Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo as 5 primeiras linhas
print(df.head())

# Exibindo as 5 últimas linhas
print(df.tail())

# Amostra de 5 linhas aleatórias
print(df.sample(5))

# Verificando o tipo de dado de cada coluna
print(df.dtypes)

# Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

# Consultando linhas com valores faltantes
print(df.isnull().sum())

# Substituindo os valores nulos pela média
df["Vendas"].fillna(df["Vendas"].mean(), inplace=True)

# Substituindo os valores nulos por zero
df["Vendas"].fillna(0, inplace=True)

# Apagando as linhas com valores nulos
df.dropna(inplace=True)

# Apagando as linhas com valores nulos com base apenas em 1 coluna
df.dropna(subset=["Vendas"], inplace=True)

# Removendo linhas que estejam com valores faltantes em todas as colunas
df.dropna(how="all", inplace=True)

# Criando a coluna de receita
df["Receita"] = df["Vendas"].mul(df["Qtde"])

# Criando a coluna de Receita/Vendas
df["Receita/Vendas"] = df["Receita"] / df["Vendas"]

# Retornando a maior receita
print("Maior Receita:", df["Receita"].max())

# Retornando a menor receita
print("Menor Receita:", df["Receita"].min())

# nlargest
print("Top 3 Receitas:")
print(df.nlargest(3, "Receita"))

# nsmallest
print("Bottom 3 Receitas:")
print(df.nsmallest(3, "Receita"))

# Agrupamento por cidade
print("Receita por Cidade:")
print(df.groupby("Cidade")["Receita"].sum())

# Ordenando o conjunto de dados
print("Top 10 Receitas:")
print(df.sort_values("Receita", ascending=False).head(10))

# Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])

# Agrupamento por ano
print("Receita por Ano:")
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

# Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Retornando a data mais antiga
print("Data mais antiga:", df["Data"].min())

# Calculando a diferença de dias
df["diferenca_dias"] = (df["Data"] - df["Data"].min()).dt.days

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# Exibindo a amostra de 20 linhas
print("Vendas de Março de 2019:")
print(vendas_marco_19.sample(20))