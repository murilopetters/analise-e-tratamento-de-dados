#Criando uma lista chamada animais
animais = [1,2,3]
animais

animais = ["cachorro", "gato", 12345, 6.5]
animais

#Imprimindo o primeiro elemento da lista
animais[0]

#Imprimindo o 4 elemento da lista
animais[3]

#Substituindo o primeiro elemento da lista
animais[0] = "papagaio"

animais

#Removendo gato da lista
animais.remove("gato")

animais

len(animais)

"gato" in animais

lista = [500, 30, 300, 80, 10]

max(lista)

min(lista)

animais.append(["leão", "Cachorro"])

animais

animais.extend(["cobra", 6])

animais

animais.count("leão")

lista.sort()

lista






#As tuplas usam parênteses como sintaxe
tp = ("Banana", "Maçã", 10, 50)

#Retornando o primeiro elemento
tp[0]

#Diferente das listas as tuplas são imutáveis, o que quer dizer que não podemos alterar os seus elementos
tp[0] = "Laranja"

tp.count("Maçã")

tp[0:2]





#Para criar um dicionário utilizamos as {}
dc = {"Maçã":20, "Banana":10, "Laranja":15, "Uva":5} #Dicionários trabalham com o condeito chave e valor

dc

#Acessando o valor de um dicionário através da chave
dc["Maçã"]

#Atualizando o valor da Maçã
dc["Maçã"] = 25
dc

#Retornando todas as chaves do dicionário
dc.keys()

#Retornando os valores do dicionário
dc.values()

#Verificando se já existe uma chave no dicionário e caso não exista inserir
dc.setdefault("Limão", 22)

dc