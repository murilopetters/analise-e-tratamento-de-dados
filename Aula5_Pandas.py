# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt

# Leitura dos arquivos
df1 = pd.read_excel("Aracaju.xlsx")
df2 = pd.read_excel("Fortaleza.xlsx")
df3 = pd.read_excel("Natal.xlsx")
df4 = pd.read_excel("Recife.xlsx")
df5 = pd.read_excel("Salvador.xlsx")

# Juntando todos os arquivos
df = pd.concat([df1, df2, df3, df4, df5])

# Exibindo informações do DataFrame
print("Informações do DataFrame:")
print(df.info())

# Exibindo as 5 primeiras linhas
print("\n5 Primeiras Linhas:")
print(df.head())

# Exibindo as 5 últimas linhas
print("\n5 Últimas Linhas:")
print(df.tail())

# Verificando o tipo de dado de cada coluna
print("\nTipos de Dados:")
print(df.dtypes)

# Alterando o tipo de dado da coluna LojaID
df["LojaID"] = df["LojaID"].astype("object")

# Consultando linhas com valores faltantes
print("\nValores Faltantes:")
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

# Retornando a maior e menor receita
print("\nMaior Receita:", df["Receita"].max())
print("Menor Receita:", df["Receita"].min())

# nlargest e nsmallest
print("\nTop 3 Receitas:")
print(df.nlargest(3, "Receita"))
print("Bottom 3 Receitas:")
print(df.nsmallest(3, "Receita"))

# Agrupamento por cidade
print("\nReceita por Cidade:")
print(df.groupby("Cidade")["Receita"].sum())

# Ordenando o conjunto de dados
print("\nTop 10 Receitas:")
print(df.sort_values("Receita", ascending=False).head(10))

# Transformando a coluna de data em tipo inteiro
df["Data"] = df["Data"].astype("int64")

# Transformando coluna de data em data
df["Data"] = pd.to_datetime(df["Data"])

# Agrupamento por ano
print("\nReceita por Ano:")
print(df.groupby(df["Data"].dt.year)["Receita"].sum())

# Criando uma nova coluna com o ano
df["Ano_Venda"] = df["Data"].dt.year

# Extraindo o mês e o dia
df["mes_venda"], df["dia_venda"] = (df["Data"].dt.month, df["Data"].dt.day)

# Retornando a data mais antiga
print("\nData mais antiga:", df["Data"].min())

# Calculando a diferença de dias
df["diferenca_dias"] = (df["Data"] - df["Data"].min()).dt.days

# Criando a coluna de trimestre
df["trimestre_venda"] = df["Data"].dt.quarter

# Filtrando as vendas de 2019 do mês de março
vendas_marco_19 = df.loc[(df["Data"].dt.year == 2019) & (df["Data"].dt.month == 3)]

# Exibindo a amostra de 20 linhas
print("\nVendas de Março de 2019:")
print(vendas_marco_19.sample(20))

# Contagem de LojaID
print("\nContagem de LojaID:")
print(df["LojaID"].value_counts(ascending=False))

# Gráfico de barras
df["LojaID"].value_counts(ascending=False).plot.bar(title="Total vendas por LojaID", color="blue")
plt.xlabel("LojaID")
plt.ylabel("Total Vendas")
plt.show()

# Gráfico de barras horizontais
df["LojaID"].value_counts().plot.barh(title="Total vendas por LojaID", color="green")
plt.xlabel("Total Vendas")
plt.ylabel("LojaID")
plt.show()

# Gráfico de barras horizontais ordenado
df["LojaID"].value_counts(ascending=True).plot.barh(title="Total vendas por LojaID", color="purple")
plt.xlabel("Total Vendas")
plt.ylabel("LojaID")
plt.show()

# Gráfico de Pizza
df.groupby(df["Data"].dt.year)["Receita"].sum().plot.pie(title="Receita por Ano", autopct='%1.1f%%')
plt.show()

# Total vendas por cidade
print("\nTotal vendas por Cidade:")
print(df["Cidade"].value_counts())

# Gráfico de barras para vendas por cidade
df["Cidade"].value_counts().plot.bar(title="Total vendas por Cidade", color="orange")
plt.xlabel("Cidade")
plt.ylabel("Total Vendas")
plt.show()

# Salvando o gráfico em PNG
df_2019.groupby(df_2019["mes_venda"])["Qtde"].sum().plot(marker="v")
plt.title("Quantidade de produtos vendidos x mês")
plt.xlabel("Mês")
plt.ylabel("Total Produtos Vendidos")
plt.legend()
plt.savefig("grafico QTDE x MES.png")
plt.show()