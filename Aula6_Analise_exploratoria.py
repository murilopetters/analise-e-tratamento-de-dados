# Importando as bibliotecas
import pandas as pd
import matplotlib.pyplot as plt
plt.style.use("seaborn")

# Upload do arquivo
from google.colab import files
uploaded = files.upload()

# Criando nosso DataFrame
df = pd.read_excel("AdventureWorks.xlsx")

# Visualizando as 5 primeiras linhas
print("Visualizando as 5 primeiras linhas:")
print(df.head())

# Quantidade de linhas e colunas
print("\nQuantidade de linhas e colunas:")
print(df.shape)

# Verificando os tipos de dados
print("\nTipos de dados:")
print(df.dtypes)

# Qual a Receita total?
print("\nReceita total:")
print(df["Valor Venda"].sum())

# Qual o custo Total?
df["custo"] = df["Custo Unitário"].mul(df["Quantidade"])  # Criando a coluna de custo
print("\nCusto Total:")
print(round(df["custo"].sum(), 2))

# Agora que temos a receita e custo e o total, podemos achar o Lucro total
# Vamos criar uma coluna de Lucro que será Receita - Custo
df["lucro"] = df["Valor Venda"] - df["custo"]
print("\nLucro Total:")
print(round(df["lucro"].sum(), 2))

# Criando uma coluna com total de dias para enviar o produto
df["Tempo_envio"] = (df["Data Envio"] - df["Data Venda"]).dt.days
print("\nVisualizando Tempo_envio:")
print(df["Tempo_envio"])

# Média do tempo de envio por Marca
print("\nMédia do tempo de envio por Marca:")
print(df.groupby("Marca")["Tempo_envio"].mean())

# Verificando se temos dados faltantes
print("\nVerificando dados faltantes:")
print(df.isnull().sum())

# Agrupando por ano e marca
print("\nLucro por ano e marca:")
print(df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum())

# Resetando o índice
lucro_ano = df.groupby([df["Data Venda"].dt.year, "Marca"])["lucro"].sum().reset_index()
print("\nLucro por ano e marca (com índice resetado):")
print(lucro_ano)

# Qual o total de produtos vendidos?
print("\nTotal de produtos vendidos:")
print(df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=False))

# Gráfico Total de produtos vendidos
df.groupby("Produto")["Quantidade"].sum().sort_values(ascending=True).plot.barh(title="Total Produtos Vendidos")
plt.xlabel("Total")
plt.ylabel("Produto")
plt.show()

# Gráfico Lucro x Ano
df.groupby(df["Data Venda"].dt.year)["lucro"].sum().plot.bar(title="Lucro x Ano")
plt.xlabel("Ano")
plt.ylabel("Receita")
plt.show()

# Selecionando apenas as vendas de 2009
df_2009 = df[df["Data Venda"].dt.year == 2009]

# Gráfico Lucro x Mês
df_2009.groupby(df_2009["Data Venda"].dt.month)["lucro"].sum().plot(title="Lucro x Mês")
plt.xlabel("Mês")
plt.ylabel("Lucro")
plt.show()

# Gráfico Lucro x Marca
df_2009.groupby("Marca")["lucro"].sum().plot.bar(title="Lucro x Marca")
plt.xlabel("Marca")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()

# Gráfico Lucro x Classe
df_2009.groupby("Classe")["lucro"].sum().plot.bar(title="Lucro x Classe")
plt.xlabel("Classe")
plt.ylabel("Lucro")
plt.xticks(rotation='horizontal')
plt.show()

# Estatísticas descritivas do Tempo_envio
print("\nEstatísticas descritivas do Tempo_envio:")
print(df["Tempo_envio"].describe())

# Gráfico de Boxplot
plt.boxplot(df["Tempo_envio"])
plt.show()

# Histograma
plt.hist(df["Tempo_envio"])
plt.show()

# Tempo mínimo e máximo de envio
print("\nTempo mínimo de envio:", df["Tempo_envio"].min())
print("Tempo máximo de envio:", df['Tempo_envio'].max())

# Identificando o Outlier
print("\nIdentificando o Outlier:")
print(df[df["Tempo_envio"] == 20])

# Salvando o DataFrame em um arquivo CSV
df.to_csv("df_vendas_novo.csv", index=False)