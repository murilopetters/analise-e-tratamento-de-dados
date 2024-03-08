# Importando a biblioteca pandas
import pandas as pd

# Lendo o arquivo CSV e tratando possíveis erros, definindo o separador como ";"
df = pd.read_csv("/content/drive/My Drive/Datasets/Gapminder.csv", error_bad_lines=False, sep=";")

# Visualizando as 5 primeiras linhas do DataFrame
print("5 primeiras linhas do DataFrame:")
print(df.head())

# Renomeando colunas do DataFrame
df = df.rename(columns={"country": "Pais", "continent": "Continente", "year": "Ano", "lifeExp": "Expectativa de vida", "pop": "Pop Total", "gdpPercap": "PIB"})

# Visualizando as 10 primeiras linhas após renomear as colunas
print("\n10 primeiras linhas após renomear as colunas:")
print(df.head(10))

# Obtendo o total de linhas e colunas no DataFrame
total_linhas_colunas = df.shape
print("\nTotal de linhas e colunas:")
print(total_linhas_colunas)

# Obtendo os nomes das colunas do DataFrame
nomes_colunas = df.columns
print("\nNomes das colunas:")
print(nomes_colunas)

# Obtendo os tipos de dados das colunas do DataFrame
tipos_dados_colunas = df.dtypes
print("\nTipos de dados das colunas:")
print(tipos_dados_colunas)

# Visualizando as últimas 15 linhas do DataFrame
print("\n15 últimas linhas do DataFrame:")
print(df.tail(15))

# Obtendo estatísticas descritivas do DataFrame
estatisticas_descritivas = df.describe()
print("\nEstatísticas descritivas:")
print(estatisticas_descritivas)

# Obtendo os valores únicos na coluna "continente"
continentes_unicos = df["Continente"].unique()
print("\nValores únicos na coluna 'Continente':")
print(continentes_unicos)

# Filtrando dados para o continente "Oceania"
oceania = df.loc[df["Continente"] == "Oceania"]
print("\nDados para o continente 'Oceania':")
print(oceania.head())

# Obtendo valores únicos na coluna "continente" para o DataFrame filtrado por Oceania
continentes_unicos_oceania = oceania["Continente"].unique()
print("\nValores únicos na coluna 'Continente' para Oceania:")
print(continentes_unicos_oceania)

# Agrupando por continente e contando a quantidade de países únicos
paises_por_continente = df.groupby("Continente")["Pais"].nunique()
print("\nQuantidade de países únicos por continente:")
print(paises_por_continente)

# Agrupando por ano e calculando a média da expectativa de vida
media_expectativa_vida_por_ano = df.groupby("Ano")["Expectativa de vida"].mean()
print("\nMédia da expectativa de vida por ano:")
print(media_expectativa_vida_por_ano)

# Calculando a média do PIB
media_pib = df["PIB"].mean()
print("\nMédia do PIB:")
print(media_pib)

# Calculando a soma do PIB
soma_pib = df["PIB"].sum()
print("\nSoma do PIB:")
print(soma_pib)